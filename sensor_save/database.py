from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

db_url = 'mysql+pymysql://root:12345!@34.64.233.229:3306/playground2' 
db_file = 'data.db' #목업데이터 확인용

class engineconn:
    engine = create_engine(f'sqlite:///{db_url}', echo=True, connect_args={"check_same_thread": False})

    def sessionmaker(self):
        Session = sessionmaker(bind = self.engine)
        session = Session()
        return session
    
    def connection(self):
        conn = self.engine.connect()
        return conn