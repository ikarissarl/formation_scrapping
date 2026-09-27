# 🕷️ Formation Web Scraping avec Python - Notes & Projets

Ce dépôt contient mes notes de cours, mes exemples de code et mes projets pratiques réalisés dans le cadre de la formation complète de ~10h sur le Web Scraping en Python dispensée par **[Docstring](https://www.docstring.fr/)**.

🎥 **Vidéo complète de la formation :** [Scraping avec Python : La Formation Complète (YouTube)](https://youtu.be/sOAZpHDEdkg?si=zozc29rkoOAybqSo)

---

## 📌 Présentation de la Formation

Cette formation aborde le web scraping de A à Z : des fondamentaux théoriques et légaux jusqu'à la mise en production de scripts automatisés sur des sites réels, en passant par le contournement des blocages anti-bot.

### 🎯 Objectifs
- Comprendre les principes du web scraping et le cadre légal/éthique.
- Maîtriser l'extraction et l'analyse de données HTML/JSON.
- Automatiser des scripts et les surveiller en production 24/7.
- Contourner les obstacles techniques (JavaScript dynamique, Captchas, Anti-bots, blocages IP).

---

## 🛠️ Stack Technique & Outils

* **Langage :** Python 3.x
* **Requêtes HTTP & Extraction HTML :**
  * `requests` — Requêtes HTTP synchrones
  * `BeautifulSoup4` — Parsing HTML / XML & navigation dans le DOM
  * `selectolax` — Parser HTML haute performance
* **Scraping Dynamique & Automation :**
  * `Playwright` — Automatisation du navigateur pour le contenu généré dynamiquement en JS
* **Gestion des Bloqueurs & Proxies :**
  * `Bright Data` — Intégration de proxies et Bright Data Scraping Browser
* **Monitoring, Logging & Automation :**
  * `Sentry` — Suivi et capture des erreurs en temps réel
  * `Cron` / `Crontab` — Planification automatique des tâches
  * Deployment sur VPS (Virtual Private Server)

---

## 🔗 Ressources & Liens Utiles

* 📺 **Formation YouTube :** [Regarder la vidéo sur YouTube](https://youtu.be/sOAZpHDEdkg?si=zozc29rkoOAybqSo)
* 🌐 **Plateforme Docstring :** [Docstring.fr](https://www.docstring.fr/) (Exercices, quiz, formations Python complémentaires)
* 💬 **Communauté Discord :** [Rejoindre le Discord Docstring](https://discord.gg/docstring)
* 🛡️ **Proxies & Scraping Browser :** [Bright Data](https://brightdata.com/) (Lien dans la description de la vidéo pour tester avec des crédits gratuits)
* 📊 **Suivi des erreurs :** [Sentry.io](https://sentry.io/)

### 📖 Documentations Officielles
* 📄 [Python Documentation](https://docs.python.org/3/)
* 📄 [Requests Documentation](https://requests.readthedocs.io/)
* 📄 [Beautiful Soup 4 Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* 📄 [Selectolax Documentation](https://selectolax.readthedocs.io/)
* 📄 [Playwright for Python](https://playwright.dev/python/)

---

## 📂 Structure du Répertoire

```text
.
├── 01_bases_requests_bs4/     # Premières requêtes HTTP et manipulation du DOM
├── 02_scraping_avance/        # Utilisation de Selectolax, Playwright et proxies
├── 03_projet_airbnb/          # Projet d'extraction de prix Airbnb
├── 04_projet_amazon_alerts/   # Script de veille tarifaire & notifications
├── requirements.txt           # Liste des dépendances Python du projet
└── README.md                  # Ce fichier

