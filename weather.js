console.log("📌 weather.js está ejecutándose");
  try {
    console.log("Buscando ciudad:", city);

    if (!city || city.trim() === "") {
      throw new Error("Debes ingresar el nombre de una ciudad.");
    }

    const geoResponse = await fetch(
      `https://geocoding-api.open-meteo.com/v1/search?name=${encodeURIComponent(city)}&count=1`
    );

    if (!geoResponse.ok) {
      throw new Error("Error en la Geocoding API.");
    }

    const geoData = await geoResponse.json();

    if (!geoData.results || geoData.results.length === 0) {
      throw new Error("Ciudad no encontrada.");
    }

    const { name, latitude, longitude } = geoData.results[0];

    console.log("Coordenadas:", latitude, longitude);

    const weatherResponse = await fetch(
      `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current_weather=true`
    );

    if (!weatherResponse.ok) {
      throw new Error("Error en la Weather Forecast API.");
    }

    const weatherData = await weatherResponse.json();

    if (!weatherData.current_weather) {
      throw new Error("No se pudo obtener el clima actual.");
    }

    const temperature = weatherData.current_weather.temperature;
    const weatherCode = weatherData.current_weather.weathercode;

    return {
      city: name,
      temperature: `${temperature} °C`,
      description: getWeatherDescription(weatherCode),
    };
  } catch (error) {
    return { error: error.message };
  }


function getWeatherDescription(code) {
  const codes = {
    0: "Cielo despejado",
    1: "Parcialmente nublado",
    2: "Nublado",
    3: "Cubierto",
    45: "Niebla",
    48: "Niebla con depósitos de hielo",
    51: "Llovizna ligera",
    53: "Llovizna moderada",
    55: "Llovizna densa",
    56: "Llovizna helada ligera",
    57: "Llovizna helada densa",
    61: "Lluvia ligera",
    63: "Lluvia moderada",
    65: "Lluvia fuerte",
    66: "Lluvia helada ligera",
    67: "Lluvia helada fuerte",
    71: "Nieve ligera",
    73: "Nieve moderada",
    75: "Nieve fuerte",
    77: "Granizo",
    80: "Lluvia por chubascos ligera",
    81: "Lluvia por chubascos moderada",
    82: "Lluvia por chubascos fuerte",
    85: "Nieve por chubascos ligera",
    86: "Nieve por chubascos fuerte",
    95: "Tormenta",
    96: "Tormenta con granizo ligera",
    99: "Tormenta con granizo fuerte",
  };

  return codes[code] || "Descripción no disponible";
}

// Ejecutar la función y mostrar el resultado
getWeatherByCity("Tokyo")
  .then((res) => console.log("Resultado:", res))
  .catch((err) => console.log("Error:", err));

