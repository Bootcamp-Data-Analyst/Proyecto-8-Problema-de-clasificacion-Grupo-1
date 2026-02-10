import pytest
import pandas as pd
import joblib
import os

def test_model_prediction():
    # Cargar modelo desde la ruta absoluta
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(base_dir, "models", "airline_model.joblib")
    assert os.path.exists(model_path), f"El modelo no existe en: {model_path}"
    
    model = joblib.load(model_path)
    
    test_data = {
        "Gender": "Female",
        "Customer Type": "Loyal Customer",
        "Age": 40,
        "Type of Travel": "Business travel",
        "Class": "Business",
        "Flight Distance": 1500,
        "Inflight wifi service": 5,
        "Departure/Arrival time convenient": 5,
        "Ease of Online booking": 5,
        "Gate location": 5,
        "Food and drink": 5,
        "Online boarding": 5,
        "Seat comfort": 5,
        "Inflight entertainment": 5,
        "On-board service": 5,
        "Leg room service": 5,
        "Baggage handling": 5,
        "Checkin service": 5,
        "Inflight service": 5,
        "Cleanliness": 5,
        "Departure Delay in Minutes": 0,
        "Arrival Delay in Minutes": 0
    }
    
    expected_cols = [
        "Gender", "Customer Type", "Age", "Type of Travel", "Class",
        "Flight Distance", "Inflight wifi service", "Departure/Arrival time convenient",
        "Ease of Online booking", "Gate location", "Food and drink",
        "Online boarding", "Seat comfort", "Inflight entertainment",
        "On-board service", "Leg room service", "Baggage handling",
        "Checkin service", "Inflight service", "Cleanliness",
        "Departure Delay in Minutes", "Arrival Delay in Minutes"
    ]
    
    input_df = pd.DataFrame([test_data])[expected_cols]
    
    prediction = model.predict(input_df)
    
    # Debería devolver 0 o 1
    assert prediction[0] in [0, 1]
