from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from enums import VehicleTypeEnum

class VehicleBM(BaseModel):
    vehicle_model: int
    owner: str
    fuel_type: str
    fuel_level: int
    location: str
    class Config:
        orm_mode = True

class VehicleRequest(BaseModel):
    vehicle_model: Optional[int]
    owner: Optional[str]
    fuel_type: Optional[str]
    fuel_level: Optional[int]
    location: Optional[str]

class VehicleModelBM(BaseModel):
    model_name: str
    year: int
    vehicle_type: VehicleTypeEnum
    class Config:
        orm_mode = True

class VehicleModelRequest(BaseModel):
    model_name: Optional[str]
    year: Optional[int]
    vehicle_type : Optional[VehicleTypeEnum]

class VehicleIDBM(VehicleBM):
    id: UUID

class VehicleModelIDBM(VehicleModelBM):
    model_id: int
