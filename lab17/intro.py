import requests

#1 Consuming a Public API with Python

api_url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 5,
    "page": 1,
    "sparkline": "false"
}

response = requests.get(api_url, params=params)

if response.status_code == 200:
    data = response.json()
    for coin in data:
        print(f"{coin['name']}: ${coin['current_price']}")

else:
    print("Failed to retrieve data:", response.status_code)

#2 API Endpoint Call

api_url = "https://api.example.com/data?type=latest&limit=5"
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    print("Data received:", data)
else:
    print("Error fetching data")

#3
# Example API endpoint (this is a dummy URL for demonstration purposes)
api_url = "https://api.example.com/weather"

# Parameters for the API request, such as the city name and API key
params = {
    "city": "New York",
    "apikey": "your_api_key_here"
}

# Make a GET request to the API
response = requests.get(api_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    weather_data = response.json()  # Convert JSON response to a Python dictionary
    print("Current Weather Data:")
    print(weather_data)
else:
    print("Failed to retrieve data. Status code:", response.status_code)
