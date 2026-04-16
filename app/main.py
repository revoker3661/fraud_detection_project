from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .model_utils import FraudModel

app = FastAPI(title="Fraud Detection Production API")

# Model initialize hoga (Make sure model_utils.py mein naya filename daala ho)
model_service = FraudModel()

# Request Validation Schema (Exactly matching 30 features of your input JSON)
class Transaction(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

@app.get("/")
def home():
    # API status mein naye model ka naam update kar diya
    return {"status": "Online", "model": "fraud_model_xgboost_optimized"}

@app.post("/predict")
def predict(tx: Transaction):
    try:
        # Pydantic model ko dict me convert karke prediction logic ko dena
        prob = model_service.predict(tx.dict())
        
        # Business Threshold (Optuna se nikala hua optimal threshold)
        threshold = 0.9421
        is_fraud = bool(prob >= threshold)
        
        return {
            "is_fraud": is_fraud,
            "fraud_probability": round(float(prob), 4),
            "recommendation": "BLOCK" if is_fraud else "ALLOW"
        }
    except Exception as e:
        # Detail error log for debugging
        raise HTTPException(status_code=500, detail=str(e))