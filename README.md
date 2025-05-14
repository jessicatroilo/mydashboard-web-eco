# 📰 Agrégateur d’Actualités RSS – Python + HTML

Ce projet est un petit agrégateur d’actualités codé en Python, qui récupère et affiche les derniers articles de plusieurs sources via leurs flux RSS. Il peut être utilisé dans un site statique ou intégré dans un projet plus large.

---

## 🔧 Fonctionnalités

- 📥 Lecture des flux RSS depuis plusieurs sources tech / green / éthique
- 🧠 Mise en cache locale (JSON) pour limiter les appels (10 minutes)
- 📅 Formatage lisible des dates de publication
- 🎨 Affichage HTML stylisé selon la source (couleur + icône)
- 🔁 Possibilité d’ajouter un bouton pour recharger dynamiquement via JavaScript

---

## 🚀 Démarrage rapide

### 1. Cloner le projet

```bash
git clone https://github.com/votre-utilisateur/nom-du-repo.git
cd nom-du-repo
````

### 2. Installer les dépendances

Le projet nécessite Python 3.7+ et les paquets suivants :

```bash
pip install feedparser
````

Optionnel (pour afficher les dates en français avec noms de jour/mois) :
```bash
pip install Babel
````

##  📂 Structure du projet

Version 1.0 :
```php
.
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── (on y mettra Tailwind plus tard)
├── rss_cache.json
├── rss_sources.py
├── requirements.txt
````


## ⚙️ Personnalisation
### 🔗 Ajouter une source

Dans ````app.py````, ajoute un flux RSS à la liste FEEDS

```python
FEEDS = [
    {"name": "Nom de la Source", "url": "https://..."},
    ...
]
````

Et dans SOURCE_STYLE, définis sa couleur et son icône :

```python

`SOURCE_STYLE = {
    "Nom de la Source": {"color": "border-rose-400", "icon": "📰"},
    ...
}
```

## ✨ À venir (ou à faire)

-  Bouton “Recharger les actus” (via JS/AJAX) 
-  Tri dynamique côté client 
-  Filtrage par source 
-  Interface plus graphique avec Tailwind CSS ou autre framework CSS  

## 📄License
Projet open-source sous licence MIT. 

## 🙌 Remerciements  
 Merci à toutes les sources d’info utilisées :

🌱[ GreenIT](https://www.greenit.fr/)

📘 [Novethic](https://www.novethic.fr/)

⚙️ [Next INpact](https://www.nextinpact.com/)

💻 [01net](https://www.01net.com/)

📷 [Les Numériques](https://www.lesnumeriques.com/)

🧰[ Code du Garage](https://code-garage.com/)

🧩[ Symfony Blog](https://symfony.com/blog)



## 🌱 Author
#### Jessica Troilo - Développé avec ❤️ pour rester à jour sans se noyer dans 10 000 onglets.
- Github: [@jessicatroilo](https://github.com/jessicatroilo)
- Linkedin [Jessica Troilo](www.linkedin.com/in/jessica-troilo-dev)
