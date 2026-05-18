# NasaFotoAPI

# Extractor de "La Foto del Día de la NASA"

## Contexto y Narrativa
* **Stakeholder:** El administrador de redes sociales y creador de contenido de un observatorio astronómico local (o club de ciencias).
* **Propuesta de Valor (Problema/Solución):** Para mantener a la comunidad interesada, el administrador necesita publicar contenido espacial diario, atractivo y verificado. Sin embargo, ingresar a los portales oficiales, descargar las imágenes y resumir manualmente los datos técnicos consume demasiado tiempo en su rutina diaria. Esta aplicación de consola resuelve ese problema automatizando la extracción de "La Foto del Día" de la API oficial de la NASA, descargando la imagen en alta calidad al instante y entregando por consola el título, la fecha y un resumen del fenómeno, listos para ser publicados en sus redes.

## Guía de Configuración
Para ejecutar este proyecto, necesitas configurar una variable de entorno en tu sistema para que la aplicación pueda autenticarse con la API de la NASA de forma segura:

* **Variable requerida:** `API_KEY_PROYECTO`
* *Nota:* Para facilitar la evaluación y las pruebas rápidas, se puede utilizar la clave pública que ofrece la NASA asignando el valor `DEMO_KEY` a esta variable.

### Configuración en Linux / macOS (Terminal):
```bash
export API_KEY_PROYECTO="DEMO_KEY"
```
