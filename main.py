from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import database
from pydantic import BaseModel
import datetime


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ClanCreate(BaseModel):
    name: str
    region: str

class ClanResponse(BaseModel):
    id: str
    name: str
    region: str
    created_at: datetime.datetime

    class Config:
        orm_mode = True




@app.post("/clans/", response_model=ClanResponse)
def create_clan(clan: ClanCreate, db: Session = Depends(get_db)):
    db_clan = models.Clan(name=clan.name, region=clan.region)
    db.add(db_clan)
    db.commit()
    db.refresh(db_clan)
    return db_clan


@app.get("/clans/", response_model=List[ClanResponse])
def read_clans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clans = db.query(models.Clan).offset(skip).limit(limit).all()
    return clans


@app.get("/clans/search/")
def search_clans(name: str, db: Session = Depends(get_db)):
    if len(name) < 3:
        raise HTTPException(status_code=400, detail="En az 3 harf giriniz.")
    return db.query(models.Clan).filter(models.Clan.name.ilike(f"%{name}%")).all()


@app.delete("/clans/{clan_id}")
def delete_clan(clan_id: str, db: Session = Depends(get_db)):
    clan = db.query(models.Clan).filter(models.Clan.id == clan_id).first()
    if not clan:
        raise HTTPException(status_code=404, detail="Clan bulunamadı")
    db.delete(clan)
    db.commit()
    return {"status": "success", "message": "Clan silindi"}