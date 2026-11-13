"""Small analyses of daily weather data."""


def analyze_weather_data(data, analysis_type):
    """Analyze a list of daily records such as {"date": ..., "temperature": ..., "humidity": ...}."""
    if analysis_type == "average":
        total_temp = sum(item["temperature"] for item in data)
        total_humidity = sum(item["humidity"] for item in data)
        avg_temp = total_temp / len(data)
        avg_humidity = total_humidity / len(data)
        return {"average_temperature": avg_temp, "average_humidity": avg_humidity}

    elif analysis_type == "max":
        max_temp_day = max(data, key=lambda x: x["temperature"])
        return {"max_temperature_date": max_temp_day["date"]}

    elif analysis_type == "min":
        min_temp_day = min(data, key=lambda x: x["temperature"])
        return {"min_temperature_date": min_temp_day["date"]}

    elif analysis_type == "trend":
        temperatures = [item["temperature"] for item in data]
        return {"temperature_change": temperatures[-1] - temperatures[0]}
