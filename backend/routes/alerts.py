from fastapi import APIRouter, Query
from typing import List, Optional
from models.schemas import Alert

router = APIRouter()

fake_alerts_db = [  # temporaire si pas encore connecté à Mongo
    {"id": 1, "type": "feu", "description": "Incendie zone A", "latitude": 48.8, "longitude": 2.3},
    {"id": 2, "type": "inondation", "description": "Inondation zone B", "latitude": 48.9, "longitude": 2.4},
    {"id": 3, "type": "feu", "description": "Feu zone C", "latitude": 48.85, "longitude": 2.35},
]

@router.get("/alerts", response_model=List[Alert])
def get_alerts(type: Optional[str] = Query(None)):
    if type:
        return [a for a in fake_alerts_db if a["type"] == type]
    return fake_alerts_db

@router.post("/alerts", response_model=Alert)
async def create_alert(alert: Alert):
    from main import broadcast_alert  # import ici pour éviter l'import circulaire
    await broadcast_alert(alert.dict())
    return alert