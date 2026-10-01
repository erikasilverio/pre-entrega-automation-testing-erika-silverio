# Pre-Entrega: Automatización Web de SauceDemo

**Estudiante:** Erika Silverio  
**Curso:** Automation Testing con Python y Selenium  

Este proyecto contiene la automatización de pruebas de extremo a extremo (E2E) sobre la plataforma de demostración [SauceDemo](https://www.saucedemo.com/), cumpliendo con las consignas solicitadas en la Pre-Entrega.

---

## 🛠️ Tecnologías Utilizadas

* **Python 3.10+**: Lenguaje de programación principal.
* **Selenium WebDriver (v4.21.0)**: Herramienta de automatización del navegador web.
* **Pytest (v8.2.0)**: Framework de pruebas unitarias y de integración.
* **Pytest-HTML (v4.1.1)**: Generador del reporte gráfico interactivo en formato HTML.
* **Git & GitHub**: Control de versiones.

---


¿Qué automatiza este proyecto?

La suite de pruebas está dividida en 3 casos de prueba independientes y automatizados:

1. **`test_01_login_exitoso`**:
   * **Objetivo:** Validar la autenticación de usuarios.
   * **Pasos:** Ingrese credenciales válidas (`standard_user` / `secret_sauce`) usando esperas explícitas.
   * **Verificación:** Confirma la redirección a `/inventory.html` y la presencia del título de sección `PRODUCTS`.

2. **`test_02_navegacion_y_catalogo`**:
   * **Objetivo:** Comprobar la integridad visual y funcional del catálogo.
   * **Pasos:** Inicia sesión y valida elementos clave del sitio.
   * **Verificación:** Valida el título principal de la ventana (`Swag Labs`), confirma la visibilidad del menú lateral y filtro de productos, e imprime en la consola de ejecución el nombre y precio del primer producto.

3. **`test_03_interaccion_carrito`**:
   * **Objetivo:** Probar la adición de productos al carrito de compras.
   * **Pasos:** Agrega el primer producto disponible y navega hacia la vista del carrito.
   * **Verificación:** Valida que el contador del icono del carrito cambie a `1` y confirma que el producto figure listado dentro de `/cart.html`.

---
1. Abrir Terminal       
2. Ejecutar Pruebas -->  pytest tests/test_saucedemo.py -v --html=reports/reporte.html
3. Revisar Resultados -->  Abrir reports/reporte.html


--------------


