import requests


def getWeather(latitude=52.52, longitude=13.41, forecast_days=7):
    """
    Obtiene el pronóstico del clima utilizando la API gratuita de Open-Meteo.

    Parámetros:
        latitude (float): Latitud de la ubicación. Valor válido entre -90 y 90.
        longitude (float): Longitud de la ubicación. Valor válido entre -180 y 180.
        forecast_days (int): Número de días del pronóstico (por defecto 7).

    Retorna:
        dict: Diccionario con los datos meteorológicos diarios si la solicitud
              es exitosa, o un diccionario con la clave "error" si ocurre
              algún problema.

    Manejo de errores:
        - Coordenadas inválidas.
        - Errores de conexión o tiempo de espera.
        - Respuestas incompletas o inesperadas de la API.

    Notas:
        Open-Meteo es una API de uso libre y no requiere autenticación.

    Ejemplo de uso:
        >>> weather = getWeather(52.52, 13.41, 7)
        >>> print(weather)
    """

    try:
        api_url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "daily": "temperature_2m_max,temperature_2m_min",
            "forecast_days": forecast_days,
            "timezone": "UTC"
        }

        response = requests.get(api_url, params=params, timeout=10)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:
        return {"error": f"No se pudo obtener el pronóstico del clima: {error}"}


# ▶️ BLOQUE PRINCIPAL – PRUEBAS DEL PROGRAMA
if __name__ == "__main__":

    print("Prueba 1: Coordenadas válidas (Berlín)")
    print(getWeather(52.52, 13.41, 7))

    print("\nPrueba 2: Coordenadas diferentes (Nueva York)")
    print(getWeather(40.71, -74.01, 3))

    print("\nPrueba 3: Coordenadas inválidas")
    print(getWeather(999, 999, 7))
