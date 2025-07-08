# FlowSight: Real-Time Traffic Congestion Forecasting Pipeline

FlowSight is a smart city traffic forecasting pipeline that simulates and predicts congestion patterns using real-time stream processing and machine learning. This project is ideal for beginners looking to explore end-to-end data engineering, model training, deployment, and interactive visualization.

## ✨ Project Highlights

- Real-time traffic data simulation using Kafka
- Stream processing with PySpark Structured Streaming or pure‑Python consumer
- Parquet-based data lake (bronze layer)
- Traffic speed prediction with a Random Forest model
- REST API for live predictions via FastAPI
- Interactive Streamlit dashboard with map visualization

---

## ⚙️ Setup and Installation

### Prerequisites

- Python 3.10+
- Java 17 (Temurin or Oracle JDK)
- (Optional) Apache Spark 3.5+ for streaming
- (Windows) Hadoop winutils.exe for native IO
- Docker Desktop (for Kafka & Zookeeper)
- Git

### Clone the Repository

```bash
git clone https://github.com/your-username/flowsight.git
cd flowsight
```

### Create and Activate Virtual Environment

```bash
py -m venv venv
venv\Scripts\activate       # Windows
# or
source venv/bin/activate    # macOS/Linux
```

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Configure Java & Hadoop on Windows

1. Verify Java 17 and `JAVA_HOME`:
   ```powershell
echo %JAVA_HOME%
```
2. Download [winutils.exe](https://github.com/steveloughran/winutils) for Hadoop 3.3.5.
3. Create `C:\hadoop\bin`, place `winutils.exe` inside.
4. Set environment variables:
   - `HADOOP_HOME=C:\hadoop`
   - Add `%HADOOP_HOME%\bin` to your `PATH`

---

## 🚗 Pipeline Execution

### 1. Start Kafka & Zookeeper

```bash
docker compose up -d
docker ps
```

This exposes Kafka on `localhost:9092` and ZK on `localhost:2181`.

### 2. Simulate Traffic Data

```bash
python traffic_simulator.py
```

Produces mock sensor messages to Kafka topic `traffic`.

### 3. Stream to Bronze Layer

**Linux/macOS:**
```bash
python stream_to_parquet.py
```

**Windows Windows-native IO issues?** Use pure‑Python:
```bash
python consumer_to_parquet.py
```

Parquet files land in `data/bronze/` or `data/bronze_py/`.

### 4. Train the ML Model

```bash
python train_model.py
```

Trains a `RandomForestRegressor` and saves the model to `model.joblib`.

### 5. Inspect Features (optional)

```bash
python inspect_features.py
```

Displays the feature names expected by the saved model.

### 6. Launch the FastAPI Service

```bash
python -m uvicorn app:app --reload
```

Browse <http://127.0.0.1:8000/docs> to test the `/predict` endpoint.

---

## 📊 Sample `/predict` Usage

**Request**
```json
{
  "sensor": "roadA",
  "speed": 48.3,
  "timestamp": 1627810200
}
```

**Response**
```json
{
  "predicted_speed_next": 50.1
}
```

---

## 🌐 Interactive Dashboard

You can start the dashboard UI as follows:

```powershell
# If the streamlit.exe launcher stub is broken, bypass it with:
python -m streamlit run dashboard.py
# Or if your stub is working, simply run:
streamlit run dashboard.py
```

This will open the dashboard at <http://localhost:8501>. Use the sidebar to pick a sensor, enter speed, and view predicted congestion on a map.

---

## 🌟 Conclusion

FlowSight ties together:

- **Streaming ingestion** (Kafka)
- **Data lake** (Parquet)
- **ML training** (scikit‑learn)
- **API serving** (FastAPI)
- **Visualization** (Streamlit & Pydeck)

Key learning points:

- Handling Spark on Windows vs pure‑Python fallback
- Avoiding feature/target mismatches in production models
- Containerizing Kafka & ZK for local development
- Deploying fast, interactive dashboards

### 📄 Technologies Used

Python · Pandas · scikit‑learn · Kafka · Docker · PySpark · FastAPI · Uvicorn · Streamlit · Pydeck · Parquet · Hadoop winutils

---

## 🚀 License

MIT License

---

Happy coding! 🚦✨

