from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cali(BaseModel):
    #__tablename__ = "sensor_calibrations"
    SENSOR_NM: str
    CALIBRATION_VALUE: int

    '''class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example":{
                "SENSOR_NM": "Joynt Fit Sensor 1",
                "CALIBRATION_VALUE": 52590
            }
        }'''