import time
import pytest
from selenium.webdriver.common.by import By
from utils.helpers import (
    obtener_driver,
    esperar_elemento,
    hacer_clic,
    escribir_texto,
    obtener_logger,
    capturar_pantalla_error
)

logger = obtener_logger()

# Tiempo de pausa visual entre acciones (en segundos)
TIEMPO_ESPERA_VISUAL = 0.2

class TestSauceDemo:
    """
    Suite de pruebas automatizadas E2E para la plataforma SauceDemo.
    Cubre desde el inicio de sesión hasta la validación del carrito de compras.
    Incluye pausas visuales para facilitar el seguimiento durante la demostración.
    """

    @pytest.fixture(autouse=True)
    def setup_y_teardown(self):
        """
        Garantiza un entorno limpio abriendo el navegador antes de cada test
        y cerrándolo al finalizar la ejecución.
        """
        logger.info("Iniciando instancia de navegador Chrome...")
        self.driver = obtener_driver()
        yield
        time.sleep(TIEMPO_ESPERA_VISUAL)  # Pausa antes de cerrar el navegador
        logger.info("Cerrando sesión de navegador.")
        self.driver.quit()

    def test_01_login_exitoso(self):
        """
        Valida el ingreso correcto al sistema utilizando credenciales válidas
        y confirma la redirección hacia el catálogo principal.
        """
        try:
            logger.info("Paso 1: Ingresando a la página de login de SauceDemo")
            self.driver.get("https://www.saucedemo.com/")
            time.sleep(TIEMPO_ESPERA_VISUAL)

            logger.info("Paso 2: Completando el formulario con el usuario 'standard_user'")
            escribir_texto(self.driver, By.ID, "user-name", "standard_user")
            time.sleep(1)
            escribir_texto(self.driver, By.ID, "password", "secret_sauce")
            time.sleep(TIEMPO_ESPERA_VISUAL)
            
            logger.info("Paso 3: Enviando credenciales")
            hacer_clic(self.driver, By.ID, "login-button")
            time.sleep(TIEMPO_ESPERA_VISUAL)

            logger.info("Paso 4: Verificando ingreso a la URL del inventario")
            esperar_elemento(self.driver, By.CLASS_NAME, "title")
            
            assert "inventory.html" in self.driver.current_url, (
                f"Error en Login: Se esperaba estar en '/inventory.html', pero la URL es {self.driver.current_url}"
            )
            logger.info("✓ Test 01 - Login Exitoso: Completado correctamente.")

        except Exception as e:
            logger.error(f"Fallo detectado en test_01_login_exitoso: {str(e)}")
            capturar_pantalla_error(self.driver, "fallo_login")
            raise e

    def test_02_navegacion_y_catalogo(self):
        """
        Comprueba la carga general del inventario, la presencia del menú y la
        correcta lectura de los datos del primer producto de la lista.
        """
        try:
            logger.info("Paso 1: Iniciando sesión previa para inspeccionar catálogo")
            self.driver.get("https://www.saucedemo.com/")
            escribir_texto(self.driver, By.ID, "user-name", "standard_user")
            escribir_texto(self.driver, By.ID, "password", "secret_sauce")
            hacer_clic(self.driver, By.ID, "login-button")
            time.sleep(TIEMPO_ESPERA_VISUAL)

            logger.info("Paso 2: Validando el título general de la aplicación web")
            assert self.driver.title == "Swag Labs", "El título de la página no coincide con 'Swag Labs'"

            logger.info("Paso 3: Verificando visibilidad del menú lateral y la sección de productos")
            esperar_elemento(self.driver, By.ID, "react-burger-menu-btn")
            time.sleep(TIEMPO_ESPERA_VISUAL)
            
            logger.info("Paso 4: Leyendo la información del primer ítem en pantalla")
            nombre_producto = self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text
            precio_producto = self.driver.find_element(By.CLASS_NAME, "inventory_item_price").text
            
            logger.info(f"Producto detectado: '{nombre_producto}' | Precio: {precio_producto}")
            assert len(nombre_producto) > 0, "No se logró obtener el nombre del primer producto"
            
            logger.info("✓ Test 02 - Navegación y Catálogo: Completado correctamente.")

        except Exception as e:
            logger.error(f"Fallo detectado en test_02_navegacion_y_catalogo: {str(e)}")
            capturar_pantalla_error(self.driver, "fallo_catalogo")
            raise e

    def test_03_interaccion_carrito(self):
        """
        Simula la adición de un producto al carrito, valida que el contador de la
        insignia aumente a 1 y confirma la presencia del ítem en la pantalla del carrito.
        """
        try:
            logger.info("Paso 1: Iniciando sesión de usuario")
            self.driver.get("https://www.saucedemo.com/")
            escribir_texto(self.driver, By.ID, "user-name", "standard_user")
            escribir_texto(self.driver, By.ID, "password", "secret_sauce")
            hacer_clic(self.driver, By.ID, "login-button")
            time.sleep(TIEMPO_ESPERA_VISUAL)

            logger.info("Paso 2: Agregando el primer producto al carrito de compras")
            # Selecciona el primer botón de añadir al carrito disponible en la lista
            hacer_clic(self.driver, By.CLASS_NAME, "btn_inventory")
            time.sleep(TIEMPO_ESPERA_VISUAL)

            logger.info("Paso 3: Verificando actualización del contador en la insignia del carrito")
            insignia_carrito = esperar_elemento(self.driver, By.CLASS_NAME, "shopping_cart_badge")
            assert insignia_carrito.text == "1", f"Se esperaba 1 producto en el badge, pero figura {insignia_carrito.text}"

            logger.info("Paso 4: Navegando al detalle del carrito (/cart.html)")
            hacer_clic(self.driver, By.CLASS_NAME, "shopping_cart_link")
            time.sleep(TIEMPO_ESPERA_VISUAL)

            logger.info("Paso 5: Confirmando presencia del producto dentro de la lista de compra")
            assert "cart.html" in self.driver.current_url, "No se logró ingresar a la vista del carrito"
            
            item_en_carrito = self.driver.find_element(By.CLASS_NAME, "inventory_item_name")
            assert item_en_carrito.is_displayed(), "El producto agregado no se visualiza dentro del carrito"

            logger.info("✓ Test 03 - Interacción con Carrito: Completado correctamente.")

        except Exception as e:
            logger.error(f"Fallo detectado en test_03_interaccion_carrito: {str(e)}")
            capturar_pantalla_error(self.driver, "fallo_carrito")
            raise e