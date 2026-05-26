import httpx


def fetch_temperature(city_name: str):
    url = f"https://wttr.in/{city_name}?format=j1"
    response = httpx.get(url)
    data = response.json()
    return float(data["current_condition"][0]["temp_C"])