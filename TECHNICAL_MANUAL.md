# Manual Técnico del Proyecto: Aplicación de Preguntas de Matemáticas by Crituras ágiles

Este manual técnico proporciona una descripción detallada del proyecto que implementa una aplicación de preguntas de matemáticas utilizando el patrón de arquitectura MVC (Modelo-Vista-Controlador) en Python. Este proyecto está diseñado para permitir a los usuarios responder preguntas matemáticas de diferentes tipos y niveles de dificultad.

## Tabla de Contenidos

- [Estructura del Proyecto](#estructura-del-proyecto)
- [Arquitectura MVC](#arquitectura-mvc)
- [Descripción de los Componentes](#descripción-de-los-componentes)
  - [Modelo (`MathModel`)](#modelo-mathmodel)
  - [Vista (`MathView`)](#vista-mathview)
  - [Controlador (`MathController`)](#controlador-mathcontroller)
  - [Archivo Principal (`main.py`)](#archivo-principal-mainpy)
- [Funcionamiento del Programa](#funcionamiento-del-programa)
- [Ejecución y Pruebas](#ejecución-y-pruebas)
- [Cómo Contribuir](#cómo-contribuir)

## Estructura del Proyecto

El proyecto está organizado en dos directorios principales:

1. **`code/`**: Contiene el código fuente de la aplicación.
2. **`test/`**: Contiene los archivos de prueba para cada módulo.

### Estructura del Directorio `code/`

```plaintext
code/
│
├── controller.py
├── model.py
├── view.py
└── main.py
```

## Arquitectura MVC

El patrón de diseño MVC (Modelo-Vista-Controlador) se ha utilizado para separar las responsabilidades y mejorar la organización y mantenibilidad del código. La arquitectura se distribuye de la siguiente manera:

- **Modelo (`MathModel`)**: Encapsula la lógica de negocio y las reglas de la aplicación. Se encarga de la generación de preguntas matemáticas y respuestas correctas. 
- **Vista (`MathView`)**: Se encarga de la interacción con el usuario. Maneja la presentación de preguntas y la captura de respuestas, así como la visualización de resultados.
- **Controlador (`MathController`)**: Coordina la interacción entre el modelo y la vista. Gestiona el flujo de datos y la lógica del juego, interactuando con el modelo para obtener datos y con la vista para mostrar información.

## Descripción de los Componentes

### Modelo (`MathModel`)

**Ubicación**: `code/model.py`

El modelo (`MathModel`) es responsable de la lógica de generación de preguntas matemáticas. Contiene métodos para generar preguntas según el nivel educativo seleccionado por el usuario. La separación en este archivo permite encapsular toda la lógica de negocio en un solo lugar.

#### Métodos Clave:

- `generate_addition_subtraction_question()`: Genera preguntas de suma o resta. Selecciona aleatoriamente una operación y asegura que el resultado de la resta no sea negativo.
- `generate_multiplication_question()`: Genera preguntas de multiplicación. La dificultad de los números depende del nivel educativo.
- `generate_division_question()`: Genera preguntas de división exacta. Se asegura de que la división sea exacta para evitar resultados fraccionarios.

**Justificación**: La lógica de generación de preguntas se mantiene en el modelo para que el controlador y la vista no se mezclen con la lógica de negocio. Esto facilita la modificación o extensión de la lógica de preguntas sin afectar otras partes del código.

### Vista (`MathView`)

**Ubicación**: `code/view.py`

La vista (`MathView`) maneja la interacción con el usuario. Es responsable de mostrar preguntas, capturar respuestas y presentar los resultados. Esta separación permite que la vista se enfoque únicamente en cómo se presenta la información al usuario, sin preocuparse por la lógica detrás de ella.

#### Métodos Clave:

- `get_level()`: Solicita al usuario que seleccione su nivel educativo, lo que determina la dificultad de las preguntas.
- `get_total_questions()`: Solicita la cantidad de preguntas que el usuario desea responder.
- `show_question(question)`: Muestra una pregunta y captura la respuesta del usuario.
- `show_result(is_correct, correct_answer)`: Informa al usuario si su respuesta es correcta o incorrecta.
- `show_final_report(total_questions, correct_count, total_time)`: Muestra un reporte final con los resultados del juego, incluyendo el porcentaje de aciertos y el tiempo total.

**Justificación**: La vista se encarga de la presentación y captura de datos del usuario. Mantener esta funcionalidad separada del controlador y el modelo permite modificar o mejorar la interfaz sin alterar la lógica del juego.

### Controlador (`MathController`)

**Ubicación**: `code/controller.py`

El controlador (`MathController`) es responsable de coordinar las interacciones entre el modelo y la vista. Ejecuta el ciclo principal del programa, gestiona la generación de preguntas, la captura de respuestas y la presentación de resultados.

#### Métodos Clave:

- `__init__()`: Inicializa la vista y configura el entorno necesario para el controlador.
- `run()`: Ejecuta el ciclo principal del juego. Utiliza el modelo para obtener preguntas y la vista para mostrar preguntas y resultados. También calcula el tiempo total y muestra un reporte final.

**Justificación**: El controlador actúa como el intermediario entre el modelo y la vista. Esto asegura que la lógica de juego y la coordinación de datos se mantengan separadas de la lógica de presentación y generación de preguntas.

### Archivo Principal (`main.py`)

**Ubicación**: `code/main.py`

Este archivo es el punto de entrada del programa. Inicializa el controlador y gestiona el flujo de ejecución del juego, permitiendo al usuario jugar múltiples veces si lo desea.

#### Funcionalidad:

- Inicializa un bucle que crea una instancia del controlador y ejecuta el ciclo del juego.
- Pregunta al usuario si desea jugar otra vez después de finalizar una ronda.

**Justificación**: Mantener el punto de entrada separado del resto del código permite que el archivo principal se enfoque únicamente en la gestión del flujo de ejecución, mientras que el controlador y la vista manejan la lógica del juego.

## Funcionamiento del Programa

1. **Inicialización**: Al ejecutar el programa, `main.py` inicializa el controlador (`MathController`).
2. **Selección del Nivel y Cantidad de Preguntas**: La vista (`MathView`) solicita al usuario que seleccione el nivel educativo y la cantidad de preguntas a responder.
3. **Generación y Presentación de Preguntas**: El controlador utiliza el modelo (`MathModel`) para generar preguntas según el nivel seleccionado y las presenta al usuario a través de la vista.
4. **Captura y Evaluación de Respuestas**: El controlador captura las respuestas del usuario, las evalúa y presenta los resultados a través de la vista.
5. **Reporte Final**: Al finalizar el número de preguntas, la vista muestra un reporte final con los resultados del juego.

## Ejecución y Pruebas

Para ejecutar el programa, navega al directorio `code/` y ejecuta el archivo `main.py`:

```bash
python main.py
```

## Pruebas

Las pruebas se encuentran en el directorio tests/. Estas pruebas están diseñadas para verificar el correcto funcionamiento de los módulos model.py, view.py y controller.py. Utilizan el framework de pruebas unittest para garantizar que cada componente del sistema funcione según lo esperado.

### Estructura del Directorio `tests/`

```plaintext
tests/
│
├── __init__.py
├── test_controller.py
├── test_model.py
└── test_view.py
```


Para ejecutar las pruebas, navega al directorio test/ y ejecuta el siguiente comando:

```bash
python -m unittest discover
```

Este comando buscará y ejecutará todos los archivos de prueba en el directorio test/ que comiencen con test_. Asegúrate de que todas las pruebas pasen para confirmar que no se han introducido errores en el código.
Cómo Contribuir

Si deseas contribuir a este proyecto, sigue estos pasos:

- Fork del Repositorio: Realiza un fork del repositorio original desde GitHub para crear tu propia copia del proyecto.

- Crea una Rama: Crea una nueva rama en tu repositorio fork para tus cambios. Esto ayuda a mantener tu trabajo organizado y separado del código principal.

    ```bash
       git checkout -b nombre-de-tu-rama
    ```

- Realiza Cambios: Implementa tus cambios en la nueva rama que has creado. Asegúrate de seguir las convenciones de codificación del proyecto y realiza pruebas para verificar que tus cambios no introduzcan errores.

- Pruebas: Asegúrate de que todas las pruebas existentes pasen y añade nuevas pruebas si has realizado cambios significativos en la lógica del código.

- Commit y Push: Realiza un commit de tus cambios y envíalos a tu repositorio fork en GitHub.

    ```bash
    git add .
    git commit -m "Descripción clara de tus cambios"
    git push origin nombre-de-tu-rama
    ```

- Pull Request: Envía un pull request desde tu rama en el repositorio fork hacia el repositorio original. Proporciona una descripción detallada de tus cambios y la razón de los mismos para que los mantenedores del proyecto puedan revisarlos y fusionarlos.

¡Gracias por tu interés en contribuir! Apreciamos cualquier mejora que puedas aportar al proyecto.