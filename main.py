from typing import List
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import crud, models, schemas
from database import SessionLocal, engine
from sqlalchemy.orm import Session
#from sqlalchemy.sql.expression import null

app = FastAPI()
origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
models.Base.metadata.create_all(engine)

@app.post('/api/v1/vehicles/', response_model=schemas.VehicleBM, tags=["Vehicles"])
def create_vehicle(veh: schemas.VehicleBM, db: Session = Depends(get_db)):
    db_vehicle = crud.create_vehicle(db, veh)
    return db_vehicle

@app.get('/api/v1/vehicles/', response_model=List[schemas.VehicleIDBM], tags=["Vehicles"])
def get_vehicles(db: Session = Depends(get_db)):
    return crud.get_all_vehicles(db)

@app.get('/api/v1/vehicles/{vehicle_id}', tags=["Vehicles"])
def get_vehicle(vehicle_id: str, db: Session = Depends(get_db)):
    return crud.get_vehicle(db, vehicle_id)

@app.delete("/api/v1/vehicles/{vehicle_id}", tags=["Vehicles"])
def del_vehicle(vehicle_id: str, db: Session = Depends(get_db)):
    deleted = crud.delete_vehicle(db, vehicle_id)
    return {"vehicle_deleted": deleted}

@app.put("/api/v1/vehicles/{vehicle_id}", response_model=schemas.VehicleBM, tags=["Vehicles"])
def upd_vehicle(vehicle_id: str, veh: schemas.VehicleRequest, db: Session = Depends(get_db)):
    veh.dict(exclude_unset=True)
    veh_update = crud.update_vehicle(db, vehicle_id, veh)
    return veh_update

@app.post('/api/v1/vehicleModels/', response_model=schemas.VehicleModelIDBM, tags=["Vehicle Models"])
def create_vehicle_model(veh: schemas.VehicleModelBM, db: Session = Depends(get_db)):
    return crud.create_vehicle_model(db, veh)

@app.get('/api/v1/vehicleModels/', response_model=List[schemas.VehicleModelIDBM], tags=["Vehicle Models"])
def get_vehicle_models(db: Session = Depends(get_db)):
    return crud.get_all_vehicle_models(db)

@app.get('/api/v1/vehicleModels/{model_id}', tags=["Vehicle Models"])
def get_vehicle_model(model_id: int, db: Session = Depends(get_db)):
    return crud.get_vehicle_model(db, model_id)

@app.delete("/api/v1/vehicleModels/{model_id}", tags=["Vehicle Models"])
def del_vehicle_model(model_id: int, db: Session = Depends(get_db)):
    return {"vehicle_model_deleted": crud.delete_vehicle_model(db, model_id)}

@app.put("/api/v1/vehicleModels/{model_id}", response_model=schemas.VehicleModelBM, tags=["Vehicle Models"])
def upd_vehicle_model(model_id: int, veh: schemas.VehicleModelRequest, db: Session = Depends(get_db)):
    veh.dict(exclude_unset=True)
    veh_update = crud.update_vehicle_model(db, model_id, veh)
    return veh_update

