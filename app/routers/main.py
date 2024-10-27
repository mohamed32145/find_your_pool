from fastapi import FastAPI, Request,Depends

from app.models.schema import Pool,Bracelet, Manager
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
    db.refresh(new_pool) # after this refresh new_pool will get the id which is generated automaticlly in postgre table
    return {"message": "Pool added successfully", "pool": new_pool}

@app.get("/get_pool/")
async def get_pool(poolcode: int, db: Session = Depends(get_db)):

    pool = db.get(Pool, poolcode)
    if pool:
        return {"message": "Pool found successfully", "pool": pool}
    else:
        return {"message" : "this pool not found "}

@app.post("/addbracelet/")
async def add_brac(customer_name: str, age: int, db: Session = Depends(get_db)):
    new_brac = Bracelet(customer_name=customer_name, age=age)
    db.add(new_brac)
    db.commit()
    db.refresh(new_brac)

    return {"message: ": "bracelete was added sucessfulyy", "brac": new_brac}




@app.post("/addmanager/")
async def add_manager(name: str, age: int, salary: int, db: Session = Depends(get_db)):
    manager = Manager( name=name, age=age, salary=salary)
    db.add(manager)
    db.commit()
    db.refresh(manager)
    return {"managere addes successfuly":manager}



