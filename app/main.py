import streamlit as st
import pandas as pd
import joblib
import os

# Configuración de la página
st.set_page_config(
    page_title="Airline Satisfaction Predictor",
    layout="wide"
)

# Estilo personalizado (Glassmorphism & Gradients)
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background: linear-gradient(45deg, #00b4db, #0083b0);
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    .card {
        background: rgba(255, 255, 255, 0.7);
        padding: 2rem;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Cargar el modelo
@st.cache_resource
def load_resources():
    # Obtener la ruta del directorio raíz del proyecto (un nivel arriba de 'app')
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(base_dir, "models", "airline_model.joblib")
    le_path = os.path.join(base_dir, "models", "label_encoder.joblib")
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"No se encontró el modelo en: {model_path}")
        
    model = joblib.load(model_path)
    le = joblib.load(le_path)
    return model, le

try:
    model, le = load_resources()
except Exception as e:
    st.error(f"Error al cargar el modelo: {e}")
    st.stop()

# Header
st.title("Predictor de Satisfacción del Pasajero")
st.markdown("---")

# Layout de columnas
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("Perfil del Pasajero")
    with st.container():
        gender = st.selectbox("Género", ["Female", "Male"])
        customer_type = st.selectbox("Tipo de Cliente", ["Loyal Customer", "disloyal Customer"])
        age = st.slider("Edad", 7, 85, 30)
        travel_type = st.selectbox("Tipo de Viaje", ["Personal Travel", "Business travel"])
        travel_class = st.selectbox("Clase", ["Eco", "Business", "Eco Plus"])
        distance = st.number_input("Distancia del Vuelo (km)", min_value=1, value=1000)

    st.subheader("Retrasos")
    departure_delay = st.number_input("Retraso Salida (min)", min_value=0, value=0)
    arrival_delay = st.number_input("Retraso Llegada (min)", min_value=0, value=0)

with col2:
    st.subheader("Calificación del Servicio (0-5)")
    services = {
        "Inflight wifi service": 3,
        "Departure/Arrival time convenient": 3,
        "Ease of Online booking": 3,
        "Gate location": 3,
        "Food and drink": 3,
        "Online boarding": 3,
        "Seat comfort": 3,
        "Inflight entertainment": 3,
        "On-board service": 3,
        "Leg room service": 3,
        "Baggage handling": 3,
        "Checkin service": 3,
        "Inflight service": 3,
        "Cleanliness": 3
    }
    
    ratings = {}
    # Dividir las calificaciones en dos sub-columnas para mejor UX
    s1, s2 = st.columns(2)
    keys = list(services.keys())
    for i, key in enumerate(keys):
        if i < 7:
            ratings[key] = s1.select_slider(f"{key}", options=range(6), value=3)
        else:
            ratings[key] = s2.select_slider(f"{key}", options=range(6), value=3)

# Botón de predicción
if st.button("Calcular Satisfacción"):
    # Preparar datos
    input_data = {
        "Gender": gender,
        "Customer Type": customer_type,
        "Age": age,
        "Type of Travel": travel_type,
        "Class": travel_class,
        "Flight Distance": distance,
        "Departure Delay in Minutes": departure_delay,
        "Arrival Delay in Minutes": arrival_delay,
        "Inflight service": 3 # Valor por defecto para la nueva columna
    }
    input_data.update(ratings)
    
    # Crear DataFrame con el orden correcto de columnas
    expected_cols = [
        "Gender", "Customer Type", "Age", "Type of Travel", "Class",
        "Flight Distance", "Inflight wifi service", "Departure/Arrival time convenient",
        "Ease of Online booking", "Gate location", "Food and drink",
        "Online boarding", "Seat comfort", "Inflight entertainment",
        "On-board service", "Leg room service", "Baggage handling",
        "Checkin service", "Inflight service", "Cleanliness",
        "Departure Delay in Minutes", "Arrival Delay in Minutes"
    ]
    input_df = pd.DataFrame([input_data])[expected_cols]
    
    # Predicción
    prediction_proba = model.predict_proba(input_df)[0]
    prediction = model.predict(input_df)[0]
    label = le.inverse_transform([prediction])[0]
    
    # Resultados
    st.markdown("---")
    res_col1, res_col2 = st.columns(2)
    
    with res_col1:
        if label == "satisfied":
            st.success(f"### Resultado: **Satisfecho**")
        else:
            st.error(f"### Resultado: **Insatisfecho**")
            
    with res_col2:
        st.metric("Confianza", f"{max(prediction_proba)*100:.2f}%")
        st.progress(float(max(prediction_proba)))

    # Recomendación dinámica
    if label == "dissatisfied":
        st.info("**Tip:** Los factores que más podrían mejorar la satisfacción son el servicio de WiFi y el entretenimiento a bordo.")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
