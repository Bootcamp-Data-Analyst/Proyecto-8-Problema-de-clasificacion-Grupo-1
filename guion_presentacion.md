# Guion de Presentación - Proyecto 8

Este documento sirve como guía para las dos presentaciones requeridas: la de negocio y la técnica.

---

## PARTE 1: Presentación para Negocio (Vision Ejecutiva)
*Sugerencia: Usar Canva/Prezi con los gráficos de la carpeta `plots/`*

### 1. El Problema (Diapositiva 1-2)
"En el competitivo sector aéreo, retener a un cliente es 5 veces más barato que conseguir uno nuevo. ¿Sabemos realmente por qué nuestros clientes se van insatisfechos?"

### 2. La Solución IA (Diapositiva 3)
"Hemos desarrollado una herramienta de predicción con un 96% de acierto que nos permite identificar al pasajero descontento incluso antes de que baje del avión."

### 3. Hallazgos Clave (Diapositiva 4-5)
- Mostrar gráfico `satisfaction_by_class.png`.
- "Hemos descubierto que el entretenimiento a bordo es el factor nº1 de satisfacción, por encima incluso de la puntualidad."

### 4. Demo de la Aplicación (Diapositiva 6)
- Mostrar la interfaz de Streamlit.
- "Cualquier agente de fidelización puede usar esta herramienta para simular escenarios y mejorar el servicio."

---

## PARTE 2: Presentación Técnica (Vision de Desarrollo)

### 1. El Stack Tecnológico
- "Hemos utilizado Python como lenguaje base, con Pandas para la manipulación y XGBoost para el cerebro de la IA."

### 2. Pipeline de Datos
- "No solo creamos un modelo, creamos un flujo: Limpieza automática -> Imputación de nulos -> Escalado -> Predicción."
- Explicar por qué se eliminaron los IDs y cómo se trataron los nulos en `Arrival Delay`.

### 3. Rendimiento y Robustez
- "Uno de los mayores retos fue el overfitting. Logramos reducirlo a un impresionante 0.6%, garantizando que el modelo funcionará con datos reales de nuevos pasajeros."
- Mostrar métricas: 96.5% Precision.

### 4. Despliegue (Docker)
- "La solución está contenerizada en Docker. Esto significa que puede desplegarse en AWS, Azure o cualquier servidor en minutos sin errores de compatibilidad."

### 5. Futuras Mejoras
- "Integración de una base de datos SQL para registrar las predicciones y monitorear el 'Data Drift' en tiempo real."
