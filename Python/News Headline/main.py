import requests
from config import api_key

def news_headline(choise):
    categories = {
        1 : "technology",
        2 : "sprots",
        3 : "business",
        4 : "health"
    }
    category = categories[choise]
    url = f"https://newsdata.io/api/1/latest?apikey={api_key}"
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        print(f"Your Status Code is: {status_code}")

        if(status_code == 200):
            print("*******---------Request is Successfull---------**********")
            data = response.json()

            for article in data["results"]:
                print("\n--------------------------------")
                print(f"Headline: {article["title"]}")
                print(f"Description: {article["description"]}")
                print(f"Source: {article["source_name"]}")
                print(f"Date: {article["pubDate"]}")
                print(f"Link: {article["link"]}")


        elif status_code == 404:
            print("**********--------------News Not found----------------************")
            print(response.json())

        elif status_code == 401:
            print("***********-------------Invalid API key------------************")
            print(response.json())

        else:
            print("**********--------------server Error-------------**************")
            print(response.json())



    except requests.exceptions.ConnectionError:
        print("*********---------------Network Error-------------***************")

    except requests.exceptions.Timeout:
        print("**********-------------Request Timeout------------***********")

    except Exception as e:
        print(e)


while(True):
    print("1. Technology Realted News")
    print("2. Sports Related News")
    print("3. Business Related News")
    print("4. Healthcare realted News")
    print("5. Exit")
    choise = int(input("Enter Your choise : "))

    if choise == 5:
        break
    elif (choise < 1) & (choise > 5) : 
        print("*************-------------Invalid Choise---------------**************")

    else:
        news_headline(choise)