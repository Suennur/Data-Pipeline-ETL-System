from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# SparkSession'ın başlatılması
spark = SparkSession.builder \
    .appName("Titanic Survival Prediction") \
    .getOrCreate()

# Veri setinin yüklenmesi
df = spark.read.csv("trainDataSet.csv", header=True, inferSchema=True)

# Özelliklerin bir araya getirilmesi
assembler = VectorAssembler(inputCols=["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"], outputCol="features")
data = assembler.transform(df)

# Veri setinin eğitim ve test setlerine ayrılması
train_data, test_data = data.randomSplit([0.7, 0.3])


# Modelin oluşturulması ve eğitimi
lr = LogisticRegression(labelCol="Survived", featuresCol="features")
model = lr.fit(train_data)

# Test veri seti üzerinde tahminlerin yapılması ve değerlendirilmesi
predictions = model.transform(test_data)
evaluator = BinaryClassificationEvaluator(labelCol="Survived")
accuracy = evaluator.evaluate(predictions)
print("Model Accuracy on Test Data: ", accuracy)

#Modelin kaydedilmesi
model.save("spark-model")

# SparkSession'ın kapatılması
spark.stop()
