#Victor Arriagada - Api Nasa
import os
import requests
import sys
from dotenv import load_dotenv 
load_dotenv() 

API_KEY = os.getenv('API_KEY_PROYECTO')

if not API_KEY:
    print("Error Crítico: La variable de entorno API_KEY_PROYECTO no está configurada.")
    sys.exit(1)

URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

try:
    response = requests.get(URL, timeout=5)
    
    # Error 1: Clave inválida o límite de peticiones (401/403)
    if response.status_code in [401, 403]:
        print("Error de Autenticación: Clave de API inválida o límite de uso alcanzado.")
        sys.exit(1)
        
    # Error 2: Recurso no encontrado (404)
    if response.status_code == 404:
        print("Error 404: No se encontraron datos en la API.")
        sys.exit(1)
        
    response.raise_for_status()
    data = response.json()
    
    # Procesamiento de 3 campos exigidos por la rúbrica
    titulo = data.get('title', 'Sin título')
    fecha = data.get('date', 'Sin fecha')
    explicacion = data.get('explanation', 'Sin explicación')
    
    print("=== BOLETÍN ASTRONÓMICO DE LA NASA ===")
    print(f"1. Título de hoy: {titulo}")
    print(f"2. Fecha: {fecha}")
    print(f"3. Resumen: {explicacion[:200]}...")
    print("======================================")
    
# Error 3: Falla de conexión a internet o DNS
except requests.exceptions.ConnectionError:
    print("Error de Red: No se pudo conectar a los servidores de la NASA.")
    sys.exit(1)
# Error 4: Tiempo de espera agotado
except requests.exceptions.Timeout:
    print("Error de Timeout: La API de la NASA tardó demasiado en responder.")
    sys.exit(1)
except requests.exceptions.RequestException as e:
    print(f"Error inesperado en la solicitud: {e}")
    sys.exit(1)
