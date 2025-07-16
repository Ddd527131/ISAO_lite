from fastapi import APIRouter
from pathlib import Path
import json

router = APIRouter()

@router.get("/sensors")
def get_sensor_data():
    path = Path("mock_data/sensors.json")
    with open(path) as f:
        data = json.load(f)
    return data
