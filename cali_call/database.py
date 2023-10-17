from typing import Optional
from sqlmodel import Field, SQLModel, create_engine

db_url = 'mysql+pymysql://root:12345!34.64.233.229:3306/playground2'
db_file = 'data.db'
engine = create_engine(f'sqlite:///{db_url}', echo=True, connect_args={"check_same_thread": False})

class CaliModel(SQLModel, table=True):
    __tablename__ = "sensor_calibrations"
    
    SENSOR_NM: str = Field(primary_key=True)
    CALIBRATION_VALUE: int


def create_table():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_table()
