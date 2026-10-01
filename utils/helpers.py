import os
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración del sistema de Logging para generar el archivo de logs de ejecución
os.makedirs("reports", exist_ok=True)
logging.basicConfig(
    filename=os.path.join("reports", "ejecucion.log"),
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

def get_logger():
    """Retorna el logger configurado para registrar eventos en la prueba."""
    return logging.getLogger("SauceDemoTest")

def get_driver():
    """Inicializa la instancia de Chrome WebDriver con opciones optimizadas."""
    logger = get_logger()
    logger.info("Inicializando el navegador Chrome...")
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")        # Ventana maximizada
    options.add_argument("--disable-notifications")  # Desactivar notificaciones emergentes
    return webdriver.Chrome(options=options)

def wait_for_element(driver, locator, timeout=10):
    """Espera explícita hasta que un elemento sea interactuable (clickable)."""
    logger = get_logger()
    logger.info(f"Esperando que el elemento sea interactuable: {locator}")
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator),
        message=f"El elemento no estuvo listo para clic a tiempo: {locator}"
    )

def wait_for_visibility(driver, locator, timeout=10):
    """Espera explícita hasta que un elemento sea visible en pantalla."""
    logger = get_logger()
    logger.info(f"Esperando visibilidad del elemento: {locator}")
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator),
        message=f"El elemento no fue visible en pantalla a tiempo: {locator}"
    )

def take_screenshot(driver, name="captura_fallo"):
    """
    Guarda una captura de pantalla PNG en la carpeta /reports
    como evidencia visual en caso de fallo.
    """
    logger = get_logger()
    os.makedirs("reports", exist_ok=True)
    filepath = os.path.join("reports", f"{name}.png")
    driver.save_screenshot(filepath)
    logger.error(f"EVIDENCIA GENERADA: Captura guardada en {filepath}")
    print(f"\n[EVIDENCIA] Captura guardada en: {filepath}")
    return filepath