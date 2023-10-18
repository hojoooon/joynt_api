from fastapi import FastAPI,Depends, Response
from fastapi.responses import RedirectResponse
from sqlmodel import Session

from model import Sensor
from database import engineconn

import uvicorn  

app = FastAPI()
engine = engineconn()
session = engine.sessoinmaker()


@app.post("/sensor", status_code = 201) 
def save_data(sensor: Sensor):
    user = Sensor()
    user.user_id = sensor.user_id
    user.SENSOR_DT = sensor.SENSOR_DT
    user.EXER_TIME = sensor.EXER_TIME
    user.EXER_COUNT = sensor.EXER_COUNT
    user.INTENSITY = sensor.INTENSITY

    session.add(user)
    session.commit()

    return {"message":"data saved successfully"}



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port = 8000, reload = True)