from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy import Boolean, Column, String, Integer, delete, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

def generate_uuid():
    return str(uuid.uuid4())
class Vehicle(Base):
   __tablename__ = 'Vehicle'
   id = Column(String, name="uuid", primary_key=True, default=generate_uuid)
   vehicle_model = Column(Integer, ForeignKey("VehicleModel.model_id"))
   owner = Column(String)
   fuel_type = Column(String)
   fuel_level = Column(String)
   location = Column(String)
   veh = relationship("VehicleModel", back_populates="vehmodel")

class VehicleModel(Base):
   __tablename__ = 'VehicleModel'
   model_id = Column(Integer, primary_key=True)
   model_name = Column(String)
   year = Column(Integer)
   vehicle_type = Column(String)
   vehmodel = relationship("Vehicle", back_populates="veh", cascade="all, delete, delete-orphan")