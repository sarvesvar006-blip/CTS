import requests

class WeatherAPI:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_weather(self):
        try:
            response = requests.get(self.api_url, timeout=5)

            if response.status_code == 404:
                return "Error: API endpoint not found (404)."

            response.raise_for_status()

            data = response.json()

            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"]

            return f"Temperature: {temp}°C\nCondition: {condition}"

        except requests.exceptions.ConnectionError:
            return "Error: Network connection problem."
        except requests.exceptions.Timeout:
            return "Error: Request timed out."
        except requests.exceptions.RequestException as e:
            return f"Request Error: {e}"
        except KeyError:
            return "Error: Unexpected API response format."
        except ValueError:
            return "Error: Invalid JSON response."


# Example API (you can replace with real weather API URL)
api_url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY&units=metric"

weather = WeatherAPI(api_url)
result = weather.fetch_weather()

print(result)