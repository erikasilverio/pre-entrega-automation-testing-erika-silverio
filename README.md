Proyecto de Automatización de Pruebas - SauceDemo

¡Hola! Te doy la bienvenida a mi repositorio de la Pre-Entrega del curso de Automation Testing.

En este proyecto desarrollé una suite de pruebas automatizadas End-to-End (E2E) para evaluar el funcionamiento de la tienda virtual SauceDemo. El objetivo principal es verificar que los flujos básicos y críticos de la plataforma funcionen sin problemas, desde el acceso con credenciales hasta la revisión de productos en el carrito de compras.

Herramientas y Tecnologías

Para construir esta solución elegí un stack sencillo pero potente dentro del ecosistema de testing con Python:

Python 3.14+: Lenguaje base para escribir la lógica de automatización.

Selenium WebDriver (v4): Utilizado para controlar las interacciones con el navegador de manera dinámica.

Pytest: Framework principal para estructurar, organizar y ejecutar los casos de prueba.

pytest-html: Extensión para generar reportes visuales de la ejecución en formato HTML.

Git & GitHub: Control de versiones y alojamiento del proyecto.

¿Cómo está organizado el proyecto?

Estructuré el código separando la lógica de pruebas de las funciones auxiliares para mantener todo ordenado, mantenible y fácil de escalar:

pre-entrega-automation-testing-erika-silverio/
│
├── tests/
│   └── test_saucedemo.py       # Suite principal de pruebas (Login, Catálogo, Carrito)
│
├── utils/
│   ├── __init__.py             # Indica a Python que la carpeta es un paquete
│   └── helpers.py              # Funciones auxiliares (esperas explícitas, logs, navegador)
│
├── reports/
│   ├── reporte.html            # Reporte visual generado tras correr las pruebas
│   └── ejecucion.log           # Historial de eventos guardados paso a paso
│
├── pytest.ini                  # Archivo de configuración global de Pytest
├── requirements.txt            # Lista de dependencias del entorno
└── README.md                   # Documentación general del repositorio


Casos de Prueba Automatizados

La suite cubre 3 flujos clave de la plataforma:

test_01_login_exitoso:

Navega a la pantalla de inicio de sesión.

Ingresa las credenciales válidas (standard_user / secret_sauce).

Valida que el sistema permita el ingreso y redirija a la página de inventario (/inventory.html).

test_02_navegacion_y_catalogo:

Inicia sesión y verifica que el título de la página sea "Swag Labs".

Confirma que el menú lateral y la grilla de productos estén presentes.

Lee e imprime en consola los datos (nombre y precio) del primer producto visible.

test_03_interaccion_carrito:

Añade el primer producto de la lista al carrito de compras.

Verifica que la insignia (badge) del carrito actualice su contador a "1".

Entra a la vista del carrito (/cart.html) y confirma que el producto seleccionado se encuentre ahí.

¿Cómo ejecutar las pruebas en tu máquina?

Sigue estos sencillos pasos para clonar el proyecto y correr las pruebas en tu entorno local:

1. Clonar el repositorio

Abre tu terminal y ejecuta:

git clone https://github.com/erikasilverio/pre-entrega-automation-testing-erika-silverio.git
cd pre-entrega-automation-testing-erika-silverio


2. Crear y activar un entorno virtual (Recomendado)

En Windows:

python -m venv venv
.\venv\Scripts\activate


En Mac/Linux:

python3 -m venv venv
source venv/bin/activate


3. Instalar las dependencias

pip install pytest selenium pytest-html


4. Ejecutar la suite de pruebas

Puedes lanzar las pruebas y generar el reporte HTML en la carpeta reports/ corriendo un solo comando:

python -m pytest tests/test_saucedemo.py -v --html=reports/reporte.html --self-contained-html


Reportes y Manejo de Evidencias

Reporte HTML: Una vez terminada la ejecución, puedes abrir el archivo reports/reporte.html en cualquier navegador para ver el resultado detallado de cada test.

Logs de ejecución: Todas las acciones realizadas quedan registradas cronológicamente en el archivo reports/ejecucion.log.

Capturas de pantalla: Si algún test llega a fallar durante la ejecución, el script tomará automáticamente una captura en formato .png y la guardará dentro de la carpeta reports/ para facilitar la investigación de errores.

Desarrollado por Erika Silverio.
