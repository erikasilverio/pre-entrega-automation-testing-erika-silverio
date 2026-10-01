import os
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def obtener_driver():
    """
    Configura e inicializa el navegador Chrome maximizado utilizando Selenium Manager.
    Evita fallos de arquitectura y compatibilidad con ChromeDriver.
    """
    opciones = webdriver.ChromeOptions()
    opciones.add_argument("--start-maximized")
    opciones.add_argument("--disable-notifications")
    
    # Selenium 4 gestiona la descarga y compatibilidad del ChromeDriver de forma automática
    servicio = Service()
    driver = webdriver.Chrome(service=servicio, options=opciones)
    return driver

def esperar_elemento(driver, localizador, valor, tiempo=10):
    """
    Espera explícita para asegurar que un elemento sea visible en el DOM antes de interactuar.
    """
    espera = WebDriverWait(driver, tiempo)
    return espera.until(EC.visibility_of_element_located((localizador, valor)))

def hacer_clic(driver, localizador, valor, tiempo=10):
    """
    Localiza un elemento en pantalla y realiza la acción de clic.
    """
    elemento = esperar_elemento(driver, localizador, valor, tiempo)
    elemento.click()

def escribir_texto(driver, localizador, valor, texto, tiempo=10):
    """
    Limpia un campo de entrada e ingresa el texto proporcionado.
    """
    campo = esperar_elemento(driver, localizador, valor, tiempo)
    campo.clear()
    campo.send_keys(texto)

def obtener_logger():
    """
    Configura la bitácora de logs para guardar la actividad en 'reports/ejecucion.log'.
    """
    os.makedirs("reports", exist_ok=True)
    
    logger = logging.getLogger("SauceDemoQA")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        manejador_archivo = logging.FileHandler("reports/ejecucion.log", mode="a", encoding="utf-8")
        formato = logging.Formatter("%(asctime)s - [%(levelname)s] - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        manejador_archivo.setFormatter(formato)
        logger.addHandler(manejador_archivo)

    return logger

def capturar_pantalla_error(driver, nombre_evidencia):
    """
    Guarda una captura de pantalla PNG en la carpeta 'reports/' cuando se detecta un fallo.
    """
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta_captura = f"reports/{nombre_evidencia}_{timestamp}.png"
    driver.save_screenshot(ruta_captura)
    return ruta_captura