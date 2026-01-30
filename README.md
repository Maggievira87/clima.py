Consulta en Python que consulta datos meteorológicos usando una API externa.


## Funcionalidades
- Consulta del clima por ciudad
- Manejo de errores
- Soporte para múltiples ciudades
- Pruebas unitarias


## Instalación
pip install requests
# Aplicación del Clima


Proye
## Uso
python weather_app.py

DESCRIPCIÓN DE LA APLICACIÓN

La Aplicación del Clima es un proyecto desarrollado en Python que permite obtener información meteorológica utilizando la API gratuita de Open-Meteo. La función principal, llamada getWeather, consulta datos de temperatura máxima y mínima para una ubicación específica a partir de sus coordenadas geográficas (latitud y longitud) y para un número configurable de días. La aplicación está diseñada para ser clara, reutilizable y robusta frente a errores, lo que la hace adecuada como proyecto académico y como base para desarrollos futuros.

FUNCIONALIDADES PRINCIPALES

La aplicación se ejecuta desde la consola y muestra los datos meteorológicos en formato JSON. Para demostrar su funcionamiento, se realizaron varias pruebas: una con coordenadas válidas (por ejemplo, Berlín), otra con coordenadas diferentes (Nueva York) y una más con coordenadas inválidas. En los casos válidos, la aplicación devuelve correctamente los datos del clima; en el caso inválido, responde con un mensaje de error controlado, lo que demuestra un manejo adecuado de excepciones y fallos de la API.

USO DE LA IA DURANTE EL PROYECTO

La inteligencia artificial fue utilizada como apoyo para revisar el código y mejorar su calidad. Mediante prompts estructurados (usando el marco TRACI), la IA ayudó a identificar oportunidades de mejora en la claridad del código, el manejo de errores y la documentación. También fue clave para generar un primer borrador del docstring de la función getWeather. Sin embargo, todas las sugerencias fueron evaluadas críticamente, aplicando solo aquellas que eran relevantes para el contexto del proyecto.

REFLEXIÓN SOBRE EL APRENDIZAJE Y LOS DESAFÍOS
Uno de los principales aprendizajes fue entender la importancia de escribir código claro y bien documentado, especialmente cuando se trabaja con APIs externas. Un desafío importante fue interpretar cuáles sugerencias de la IA eran realmente útiles y cuáles no aplicaban, lo que reforzó la necesidad del criterio humano. También resultó retador manejar correctamente los errores y pensar en casos límite como coordenadas inválidas o fallos de conexión.

LOGRO PERSONAL Y MEJORA FUTURA

Me siento orgullosa de haber logrado una función bien estructurada, documentada y probada, integrando de forma responsable el apoyo de la IA. Si tuviera más tiempo, mejoraría la aplicación agregando una interfaz gráfica, soporte para múltiples ciudades ingresadas por el usuario y pruebas automatizadas más completas para distintos escenarios.




