from pydantic import BaseModel
from typing import Optional, List

class VehicleBM(BaseModel):
    vehicle_model: int
    owner: str
    fuel_type: str
    fuel_level: str
    location: str
    class Config:
        orm_mode = True
class VehicleModelBM(BaseModel):
    model_name: str
    year: int
    vehicle_type: str
    class Config:
        orm_mode = True
class VehicleIDBM(VehicleBM):
    id: str
class VehicleModelIDBM(VehicleModelBM):
    model_id: int
