from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# ─── 1) Define the input schema ─────────────────────────────────
class TrafficRecord(BaseModel):
    sensor: str             # e.g., "roadA"
    speed: float            # the current speed reading
    timestamp: int          # UNIX seconds

# ─── 2) Load the trained model ───────────────────────────────────
model = joblib.load("model.joblib")

# We need to recreate the same features you trained on
SENSOR_COLUMNS = [col for col in model.feature_names_in_ if col.startswith("sensor_")]

app = FastAPI(title="CityPulse Congestion Predictor")

# ─── 3) Health check endpoint ───────────────────────────────────
@app.get("/ping")
def ping():
    return {"ping": "pong"}

# ─── 4) Prediction endpoint ─────────────────────────────────────
@app.post("/predict")
def predict(record: TrafficRecord):
    try:
        df = pd.DataFrame([record.dict()])
        df["speed_mean_3"] = df["speed"]
        df["speed_lag1"]   = df["speed"]

        # one-hot encode each sensor
        df["sensor_roadA"] = 1 if record.sensor == "roadA" else 0
        df["sensor_roadB"] = 1 if record.sensor == "roadB" else 0
        df["sensor_roadC"] = 1 if record.sensor == "roadC" else 0

        FEATURE_NAMES = [
            "speed_mean_3",
            "speed_lag1",
            "sensor_roadA",
            "sensor_roadB",
            "sensor_roadC",
        ]
        X = df[FEATURE_NAMES]

        pred = model.predict(X)[0]
        return {"predicted_speed_next": float(pred)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
# ─── 5) Run with: uvicorn app:app --reload ───────────────────────
