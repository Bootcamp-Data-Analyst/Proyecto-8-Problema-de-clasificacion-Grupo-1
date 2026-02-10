<p align="center">
  <img width="479" height="479" src="https://github.com/user-attachments/assets/b4cd9a50-83f2-4240-9f5d-94b59c7b64e9">
</p>


# Proyecto 8: Predicción de Satisfacción de Pasajeros de Aerolíneas

## Descripción

Este proyecto desarrolla un modelo de Machine Learning capaz de predecir si un pasajero estará satisfecho o insatisfecho con su vuelo basándose en diversos parámetros de servicio, demografía y retrasos.

Incluye una aplicación interactiva desarrollada en **Streamlit** para realizar predicciones en tiempo real y está preparado para ser desplegado mediante **Docker**.

> **Nota sobre Rutas:** El proyecto ha sido actualizado con rutas robustas (basadas en `__file__`). Esto permite ejecutar los scripts desde cualquier directorio sin fallos de "archivo no encontrado".

## Características

- **Modelo ML**: XGBoost con un 95.8% de precisión en test.
- **Overfitting controlado**: Diferencia entre Train/Test < 0.7% (Objetivo: < 5%).
- **EDA Completo**: Análisis de correlaciones, distribuciones y valores nulos.
- **App Interactiva**: Interfaz premium con Glassmorphism.
- **Contenerización**: Dockerfile listo para despliegue.

## Tecnologías

- Python (Pandas, Scikit-learn, XGBoost)
- Streamlit
- Docker
- Joblib (Serialización)

## Resultados del Modelo

- **Accuracy**: 95.81%
- **F1-Score**: 0.96
- **Overfitting**: 0.67%
- **Top Feature**: Inflight entertainment y Seat comfort.

## Instrucciones para ejecutar

1. Instalar dependencias: `pip install -r requirements.txt`
2. Entrenar el modelo (opcional): `python src/train.py`
3. Ejecutar la App: `streamlit run app/main.py`
4. Ejecutar con Docker:
   ```bash
   docker build -t airline-satisfaction .
   docker run -p 8501:8501 airline-satisfaction
   ```

## Pruebas

Ejecutar `pytest` en la raíz del proyecto.
