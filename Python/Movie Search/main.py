import requests
from config import api_key

def findMovieDetails(movie):
    url = f"https://www.omdbapi.com/?apikey={api_key}&t={movie}"
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        print(status_code)

        if(status_code == 200):
            data = response.json()
            if(data["Response"] == "False"):
                print("**********------------REQUEST IS SUCCESSFULL but MOVIE NOT FOUND-----------***********")
                
            else:
                print("***********----------Request is Successfull------------**********")

                print(f"\nMovie Name: {data['Title']}\n")
                print(f"Released date: {data['Released']}\n")
                print(f"Length: {data['Runtime']}\n")
                print(f"Genre: {data['Genre']}\n")

                Director = data.get("Director", "N/A")
                print(f"Director: {Director}\n")

                Writer = data.get("Writer", "N/A")
                print(f"Writer: {Writer}\n")

                print(f"Actors: {data['Actors']}\n")
                print(f"Plot: {data['Plot']}\n")

                Awards = data.get("Awards", "N/A")
                print(f"Awards: {Awards}\n")

                posterLink = data.get("Poster", "N/A")
                print(f"Poster Link: {posterLink}")

                BoxOffice = data.get("BoxOffice", "N/A")
                print(f"BoxOffice Revenue: {BoxOffice}\n")

                print(f"imdb Rating: {data['imdbRating']}\n")
                for article in data["Ratings"]:
                    print(f"Source: {article['Source']}\n")
                    print(f"Value: {article['Value']}\n")



        elif(status_code == 404):
            print("**********------------MOVIE NOT FOUND-----------***********")
            print(response.json())

        elif(status_code == 401):
            print("***********------------INVALID API KEY----------***********")
            print(response.json())

        else:
            print("***********------------SERVER ERROR-----------************")
            print(response.json())

    except requests.exceptions.Timeout:
        print("***********------------REQUEST TIMEOUT-------------***********")

    except requests.exceptions.ConnectionError:
        print("***********------------NETWORK ERROR------------*************")
    
    except Exception as e:
        print(e)

while(True):
    choise = input("Enter a movie Name (or Exit to exit): ")
    if(choise.upper() == "EXIT"):
        break
    else:
        findMovieDetails(choise)
        