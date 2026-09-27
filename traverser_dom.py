import requests
from bs4 import BeautifulSoup as soup

url = "https://www.kadea.academy/"
reponse = requests.get(url) #on utilise la méthode get pour envoyer une requête HTTP GET à l'URL spécifiée.
soup = soup(reponse.text, "html.parser") #on utilise BeautifulSoup pour parser le contenu HTML de la page web. on peut parser le contenu en utilisant différents parsers tels que "html.parser", "lxml", "html5lib",xml etc.

#si le parser "html.parser" donne des erreurs, on peut utiliser "lxml" ou "html5lib" à la place.

def traverse_dom(element, level = 0):
    """fonction récursive pour parcourir le DOM de la page web et afficher les balises HTML et leur contenu."""

    #on utilise level pour indenter les balises HTML en fonction de leur niveau dans le DOM.
    if element.name: #on utilise name pour vérifier si l'élément est une balise HTML.
        print("  " * level + f"<{element.name}>") #on utilise name pour récupérer le nom de la balise HTML.
    if hasattr(element,"children"): #on utilise hasattr pour vérifier si l'élément a des enfants.

        for child in element.children: #on utilise children pour récupérer les enfants de la balise HTML.
            traverse_dom(child, level + 1) #on appelle la fonction récursive pour parcourir les enfants de la balise HTML.

traverse_dom(soup) #on appelle la fonction traverse_dom pour parcourir le DOM de la page web.

"""on utilise traverse_dom pour parcourir le DOM de la page web et afficher les balises HTML et 
leur contenu. on peut utiliser cette fonction pour analyser la structure du DOM de la page web et 
extraire des informations spécifiques en fonction des balises HTML et de leur contenu."""