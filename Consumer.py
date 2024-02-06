from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col , udf , expr
from pyspark.sql.types import StructType, StructField, StringType, FloatType, ArrayType
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegressionModel
import json
from pyspark.sql.functions import when

# UDF Tanımı
def parse_json(json_str):
    try:
        # JSON string'ini yükleyip parse ediyoruz
        json_obj = json.loads(json_str)
        # Sırayla her bir key-value çiftini alıyoruz
        result = {}
        for key, value in json_obj.items():
            # Anahtar değerini kullanarak her bir değeri alıyoruz
            result[key] = float(list(value.values())[0])
        return result
    except json.JSONDecodeError:
        # Hata durumunda boş bir sözlük döndürüyoruz
        return {key: None for key in json_obj.keys()}

# UDF'yi kaydediyoruz
parse_json_udf = udf(parse_json, StructType([

    StructField("Pclass", FloatType()),
    StructField("Sex", FloatType()),
    StructField("Age", FloatType()),
    StructField("SibSp", FloatType()),
    StructField("Parch", FloatType()),
    StructField("Fare", FloatType()),
    StructField("Embarked", FloatType()),
    StructField("Survived", FloatType())
]))

# Spark Session başlatma
spark = SparkSession \
    .builder \
    .appName("KafkaSparkStreamingConsumer") \
    .getOrCreate()

# Kafka'dan veri okuma
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "test") \
    .option("maxOffsetsPerTrigger", 1) \
    .load()

# Byte verileri string'e çevirme ve 'json' olarak adlandırma
json_df = df.selectExpr("CAST(value AS STRING) as json")

# JSON string'leri parse ederek yeni bir DataFrame oluşturma
parsed_df = json_df.select(parse_json_udf(col("json")).alias("data")).select(
    "data.Pclass", "data.Sex", "data.Age", 
    "data.SibSp", "data.Parch", "data.Fare", "data.Embarked", "data.Survived"
)

# MLlib modelini yükleme
model_path = "./spark-model"
model = LogisticRegressionModel.load(model_path)

feature_columns = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")

# Veriyi konsola yazdırma ve tahmin yapma
def process_batch(df, epoch_id):
    # Özellikleri vektörleştirmek için VectorAssembler kullanma
    df = assembler.transform(df)
    
    # Modelle tahmin yapma
    predictions = model.transform(df)
    df.show(truncate=False)
    # Tahminleri konsola yazdırma
    predictions.select("prediction").show(truncate=False)

    # Tahmin doğruluğunu değerlendirme
    accuracy_df = predictions.withColumn("is_correct", expr("prediction == Survived"))
    accuracy_df.select("prediction", "Survived", "is_correct").show(truncate=False)

# writeStream kullanarak her batch'i işleyecek şekilde ayarlama
query = parsed_df.writeStream \
    .foreachBatch(process_batch) \
    .start()

query.awaitTermination()