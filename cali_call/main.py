from fastapi import FastAPI, Depends, Response
from fastapi.responses import RedirectResponse

from model import Cali
from database import engineconn

import uvicorn

app = FastAPI()
engine = engineconn()
session = engine.sessionmaker()


@app.get("/get_data/{sensor_nm}")
async def get_data(sensor_nm: str, response: Response):
        cali_data = session.query(Cali).filter(Cali.SENSOR_NM == sensor_nm).first()
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
    uvicorn.run("main:app", host="127.0.0.1", port = 8000, reload = True)

