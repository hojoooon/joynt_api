from sqlalchemy import Column, Integer, VARCHAR, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Sensor(Base):
    __tablename__ = "user_fit_data"
    user_id: Column(VARCHAR(255), primary_key=True)
    SENSOR_DT: Column(DateTime)
    EXER_TIME: Column(DateTime)
    EXER_COUNT: Column(Integer)
    INTENSITY: Column(Integer)
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