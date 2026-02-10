# Guia para Dummies: Proyecto de Clasificacion de Satisfaccion de Pasajeros

Esta guia te enseñara a construir una Inteligencia Artificial capaz de predecir si un pasajero de avion estara contento con su viaje. No necesitas ser un experto, solo seguir estos pasos.

---

## Antes de empezar: Tus herramientas
Para este proyecto usaremos:
1.  **VS Code (Visual Studio Code)**: Es el programa donde escribiremos nuestro codigo.
2.  **Python**: El lenguaje de programacion de la IA.
3.  **Terminal/Consola**: Donde daremos las ordenes para ejecutar el programa.

---

## Paso 1: Preparar la casa (Estructura de Carpetas)
Un proyecto de Inteligencia Artificial debe estar ordenado. Crea una carpeta llamada `proyecto_8` y dentro de ella crea estas subcarpetas:
-   `data`: Para guardar nuestro archivo de Excel (CSV).
-   `notebooks`: Para nuestros borradores y analisis.
-   `src`: Para el codigo que entrena a la IA.
-   `app`: Para el codigo de la pagina web interactiva.
-   `models`: Para guardar a la IA una vez que haya aprendido.

**¿Por que?** Porque si mezclas los datos con el codigo, el proyecto se vuelve un caos y es dificil de mantener.

---

## Paso 2: El archivo de ingredientes (`requirements.txt`)
Crea un archivo llamado `requirements.txt` en la raiz de `proyecto_8`. Escribe dentro las librerias que necesitamos:
```text
pandas
scikit-learn
xgboost
streamlit
joblib
```
**Decision**: Usamos `pandas` para leer datos, `xgboost` porque es una de las IAs mas potentes para datos tabulares, y `streamlit` para crear la web de forma facil.

---

## Paso 3: El cerebro del proyecto (`src/train.py`)
Aqui es donde la IA aprende. Crea el archivo `train.py` dentro de la carpeta `src`.

**¿Que hace este archivo?**
1.  **Lee los datos**: Usa `pandas` para cargar el archivo CSV.
2.  **Limpia**: Si faltan datos (como un retraso de vuelo vacio), la IA no puede aprender. Rellenamos esos huecos.
3.  **Entrena**: Le pasamos los datos del pasado (edad, clase, servicios) y le decimos: "Aprende que hace que estas personas esten satisfechas".
4.  **Evalua**: Guardamos un poco de datos que la IA no ha visto para preguntarle: "¿Que crees que paso aqui?". Si acierta mas del 95%, ¡es muy buena!
5.  **Guarda**: Usamos `joblib` para "congelar" a la IA en un archivo llamado `airline_model.joblib`.

---

## Paso 4: La cara al publico (`app/main.py`)
Nadie quiere ver lineas de codigo negro. Quieren una web. Crea `main.py` en la carpeta `app`.

**¿Por que Streamlit?**
Porque te permite crear una pagina web usando solo Python. Sin saber HTML o CSS complicado.
-   Creamos botones y deslizadores para que el usuario ponga sus datos.
-   Cargamos la IA "congelada" del paso anterior.
-   Cuando el usuario pulsa "Calcular", la IA hace su magia y devuelve "Satisfecho" o "Insatisfecho".

---

## Paso 5: Como ponerlo en marcha
1.  **Instala las herramientas**: Abre tu terminal en la carpeta del proyecto y escribe:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Entrena a la IA**:
    ```bash
    python src/train.py
    ```
3.  **Lanza la web**:
    ```bash
    python -m streamlit run app/main.py
    ```

---

## Decisiones Importantes explicadas para Dummies

1.  **¿Por que XGBoost?**: Hay muchas IAs (Arboles de decision, Redes Neuronales...). XGBoost es como el "coche de carreras" para datos de tablas como los de aerolineas: es rapido y muy preciso.
2.  **¿Por que dividir en Train y Test?**: Imagina que un estudiante se memoriza el examen. Si le das el mismo examen, sacara un 10, pero si le cambias una pregunta, suspendera. Dividir los datos nos permite saber si la IA "entendio" o solo "memorizo".
3.  **¿Por que el escalado de datos?**: La IA se confunde si comparas "Edad" (numeros pequeños como 20) con "Distancia de vuelo" (numeros grandes como 3000). El escalado pone todo en una escala similar para que la IA no crea que la distancia es mas importante solo por ser un numero mas grande.

---

¡Felicidades! Siguiendo estos pasos habras creado un sistema de Inteligencia Artificial completo desde cero.
