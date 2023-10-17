from typing import Optional
from sqlmodel import Field, SQLModel, create_engine
from datetime import datetime
from fastapi import Body

db_url = 'mysql+pymysql://root:12345!@34.64.233.229:3306/playground2' 
db_file = 'data.db'
engine = create_engine(f'sqlite:///{db_url}', echo=True)

class SensorModel(SQLModel, table=True):
    __tablename__ = "user_fit_data"
    user_id: str = Field(default=None, primary_key= True)
    SENSOR_DT: Optional[datetime] = Body(None)
    EXER_TIME: Optional[datetime] = Body(None)
    EXER_COUNT: int
    INTENSITY: int


def create_table():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_table()

