# 🚀 Real-Time Data Pipeline & ETL System with Kafka and Spark

This project demonstrates a **real-time data streaming and analytics pipeline** using Apache Kafka and Apache Spark. The system is designed to process and analyze streaming data based on the Titanic dataset from Kaggle's "Machine Learning from Disaster" competition.

The goal of this project is to build a **small-scale data analytics system** capable of performing real-time machine learning predictions on streaming data.

---

## 🎯 Project Goals
- Build a **real-time data streaming pipeline**.
- Apply **ETL (Extract, Transform, Load)** steps on streaming data.
- Perform **online machine learning predictions** in real-time.
- Display prediction results and accuracy on the terminal interface instantly.

---

## 🛠️ Technologies Used

| Category            | Tools                  |
|---------------------|------------------------|
| Streaming           | Apache Kafka           |
| Data Processing     | Apache Spark Streaming |
| Machine Learning    | Spark MLlib, Python    |
| Data Format         | CSV                    |

---

## 📦 Project Structure

data-pipeline-etl-system/
├── kafka_producer.py # Sends data from CSV to Kafka topic
├── spark_streaming.py # Reads streaming data from Kafka, processes it, runs ML model
├── model_training.py # Trains and saves the ML model
├── dataset/
│ └── train.csv # Titanic dataset
├── requirements.txt # Python dependencies
└── README.md

---


---

## 🔄 Workflow

1. **Data Source:** Titanic dataset (CSV format)
2. **Producer:** `kafka_producer.py` sends data row-by-row to Kafka topic.
3. **Streaming:** Apache Spark consumes data in real-time from Kafka.
4. **Data Processing:** Each incoming row is pre-processed and assembled into a DataFrame.
5. **Model Prediction:** The trained ML model makes a prediction on each row instantly.
6. **Result Display:** Predictions and model accuracy are printed to the terminal in real-time.

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

🎯 Key Features
Real-time data ingestion with Apache Kafka

Real-time processing with Apache Spark Streaming

Online machine learning predictions with Spark MLlib

Streaming visualization in terminal interface

---

🔍 Dataset
Dataset used: Titanic - Machine Learning from Disaster

---

🚀 Future Improvements
Dockerize the entire system for easier deployment

Add monitoring and visualization with Grafana and Prometheus

Integrate with a web dashboard to display live predictions

---

🤝 Contact
Developed by Suennur Altaş
📫 Email: suennur.altas@gmail.com
🔗 LinkedIn | GitHub
