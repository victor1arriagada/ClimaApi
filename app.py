#Victor Arriagada - Foto del día de la NASA
import os
import requests
import sys

API_KEY = os.getenv('API_KEY_PROYECTO')

if not API_KEY:
    print("Error Crítico: La variable de entorno API_KEY_PROYECTO no está configurada.")
    sys.exit(1)

URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

try:
    response = requests.get(URL, timeout=5)
    
    # Error 1: Clave inválida o límite de peticiones
    if response.status_code in [401, 403]:
        print("Error de Autenticación: Clave de API inválida o límite de uso alcanzado.")
        sys.exit(1)
        
    # Error 2: Recurso no encontrado
    if response.status_code == 404:
        print("Error 404: No se encontraron datos en la API.")
        sys.exit(1)
        
    response.raise_for_status()
    data = response.json()
    
    titulo = data.get('title', 'Sin título')
    fecha = data.get('date', 'Sin fecha')
    explicacion = data.get('explanation', 'Sin explicación')
    imagen_url = data.get('url', '')
    media_type = data.get('media_type', '') # A veces la NASA sube videos en vez de fotos
    
    print("=== FOTO DEL DIA (POR LA NASA) ===")
    print(f"1. Título de hoy: {titulo}")
    print(f"2. Fecha: {fecha}")
    print(f"3. Resumen: {explicacion[:150]}...")
    print(f"4. URL Enlace: {imagen_url}")
    
    if media_type == 'image' and imagen_url:
        print("\nDescargando la imagen astronómica...")
        img_response = requests.get(imagen_url, timeout=10)
        img_response.raise_for_status()
        
        with open('foto_nasa_hoy.jpg', 'wb') as file:
            file.write(img_response.content)
            
        print("¡Éxito! La foto se ha guardado como 'foto_nasa_hoy.jpg'.")
    else:
        print("\nNota: El registro de hoy es un video. Abre la URL para verlo.")
        
    print("======================================")
    
# Error 3: Falla de conexión a internet o DNS
except requests.exceptions.ConnectionError:
    print("Error de Red: No se pudo conectar a los servidores.")
    sys.exit(1)
# Error 4: Tiempo de espera agotado
except requests.exceptions.Timeout:
    print("Error de Timeout: La API de la NASA o la descarga tardó demasiado.")
    sys.exit(1)
except requests.exceptions.RequestException as e:
    print(f"Error inesperado en la solicitud: {e}")
    sys.exit(1)
