from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

from app.database import Base, engine
from app.routers import Pool, Manager, Bracelet




oauth2_schema = OAuth2PasswordBearer(tokenUrl="manager/login")


# Initialize  FastAPI
app = FastAPI()

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)


app.include_router(Pool.router)
app.include_router(Manager.router)
app.include_router(Bracelet.router)













