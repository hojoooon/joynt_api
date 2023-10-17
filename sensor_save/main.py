from fastapi import FastAPI,Depends, Response
from fastapi.responses import RedirectResponse
from typing import List
from sqlmodel import Session

from model import Sensor
from database import SensorModel, engine

import uvicorn  

app = FastAPI()
data = []

def get_session():
    with Session(engine) as session:
        yield session

    

@app.post("/sensor", status_code = 201) #response model 에러로 인해 x
def save_data(sensor: SensorModel, session: Session=Depends(get_session)):
    session.add(sensor)
    session.commit()
    session.refresh(sensor)

    return {"message":"data saved successfully"}
    

if __name__ == "__main__":
    #uvicorn.run("main:app", host="35.216.50.104", port=8001, reload=True)
    uvicorn.run("main:app", host="127.0.0.1", port = 8000, reload = True)