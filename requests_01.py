import requests as r

url = "https://www.google.com"
reponse = r.get(url) #on utilise la méthode get pour envoyer une requête HTTP GET à l'URL spécifiée.

print(reponse.text) #on utilise text pour récupérer le contenu de la page web.

"""on utilise status_code pour vérifier si la requête a été effectuée avec succès 
(200) ou non (404, 500, etc.), on utilise reponse.text pour récupérer le contenu de la page web."""

#on utilise reponse.raise_for_status() pour lever une erreur.

with open("index.html", "w", encoding="utf-8") as f:
    f.write(reponse.text) #on utilise write pour écrire le contenu de la page web dans un fichier HTML. on peut aussi utiliser ".json" pour ecrire le contenu dans un fichier JSON tlle que une api.