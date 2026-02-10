# Informe Técnico de Rendimiento del Modelo - Proyecto 8

## 1. Resumen Ejecutivo
El objetivo de este proyecto fue desarrollar un modelo de clasificación capaz de predecir la satisfacción de los pasajeros de una aerolíneabasándose en 22 parámetros de servicio y demográficos. El modelo final, basado en el algoritmo **XGBoost**, demuestra una capacidad predictiva excepcional con una precisión superior al 96%.

## 2. Análisis del Dataset y Preprocesamiento
El dataset original cuenta con 103,904 registros.
- **Limpieza**: Se trataron 310 valores nulos en la variable `Arrival Delay` imputando los valores de `Departure Delay`.
- **Ingeniería de Características**: Se eliminaron los identificadores únicos (`id`, `Unnamed: 0`) para evitar el filtrado de datos (data leakage).
- **Transformación**: Se aplicó *OneHotEncoding* a variables categóricas y *StandardScaler* a las numéricas mediante un Pipeline robusto.

## 3. Arquitectura del Modelo
Se seleccionó **XGBoost (Extreme Gradient Boosting)** por su alta eficiencia en datos tabulares.
- **Parámetros**: `n_estimators=200`, `learning_rate=0.1`, `max_depth=6`.
- **Validación**: División 80/20 con estratificación para mantener la proporción de clases.

## 4. Métricas de Rendimiento
El rendimiento del modelo se evaluó en un conjunto de prueba totalmente independiente (test set):

| Métrica | Valor |
|---------|-------|
| **Accuracy (Exactitud)** | 96.51% |
| **F1-Score (Promedio)** | 0.96 |
| **Precisión (Satisfied)** | 0.97 |
| **Recall (Satisfied)** | 0.95 |

### Control de Overfitting
- **Accuracy Entrenamiento**: 97.11%
- **Accuracy Test**: 96.51%
- **Diferencia**: **0.60%** (Objetivo: < 5%).
- *Conclusión*: El modelo generaliza perfectamente y no ha memorizado los datos de entrenamiento.

## 5. Análisis de Importancia de Características
Basándonos en el gráfico de importancia (disponible en `plots/feature_importance.png`), los factores que más influyen en la satisfacción son:
1. **Inflight entertainment** (Entretenimiento a bordo).
2. **Seat comfort** (Comodidad del asiento).
3. **Ease of Online booking** (Facilidad de reserva online).

## 6. Conclusiones y Recomendaciones
El modelo es altamente fiable para su puesta en producción. Se recomienda a la aerolínea priorizar la mejora de los sistemas de entretenimiento y la comodidad de los asientos, ya que son los disparadores principales de una experiencia positiva para el pasajero.
