import requests
from bs4 import BeautifulSoup as soup

url = "https://www.kadea.academy/"
reponse = requests.get(url) #on utilise la méthode get pour envoyer une requête HTTP GET à l'URL spécifiée.
soup = soup(reponse.text, "html.parser") #on utilise BeautifulSoup pour parser le contenu HTML de la page web. on peut parser le contenu en utilisant différents parsers tels que "html.parser", "lxml", "html5lib",xml etc.

#si le parser "html.parser" donne des erreurs, on peut utiliser "lxml" ou "html5lib" à la place.

print(soup.prettify()) #on utilise prettify pour afficher le contenu HTML de la page web de manière lisible.

with open("kadea_scrapping.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify()) #on utilise write pour écrire le contenu de la page web dans un fichier HTML. on peut aussi utiliser ".json" pour ecrire le contenu dans un fichier JSON tlle que une api.
    