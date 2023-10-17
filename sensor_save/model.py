from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Sensor(BaseModel):
    user_id: str
    SENSOR_DT: datetime
    EXER_TIME: datetime
    EXER_COUNT: int
    INTENSITY: int
'''
    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example":{
                "user_id": "01012345678",
                "SENSOR_DT": "2023-09-25 16:22:25",
                "EXER_DT": "2023-09-25 16:22:25",
                "EXER_COUNT": 40,
                "INTENSITY": 3
            }
        }
'''