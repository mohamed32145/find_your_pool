from fastapi import FastAPI, Request,Depends
from app.models.classees import *      # Import your classes as needed
from app.models.schema import Pool
from app.database import get_db, Base, engine
from sqlalchemy.orm import Session


# Initialize  FastAPI
app = FastAPI()

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)


# Define your routes
@app.post("/add_pool/")
async def add_pool(length: float, width: float, depth: float, managerid: int, db: Session = Depends(get_db)):
    new_pool = Pool(length=length, width=width, depth=depth, manager_id=managerid)
    db.add(new_pool)
    db.commit()
    db.refresh(new_pool)
    return {"message": "Pool added successfully", "pool": new_pool}

@app.get("/get_pool/")
async def get_pool(poolcode: int):
    try:
        p = sd.findpoolbyid(poolcode)
        if p is None:
            return {"error": f"No pool found with code {poolcode}"}
        return {
            f"pool code is {p.code}, pool depth is {p.depth}, its length is {p.length}, and the width is {p.width}"}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

@app.post("/addbracelet/")
async def add_brac(code: int, customer_name: str, age: int):
    brac = bracelet(code, customer_name, age)
    result = sd.addbracelet(brac)
    return result

@app.post("/addmanager/")
async def add_manager(id: int, name: str, age: int, salary: int):
    manager = Manager(id=id, name=name, age=age, salary=salary)
    response = sd.addmanager(manager)
    return response

