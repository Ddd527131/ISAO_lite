from fastapi import FastAPI, WebSocket
# ...existing code...
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import alerts, sensors


app = FastAPI()

# CORS pour que le frontend communique
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(alerts.router)
app.include_router(sensors.router)
# Pour autoriser frontend Vue.js
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # sécurise plus tard
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connexions WebSocket
clients = []

@app.websocket("/ws/alerts")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            await websocket.receive_text()  # garde la connexion ouverte
    except:
        clients.remove(websocket)

# Fonction pour envoyer une nouvelle alerte à tous
async def broadcast_alert(alert: dict):
    living_clients = []
    for ws in clients:
        try:
            await ws.send_json(alert)
            living_clients.append(ws)
        except:
            pass  # ignore client mort
    clients[:] = living_clients