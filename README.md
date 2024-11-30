# README.md

# ue19-lab-05

Ce projet contient une app Python (app.py) qui interroge un API publique pour afficher une blague. Le service utilisé est **JokesAPI**, comme proposé dans l'énoncé.

## Fonctionnalités
- Interroge JokesAPI pour récupérer et afficher une blague aléatoire.
- Exécutable à la fois en local et dans un conteneur Docker.

## Prérequis
- Python 3.9 ou supérieur.
- Docker (si vous souhaitez exécuter dans un conteneur).

## Installation

### Exécution locale
1. Clonez le repository :
   ```bash
   git clone https://github.com/L-tech-arch/ue19-lab-05/
   cd ue19-lab-05
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Exécutez l'application :
   ```bash
   python app.py
   ```

### Exécution avec Docker
1. Construisez l'image Docker :
   ```bash
   docker build -t jokes-api-app .
   ```

2. Exécutez le conteneur :
   ```bash
   docker run --rm jokes-api-app
   ```

## Fichiers inclus
- **app.py** : Contient le code de l'application.
- **requirements.txt** : Liste des dépendances Python.
- **Dockerfile** : Décrit comment construire le conteneur Docker.

# app.py

import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    try:
        response = requests.get(url)
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

# requirements.txt

requests==2.31.0

# Dockerfile

# Étape de base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY app.py requirements.txt ./

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande pour exécuter le script
CMD ["python", "app.py"]
