import requests

def get_joke():
    url_joke = "https://v2.jokeapi.dev/joke/Any"
    try:
        response = requests.get(url_joke)
        response.raise_for_status()
        joke_data = response.json()
        if joke_data.get("type") == "single":
            return joke_data.get("joke")
        elif joke_data.get("type") == "twopart":
            return f"{joke_data.get('setup')} - {joke_data.get('delivery')}"
        else:
            return "Une blague n'a pas pu être récupérée."
    except requests.RequestException as e:
        return f"Erreur lors de la récupération de la blague : {e}"

if __name__ == "__main__":
    print("Voici une blague :")
    print(get_joke())