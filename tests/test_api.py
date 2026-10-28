from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200


def test_prediction():
    data = {
        "Pregnancies": 2,
        "Glucose": 120,
        "BloodPressure": 70,
        "SkinThickness": 20,
        "Insulin": 79,
        "BMI": 25.0,
        "DiabetesPedigreeFunction": 0.5,
        "Age": 30
    }

    response = client.post("/predict", json=data)

    assert response.status_code == 200
    assert response.json()["prediction"] in [0, 1]