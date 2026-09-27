import requests
from bs4 import BeautifulSoup as soup

url = "https://www.kadea.academy/"
reponse = requests.get(url) #on utilise la méthode get pour envoyer une requête HTTP GET à l'URL spécifiée.
soup = soup(reponse.text, "html.parser") #on utilise BeautifulSoup pour parser le contenu HTML de la page web. on peut parser le contenu en utilisant différents parsers tels que "html.parser", "lxml", "html5lib",xml etc.

#si le parser "html.parser" donne des erreurs, on peut utiliser "lxml" ou "html5lib" à la place.

body = soup.find_all("body") #on utilise find_all pour récupérer toutes les balises HTML "body" de la page web. on peut utiliser find pour récupérer la première balise HTML "body" de la page web.

print(body) #on utilise print pour afficher le contenu de la balise HTML "body" de la page web.

"""on peut utiliser aside, header, footer, nav, section, article, div, span, h1, 
h2, h3, h4, h5, h6, p, a, img, ul, ol, li etc. pour récupérer les balises HTML spécifiques de la page web.
 on peut aussi utiliser les attributs des balises HTML pour récupérer les balises HTML spécifiques de la page web."""
    