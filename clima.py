import requests


def obtener_coordenadas(ciudad):
    """
    Usa la API de geocoding para obtener la latitud y longitud de una ciudad.
    Devuelve una tupla (lat, lon) o None si no se encuentra la ciudad.
    """
    # URL del servicio que convierte una ciudad en coordenadas
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    # Parámetros que se envían en la petición (nombre de la ciudad y 1 resultado)
    geo_params = {"name": ciudad, "count": 1}

    # Hacemos la petición a la API y convertimos la respuesta a formato JSON (diccionario)
    geo_respuesta = requests.get(geo_url, params=geo_params).json()

    # Si no hay resultados, devolvemos None para indicar que no se encontró la ciudad
    if "results" not in geo_respuesta or not geo_respuesta["results"]:
        return None

    # Tomamos el primer resultado y extraemos latitud y longitud
    lat = geo_respuesta["results"][0]["latitude"]
    lon = geo_respuesta["results"][0]["longitude"]

    return lat, lon


def obtener_clima_actual(lat, lon):
    """
    Usa la API de clima para obtener el clima actual a partir de latitud y longitud.
    Devuelve el diccionario con la información del clima.
    """
    # URL del servicio de clima
    clima_url = "https://api.open-meteo.com/v1/forecast"

    # Parámetros: latitud, longitud y que queremos el clima actual
    clima_params = {"latitude": lat, "longitude": lon, "current_weather": True}

    # Hacemos la petición a la API y devolvemos la respuesta en formato JSON
    clima = requests.get(clima_url, params=clima_params).json()

    return clima


def mostrar_temperatura(ciudad, clima):
    """
    Muestra en pantalla la temperatura actual de una ciudad,
    usando la información devuelta por la API de clima.
    """
    temperatura = clima["current_weather"]["temperature"]
    print(f"La temperatura en {ciudad} es {temperatura}°C")


def main():
    """Función principal del programa."""
    # Pedimos al usuario el nombre de la ciudad
    ciudad = input("Ingresa la ciudad: ")

    # Obtenemos las coordenadas de la ciudad
    coordenadas = obtener_coordenadas(ciudad)

    # Si no se encontraron coordenadas, mostramos un mensaje y terminamos
    if coordenadas is None:
        print("Ciudad no encontrada.")
        return

    lat, lon = coordenadas

    # Obtenemos el clima actual usando las coordenadas
    clima = obtener_clima_actual(lat, lon)

    # Mostramos la temperatura actual
    mostrar_temperatura(ciudad, clima)


if __name__ == "__main__":
    main()
