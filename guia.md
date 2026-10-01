┌─────────────────────────┐
│ 1. Abrir Terminal       │
└────────────┬────────────┘
             │
┌────────────▼────────────┐
│ 2. Activar Entorno      │  -->  .\venv\Scripts\activate  (Windows)
└────────────┬────────────┘
             │
┌────────────▼────────────┐
│ 3. Instalar Paquetes    │  -->  python -m pip install -r requirements.txt
└────────────┬────────────┘
             │
┌────────────▼────────────┐
│ 4. Ejecutar Pruebas     │  -->  pytest tests/test_saucedemo.py -v --html=reports/reporte.html
└────────────┬────────────┘
             │
┌────────────▼────────────┐
│ 5. Revisar Resultados   │  -->  Abrir reports/reporte.html
└─────────────────────────┘