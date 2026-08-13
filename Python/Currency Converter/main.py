import requests
from config import api_key

def convert_currency():
    from_currency = input("Select the Base Currency: ").upper()
    to_currency = input("Enter the Required Currency: ").upper()
 
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    try:
        print("************----------API Output-----------***********")
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            amount = float(input("Enter amount: "))
            data = response.json()
            if to_currency in data["conversion_rates"]:
                print("********--------Request is Successfull-------*********")
                exchange_rate = data["conversion_rates"][f"{to_currency}"]
                print(f"Exchange rate of 1{from_currency} to {to_currency} is {exchange_rate}")
                print(f"Your exchange amount is: {exchange_rate * amount}")
            else:
                print("Invalid Currency Code")



        elif response.status_code == 404:
            print("Error in request")
            print(response.json())

        elif response.status_code == 401:
            print("Invalid API key")
            print(response.json())

    except requests.exceptions.Timeout:
        print("Request Timeout")
    except Exception as e:
        print(e)

while(True):
    choise = input("do you wnat to continue(Y/N): ").upper()
    if choise == "N":
        break

    convert_currency()
