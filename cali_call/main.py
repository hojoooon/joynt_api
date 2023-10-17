from fastapi import FastAPI,Depends, Response, status
from fastapi.responses import RedirectResponse
from typing import List, Union
from sqlmodel import Session

from model import Cali
from database import CaliModel, engine

import uvicorn

app = FastAPI()


def get_session():
    with Session(engine) as session:
        yield session

@app.get("/get_data/{sensor_nm}", response_model = Union[Cali, str])
async def get_data(sensor_nm: str, response: Response, session: Session = Depends(get_session)):
        cali_data = session.get(CaliModel, sensor_nm)
        if cali_data is None:
            response.status_code = 404
            return "Data not found"
        return cali_data
'''
목업데이터 확인용 코드
@app.post("/save_data/", response_model=List[Cali], status_code = 201)
async def save_data(cali: CaliModel, session: Session=Depends(get_session)):
        session.add(cali)
        session.commit()
        session.refresh(cali)

        return session
'''

if __name__ == '__main__':
    #uvicorn.run("main:app", host="35.216.50.104", port = 8001, reload=True)
    uvicorn.run("main:app", host="127.0.0.1", port = 8000, reload = True)

