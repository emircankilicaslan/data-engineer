from sqlalchemy import Column, String, DateTime
from database import Base
import uuid
import datetime

class Clan(Base):
    __tablename__ = "clans"

 
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    region = Column(String)
   
    created_at = Column(DateTime, default=datetime.datetime.utcnow)