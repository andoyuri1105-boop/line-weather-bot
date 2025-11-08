import requests

API_KEY = "bce0dd5f4f0105d0aad1504b3ff98d8d"
LAT = 43.1143
LON = 141.3392

url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric&lang=ja"

r = requests.get(url)
print("status:", r.status_code)
print("text:", r.text[:500])
