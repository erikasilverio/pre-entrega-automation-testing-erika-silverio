# Pre-Entrega Automation Testing - Erika Silverio

Proyecto de automatización de pruebas End-to-End (E2E) desarrollado para la plataforma SauceDemo (www.saucedemo.com). El objetivo principal es validar los flujos fundamentales de navegación, autenticación de usuario y gestión del carrito de compras.

---

##  Tecnologías Requeridas
* **Lenguaje principal:** Python 3.14
* **Herramienta de automatización:** Selenium WebDriver (Selenium 4 con Selenium Manager)
* **Framework de pruebas:** Pytest
* **Generación de reportes:** Pytest-HTML
* **Control de versiones:** Git y GitHub

---

##  Pasos para Instalación y Configuración

1. **Clonar el repositorio:**
   git clone https://github.com/erikasilverio/pre-entrega-automation-testing-erika-silverio.git
   cd pre-entrega-automation-testing-erika-silverio

2. **Crear y activar el entorno virtual:**
   * **En Windows (PowerShell):**
     python -m venv venv
     .\venv\Scripts\activate

   * **En Mac / Linux:**
     python3 -m venv venv
     source venv/bin/activate

3. **Instalar dependencias necesarias:**
   pip install pytest selenium pytest-html

---

##  Ejecución de Pruebas

Para correr toda la suite de pruebas y generar automáticamente el reporte en formato HTML, ejecuta el siguiente comando en la terminal:

python -m pytest tests/test_saucedemo.py -v --html=reports/reporte.html --self-contained-html

---

##  Evidencias de Ejecución

* **Reporte HTML:** Se genera de forma automática en la carpeta `reports/reporte.html` tras finalizar la ejecución.
* **Logs de ejecución:** Registro detallado de cada paso guardado en `reports/ejecucion.log`.
* **Capturas de pantalla:** En caso de producirse un error durante los tests, el sistema guardará automáticamente una evidencia en imagen dentro de la carpeta `reports/`.

* *Erika Silverio*
