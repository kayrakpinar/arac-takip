from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas

def get_vehicle(db: Session, vehicle_id: str):
    return db.query(models.Vehicle).where(models.Vehicle.id == vehicle_id).first()

def get_all_vehicles(db: Session):
    return db.query(models.Vehicle).all()

def create_vehicle(db: Session, vehicles: schemas.VehicleBM):
    db_vehicle = models.Vehicle(**vehicles.dict())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def delete_vehicle(db: Session, vehicle_id: str) -> bool:
    if db.query(models.Vehicle).filter_by(id = vehicle_id).count() != 0:
        veh = db.query(models.Vehicle).where(models.Vehicle.id == vehicle_id).first()
        db.delete(veh)
        db.commit()
        if db.query(models.Vehicle).filter_by(id = vehicle_id).count() == 0:
            return True
        else:
            return False
    else:
        return None

def update_vehicle(db: Session, vehicle_id: str, vehicles: schemas.VehicleBM):
    obj = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    for key, value in vehicles.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def get_vehicle_model(db: Session, model_id: int):
    return db.query(models.VehicleModel).where(models.VehicleModel.model_id == model_id).first()

def get_all_vehicle_models(db: Session):
    return db.query(models.VehicleModel).all()

def create_vehicle_model(db: Session, vehicle_models: schemas.VehicleModelBM):
    db_vehicle_model = models.VehicleModel(**vehicle_models.dict())
    db.add(db_vehicle_model)
    db.commit()
    db.refresh(db_vehicle_model)
    return db_vehicle_model

def delete_vehicle_model(db: Session, model_id: int) -> bool:
    if db.query(models.VehicleModel).filter_by(model_id = model_id).count() != 0:
        veh = db.query(models.VehicleModel).where(models.VehicleModel.model_id == model_id).first()
        db.delete(veh)
        db.commit()
        if db.query(models.VehicleModel).filter_by(model_id = model_id).count() == 0:
            return True
        else:
            return False
    else:
        return None

def update_vehicle_model(db: Session, model_id: id, vehicle_models: schemas.VehicleModelRequest):
    obj = db.query(models.VehicleModel).filter(models.VehicleModel.model_id == model_id).first()
    for key, value in vehicle_models.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj