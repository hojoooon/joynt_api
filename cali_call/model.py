from sqlalchemy import Column, Integer, String, VARCHAR, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Cali(Base):
    __tablename__ ="sensor_calibration"
    SENSOR_NM: Column(VARCHAR(255), nullable=False, primary_key=True)
    CALIBRATION_VALUE: Column(Integer)
