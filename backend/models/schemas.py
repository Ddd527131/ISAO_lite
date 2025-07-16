from pydantic import BaseModel
from typing import Literal

class Alert(BaseModel):
    id: int
    type: Literal["inondation", "feu", "séisme", "canicule"]
    message: str
    latitude: float
    longitude: float
    niveau: int  # 1 à 5

class SensorData(BaseModel):
    id: int
    type: str
    value: float
    unit: str
    latitude: float
    longitude: float
