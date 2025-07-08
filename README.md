# FlowSight: Smart City Traffic Prediction Pipeline

FlowSight is a smart city traffic forecasting pipeline that simulates and predicts congestion patterns using real-time stream processing and machine learning. This project is ideal for beginners looking to explore data engineering, PySpark, Kafka, and deployment with FastAPI.

## ✨ Project Highlights

- Real-time traffic data simulation using Kafka
- Stream processing with PySpark Structured Streaming
- Parquet-based data lake (bronze layer)
- Traffic speed prediction using a trained Random Forest model
- FastAPI deployment for serving predictions

---

## ⚙️ Setup and Installation

### Prerequisites

- Python 3.10+
- Java 17 (Temurin or Oracle JDK)
- Spark 3.5+
- Hadoop (winutils.exe for Windows)
- Docker Desktop (for Kafka)
- Git

### Clone the Repository

```bash
git clone https://github.com/your-username/FlowSight.git
cd FlowSight
```

### Create a Virtual Environment

```bash
py -m venv venv
venv\Scripts\activate  # Windows
```

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Setup Java and Hadoop for PySpark (Windows users)

1. Ensure Java 17 is installed and `JAVA_HOME` is set:
   ```bash
   echo %JAVA_HOME%
   ```
2. Download [winutils.exe](https://github.com/steveloughran/winutils) for Hadoop 3.3.5
3. Create folder: `C:\hadoop\bin` and place `winutils.exe` inside
4. Add these environment variables:
   - `HADOOP_HOME=C:\hadoop`
   - Add `%HADOOP_HOME%\bin` to `PATH`

---

## 🚗 Step-by-Step Pipeline Execution

### Step 1: Start Kafka via Docker

```bash
docker-compose up -d
```

### Step 2: Simulate Traffic Data

```bash
python traffic_simulator.py
```

This generates mock sensor data (e.g., speed, road ID, timestamp) and sends it to Kafka topic `traffic`.

### Step 3: Stream to Bronze Layer

```bash
python stream_to_parquet.py
```

Consumes Kafka stream and writes Parquet files to `data/bronze/`.

### Step 4: Train the ML Model

```bash
python train_model.py
```

Trains a `RandomForestRegressor` to predict future traffic speed.

### Step 5: Inspect Features (optional)

```bash
python inspect_features.py
```

Verifies which features were used for training (used later for prediction).

### Step 6: Run the FastAPI App

```bash
uvicorn app:app --reload
```

Visit `http://127.0.0.1:8000/docs` to test the `/predict` endpoint.

---

## 📊 Sample Input to `/predict`

```json
{
  "speed_mean_3": 48.3,
  "speed_lag1": 46.7,
  "speed_next": 50.2,
  "sensor_roadA": 1,
  "sensor_roadB": 0,
  "sensor_roadC": 0
}
```

---

## 🌟 Conclusion

FlowSight demonstrates how to connect streaming systems with ML to build an end-to-end traffic prediction system. It taught me how to debug Spark, handle schema mismatches, structure data pipelines, and deploy a basic ML model using FastAPI.

### 📄 Technologies Used

- Python, Pandas, Scikit-learn
- Kafka + Docker
- PySpark Structured Streaming
- FastAPI + Uvicorn
- Parquet, winutils

---

## 🌐 Find me on LinkedIn

If you found this interesting or helpful, connect with me: [https://www.](https://www.linkedin.com/in/khushi-gangrade/)[linkedin.com/in/khushi-gangrade/](https://www.linkedin.com/in/khushi-gangrade/)

---

## 🚀 License

MIT License

---

Happy learning! 🚀

