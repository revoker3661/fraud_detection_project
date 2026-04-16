import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    # 🏆 UPDATE: Yahan naye model ka exact naam aayega jo main.py me hai
    assert response.json() == {"status": "Online", "model": "fraud_model_xgboost_optimized"}

def test_fraud_prediction():
    # Ek dummy valid transaction (Testing logic)
    payload = {f"V{i}": 0.01 for i in range(1, 29)}
    payload["Time"] = 123.45
    payload["Amount"] = 50.0
    
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "is_fraud" in data
    assert "fraud_probability" in data
    assert data["recommendation"] in ["ALLOW", "BLOCK"]

# Command to run: pytest tests/test_api.py