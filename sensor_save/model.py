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
