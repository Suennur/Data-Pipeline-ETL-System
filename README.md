# 🚀 Real-Time Data Pipeline & ETL System with Kafka and Spark

This project demonstrates a **real-time data streaming and analytics pipeline** using Apache Kafka and Apache Spark. The system is designed to process and analyze streaming data based on the Titanic dataset from Kaggle's "Machine Learning from Disaster" competition.

The goal of this project is to build a **small-scale data analytics system** capable of performing **real-time machine learning predictions** on streaming data. The machine learning model is trained using **Logistic Regression** with Spark MLlib.

---

## 🎯 Project Goals
- Build a **real-time data streaming pipeline**.
- Apply **ETL (Extract, Transform, Load)** steps on streaming data.
- Train a Logistic Regression model with PySpark MLlib.
- Perform **online machine learning predictions** in real-time using the trained model.
- Display prediction results and model accuracy on the terminal interface instantly.

---

## 🛠️ Technologies Used

| Category            | Tools                  |
|---------------------|------------------------|
| Streaming           | Apache Kafka           |
| Data Processing     | Apache Spark Streaming |
| Machine Learning    | Spark MLlib, Logistic Regression, Python |
| Data Format         | CSV                    |
| Data Preprocessing  | pandas, scikit-learn, matplotlib, seaborn |

---

## 🔄 Workflow

1. **Data Source:** Titanic dataset (CSV format)
2. **Data Preprocessing:** Missing values were imputed, categorical features were label encoded, and unnecessary columns were dropped using pandas and scikit-learn.
3. **Producer:** `kafka_producer.py` sends data row-by-row to Kafka topic.
4. **Streaming:** Apache Spark consumes data in real-time from Kafka.
5. **Data Processing:** Each incoming row is pre-processed and assembled into a DataFrame.
6. **Model Prediction:** The trained ML model makes a prediction on each row instantly.
7. **Result Display:** Predictions and model accuracy are printed to the terminal in real-time.

---

## 📊 Sample Output

![image](https://github.com/user-attachments/assets/66d53bec-4522-40dd-9a86-95c33b638d40)

---

## ⚙️ Installation and Setup

1. **Clone the repository:**
```bash
git clone https://github.com/kullaniciadi/data-pipeline-etl-system.git
cd data-pipeline-etl-system
```

---

## 🎯 Key Features
 Data preprocessing with missing value imputation, label encoding, and feature selection

Real-time data ingestion with Apache Kafka

Real-time processing with Apache Spark Streaming

Online machine learning predictions with Spark MLlib

Streaming visualization in terminal interface

---

## 🔍 Dataset
Dataset used: Titanic - Machine Learning from Disaster

---

## 🧹 Data Preprocessing Details

Data preprocessing was performed using pandas and scikit-learn:
- Missing values in the "Age" column were imputed using the mean.
- Categorical variables like "Sex" and "Embarked" were label encoded.
- Irrelevant columns such as "Cabin", "Name", "Ticket", and "PassengerId" were removed.
- Data was split into training and testing sets using an 80-20 split.

Preprocessing code is provided in the `preprocessing.ipynb` notebook.

---

## 🚀 Future Improvements

Add monitoring and visualization with Grafana and Prometheus

Dockerize the entire system for easier deployment

Integrate with a web dashboard to display live predictions

---

## 🤝 Contact
Developed by Suennur Altaş

📫 Email: suennur.altas@gmail.com

🔗 LinkedIn | GitHub
