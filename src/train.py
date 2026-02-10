import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Rutas relativas al archivo
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, "data", "airline_passenger_satisfaction.csv")

# 1. Carga de datos
df = pd.read_csv(data_path)

# Eliminar columna innecesaria de índice si existe
if 'Unnamed: 0' in df.columns:
    df = df.drop('Unnamed: 0', axis=1)
if 'id' in df.columns:
    df = df.drop('id', axis=1)

# 2. Preprocesamiento básico
# Imputar Arrival Delay con el valor de Departure Delay si es nulo (suelen estar correlacionados)
df['Arrival Delay in Minutes'] = df['Arrival Delay in Minutes'].fillna(df['Departure Delay in Minutes'])

# Separar características y objetivo
X = df.drop('satisfaction', axis=1)
y = df['satisfaction']

# Codificar target (satisfied=1, dissatisfied=0)
le = LabelEncoder()
y = le.fit_transform(y)

# Identificar columnas
categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()

# 3. Construcción del Pipeline
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ]
)

# Definir el modelo
model = XGBClassifier(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=6,
    random_state=42,
    use_label_encoder=False,
    eval_metric='logloss'
)

clf = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', model)
])

# 4. División Train/Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 5. Entrenamiento
print("Entrenando el modelo...")
clf.fit(X_train, y_train)

# 6. Evaluación de Overfitting
train_acc = clf.score(X_train, y_train)
test_acc = clf.score(X_test, y_test)
overfitting = (train_acc - test_acc) * 100

print(f"\n--- Métricas de Rendimiento ---")
print(f"Accuracy Entrenamiento: {train_acc:.4f}")
print(f"Accuracy Test: {test_acc:.4f}")
print(f"Diferencia (Overfitting): {overfitting:.2f}%")

if overfitting < 5:
    print("El overfitting es inferior al 5%.")
else:
    print("Atención! El overfitting es superior al 5%.")

# 7. Informe de Clasificación
y_pred = clf.predict(X_test)
print("\n--- Informe de Clasificación ---")
print(classification_report(y_test, y_pred, target_names=le.classes_))

# 8. Importancia de Características (Feature Importance)
# Necesitamos acceder al modelo dentro del pipeline
feature_names = (numerical_cols + 
                 clf.named_steps['preprocessor']
                 .named_transformers_['cat']
                 .named_steps['onehot']
                 .get_feature_names_out(categorical_cols).tolist())

importances = clf.named_steps['classifier'].feature_importances_
feat_imp = pd.Series(importances, index=feature_names).sort_values(ascending=False).head(15)

plt.figure(figsize=(10, 6))
feat_imp.plot(kind='barh', color='teal')
plt.title('Top 15 Características más Importantes')
plt.gca().invert_yaxis()
# 8. Importancia de Características (Feature Importance)
# ... (código previo) ...
plt.tight_layout()
plots_dir = os.path.join(base_dir, "plots")
if not os.path.exists(plots_dir): os.makedirs(plots_dir)
plt.savefig(os.path.join(plots_dir, "feature_importance.png"))
print(f"Grafico guardado: {os.path.join(plots_dir, 'feature_importance.png')}")

# 9. Guardar modelo y transformadores
models_dir = os.path.join(base_dir, "models")
if not os.path.exists(models_dir): os.makedirs(models_dir)
joblib.dump(clf, os.path.join(models_dir, "airline_model.joblib"))
joblib.dump(le, os.path.join(models_dir, "label_encoder.joblib"))
print(f"\nModelo guardado en {os.path.join(models_dir, 'airline_model.joblib')}")
