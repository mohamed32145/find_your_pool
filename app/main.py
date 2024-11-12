from fastapi import FastAPI

from app.database import Base, engine
from app.routers import Pool, Manager, Bracelet






# Initialize  FastAPI
app = FastAPI()

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)


app.include_router(Pool.router)
app.include_router(Manager.router)
app.include_router(Bracelet.router)













