# ISAO Lite

ISAO Lite est une application web permettant de visualiser et gérer des alertes (feu, inondation, incident chimique) sur une carte interactive. Elle est composée d’un backend Python (FastAPI) et d’un frontend JavaScript (HTML/CSS/Leaflet ou Vue.js).

## Fonctionnalités

- Affichage des alertes sur une carte interactive
- Filtrage des alertes par type
- Ajout d’alertes via une API REST
- Actualisation en temps réel des alertes grâce à WebSocket
- Dashboard listant les alertes

## Structure du projet

```
ISAO-Lite/
│
├── backend/         # Backend FastAPI (API REST + WebSocket)
│   ├── main.py
│   ├── routes/
│   └── models/
│
├── frontend/        # Frontend (HTML, CSS, JS ou Vue.js)
│   ├── index.html
│   ├── style.css
│   └── app.js
│
└── README.md
```

## Installation

### Backend

1. Aller dans le dossier backend :
    ```sh
    cd backend
    ```
2. Installer les dépendances Python :
    ```sh
    pip install fastapi uvicorn
    ```
3. Lancer le serveur :
    ```sh
    uvicorn main:app --reload
    ```

### Frontend

1. Aller dans le dossier frontend :
    ```sh
    cd frontend
    ```
2. Installer les dépendances (si besoin) :
    ```sh
    npm install
    ```
3. Lancer le serveur de développement :
    ```sh
    npm run dev
    ```
   ou ouvrir directement `index.html` dans votre navigateur.

## Utilisation

- Accédez à l’interface web via le frontend (ex : http://127.0.0.1:8080).
- Les alertes sont affichées sur la carte et dans le dashboard.
- Les nouvelles alertes sont reçues en temps réel grâce à WebSocket.

## Technologies utilisées

- **Backend** : Python, FastAPI, Uvicorn
- **Frontend** : HTML, CSS, JavaScript, Leaflet, (optionnel : Vue.js)
- **WebSocket** pour la communication temps réel

## Auteur

- DONKOU NGOUADOU DURAND ADMIN
---
