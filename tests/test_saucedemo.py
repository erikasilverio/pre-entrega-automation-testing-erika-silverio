import pytest
from selenium.webdriver.common.by import By
from utils.helpers import (
    get_driver, 
    wait_for_element, 
    wait_for_visibility, 
    take_screenshot,
    get_logger
)

class TestSauceDemo:

    def setup_method(self):
        """PRECONDICIÓN: Inicia el navegador y abre la URL objetivo antes de cada test."""
        self.logger = get_logger()
        self.logger.info("--- INICIANDO CASO DE PRUEBA ---")
        self.driver = get_driver()
        self.driver.get("https://www.saucedemo.com/")
        self.logger.info("Navegando a https://www.saucedemo.com/")

    def teardown_method(self):
        """POSTCONDICIÓN: Cierra el navegador tras finalizar cada test (Garantiza independencia)."""
        self.driver.quit()
        self.logger.info("--- FINALIZANDO CASO DE PRUEBA (Navegador cerrado) ---\n")

    def test_01_login_exitoso(self):
        """
        CONSIGNA 1: Automatización de Login
        - Credenciales: standard_user / secret_sauce
        - Espera explícita
        - Validaciones: Redirección a /inventory.html y texto 'Products' / 'Swag Labs'
        """
        try:
            self.logger.info("Ejecutando test_01_login_exitoso")
            
            # Ingreso de credenciales con esperas explícitas
            wait_for_visibility(self.driver, (By.ID, "user-name")).send_keys("standard_user")
            wait_for_visibility(self.driver, (By.ID, "password")).send_keys("secret_sauce")
            wait_for_element(self.driver, (By.ID, "login-button")).click()

            # Validación 1: Verificar redirección a la URL del inventario
            current_url = self.driver.current_url
            assert "/inventory.html" in current_url, f"Redirección fallida. URL actual: {current_url}"
            self.logger.info("Validación exitosa: Redirigido correctamente a /inventory.html")
            
            # Validación 2: Verificar título de sección 'Products'
            titulo_seccion = wait_for_visibility(self.driver, (By.CLASS_NAME, "title")).text
            assert titulo_seccion.upper() == "PRODUCTS", f"Título esperado 'PRODUCTS', se obtuvo '{titulo_seccion}'"
            self.logger.info("Validación exitosa: Encabezado 'Products' presente")

        except Exception as e:
            take_screenshot(self.driver, "fallo_test_01_login")
            self.logger.error(f"Fallo en test_01_login_exitoso: {str(e)}")
            raise e

    def test_02_navegacion_y_catalogo(self):
        """
        CONSIGNA 2: Navegación y verificación del catálogo
        - Valida el título general de la página ('Swag Labs')
        - Valida elementos clave visibles (Menú lateral, Filtro de ordenamiento)
        - Valida presencia de productos e imprime el Nombre y Precio del primero
        """
        try:
            self.logger.info("Ejecutando test_02_navegacion_y_catalogo")
            
            # Autenticación requerida para acceder al catálogo
            wait_for_visibility(self.driver, (By.ID, "user-name")).send_keys("standard_user")
            wait_for_visibility(self.driver, (By.ID, "password")).send_keys("secret_sauce")
            wait_for_element(self.driver, (By.ID, "login-button")).click()

            # 1. Validar el título principal de la ventana web
            titulo_web = self.driver.title
            assert "Swag Labs" in titulo_web, f"Título web esperado 'Swag Labs', se obtuvo '{titulo_web}'"
            self.logger.info("Validación exitosa: Título de página contiene 'Swag Labs'")

            # 2. Validar visibilidad de elementos globales de la interfaz
            menu_btn = wait_for_visibility(self.driver, (By.ID, "react-burger-menu-btn"))
            filtro = wait_for_visibility(self.driver, (By.CLASS_NAME, "product_sort_container"))
            assert menu_btn.is_displayed(), "El botón de menú lateral no está visible"
            assert filtro.is_displayed(), "El filtro de ordenamiento no está visible"
            self.logger.info("Validación exitosa: Menú lateral y Filtros presentes")

            # 3. Comprobar catálogo y listar nombre/precio del primer producto
            productos = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
            assert len(productos) > 0, "No existen productos visibles en el catálogo"

            primer_nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
            primer_precio = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
            
            self.logger.info(f"Primer producto detectado: '{primer_nombre}' - Precio: '{primer_precio}'")
            print(f"\n[CATÁLOGO] Primer producto: {primer_nombre} | Precio: {primer_precio}")

        except Exception as e:
            take_screenshot(self.driver, "fallo_test_02_catalogo")
            self.logger.error(f"Fallo en test_02_navegacion_y_catalogo: {str(e)}")
            raise e

    def test_03_interaccion_carrito(self):
        """
        CONSIGNA 3: Interacción con productos y carrito
        - Añade el primer producto disponible al carrito
        - Verifica que el contador de la insignia del carrito cambie a '1'
        - Navega a la vista del carrito
        - Comprueba que el producto añadido figure en la lista del carrito
        """
        try:
            self.logger.info("Ejecutando test_03_interaccion_carrito")
            
            # Autenticación
            wait_for_visibility(self.driver, (By.ID, "user-name")).send_keys("standard_user")
            wait_for_visibility(self.driver, (By.ID, "password")).send_keys("secret_sauce")
            wait_for_element(self.driver, (By.ID, "login-button")).click()

            # 1. Añadir el primer producto al carrito
            wait_for_element(self.driver, (By.CSS_SELECTOR, ".inventory_item button")).click()
            self.logger.info("Se hizo clic en 'Add to cart' para el primer producto")

            # 2. Verificar incremento del contador en el ícono del carrito
            badge_texto = wait_for_visibility(self.driver, (By.CLASS_NAME, "shopping_cart_badge")).text
            assert badge_texto == "1", f"Contador de carrito esperado '1', se obtuvo '{badge_texto}'"
            self.logger.info("Validación exitosa: Contador del carrito muestra '1'")

            # 3. Navegar a la pantalla del carrito
            wait_for_element(self.driver, (By.CLASS_NAME, "shopping_cart_link")).click()
            assert "/cart.html" in self.driver.current_url, "No se redirigió a /cart.html"

            # 4. Comprobar presencia del ítem agregado dentro de la lista
            items_en_carrito = self.driver.find_elements(By.CLASS_NAME, "cart_item")
            assert len(items_en_carrito) == 1, "El producto agregado no figura dentro del carrito"
            self.logger.info("Validación exitosa: Producto verificado dentro del carrito de compras")

        except Exception as e:
            take_screenshot(self.driver, "fallo_test_03_carrito")
            self.logger.error(f"Fallo en test_03_interaccion_carrito: {str(e)}")
            raise e