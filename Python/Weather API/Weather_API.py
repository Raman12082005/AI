import requests
from config import api_key

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=5)

        print("\n***************-------------API output------------****************\n")
        print("Your status code : ", response.status_code)
        if response.status_code == 200:
            print("The request was successful")
            data = response.json()
            print(f"temperature = {data["main"]["temp"]}")
            print(f"humidity = {data["main"]["humidity"]}")
            print(f"wind_speed = {data["wind"]["speed"]}")
            print(f"weather = {data["weather"][0]["description"]}")

            rain = data.get("rain", "No rain data")
            print("Rain:", rain)

            print(f"country = {data["sys"]["country"]}")

        elif response.status_code == 404:
            print("City not found")
            print(response.json())

        elif response.status_code == 401:
            print("Invalid API key")
            print(response.json())

        else:
            print(response.json())
            print("Server Error")
    except requests.exceptions.ConnectionError:
        print("No Internet Connection")
    except requests.exceptions.Timeout:
        print("Request Timeout")
    except Exception as e:
        print(e)



while(True):
    city = input("Enter the city name (or type 'exit' to quit): ")
    if city == "exit":
        print("\n*********-------Thankyou for using Weather API---------**********\n")
        break

    get_weather(city)
