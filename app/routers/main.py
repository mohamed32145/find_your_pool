from fastapi import FastAPI, Request, Depends, HTTPException
from app.models.schema import Pool,Bracelet, Manager
from app.database import get_db, Base, engine
from app.models.models import *
from app.routers.help_functions import *


# Initialize  FastAPI
app = FastAPI()

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)



@app.post("/add_pool/", response_model= PoolResponse)
async def add_pool(length: float, width: float, depth: float,  db: Session = Depends(get_db)):
    new_pool = Pool(length=length, width=width, depth=depth)
    db.add(new_pool)
    db.commit()
    db.refresh(new_pool) # after this refresh new_pool will get the id which is generated automaticlly in postgre table
    response = PoolResponse(message = "pool was added", pool = PoolSchema.model_validate(new_pool))
    return  response

@app.get("/get_pool/")
async def get_pool(poolcode: int, db: Session = Depends(get_db)):
    pool = db.get(Pool, poolcode)
    if pool is None:
        raise HTTPException(status_code=404, detail="pool not found")
    return {"message": "Pool found successfully", "pool": pool}



@app.post("/addbracelet/", response_model= braceletResponse)
async def add_brac(customer_name: str, age: int, db: Session = Depends(get_db)):
    new_brac = Bracelet(customer_name=customer_name, age=age)
    db.add(new_brac)
    db.commit()
    db.refresh(new_brac)

    response = braceletResponse(bracelet = braceletSchema.model_validate(new_brac))

    return response



@app.post("/addmanager/", response_model= managerResponse)
async def add_manager(name: str, age: int, salary: int, db: Session = Depends(get_db)):
    new_manager = Manager(name=name, age=age, salary=salary)
    db.add(new_manager)
    db.commit()
    db.refresh(new_manager)

    managerscema = managerResponse(manager= managerSchema.model_validate(new_manager))

    return managerscema


@app.delete("/deletabrac/{brac_code}")
async  def delete_brac(brac_code: int, db: Session = Depends(get_db)):
    brac = db.get(Bracelet, brac_code)

    if brac is None:
        raise HTTPException(status_code=404, detail="Bracelet not found")
    db.delete(brac)
    db.commit()

    delete_bracelets_by_code(brac_code, db)
    return {"detail": "Bracelet deleted successfully"}

@app.delete("/deletpool/{pool_id}")
async  def delete_brac(pool_id: int, db: Session = Depends(get_db)):
    pool = db.get(Pool, pool_id)

    if pool is None:
        raise HTTPException(status_code=404, detail="Pool not found")
    db.delete(pool)
    db.commit()
# you don’t need to pass session explicitly, Depends(get_db) will automatically handle it.
    delete_rows_by_pool_id(pool_id, db)
    delete_pool_from_pool_manager_table(pool_id, db)

    return {"detail": "Pool deleted successfully"}



@app.delete("/deletmanager/{manager_id}")
async  def delete_brac(manager_id: int, db: Session = Depends(get_db)):
    mang = db.get(Manager ,manager_id)

    if mang is None:
        raise HTTPException(status_code=404, detail="manager not found")
    db.delete(mang)
    db.commit()
    delete_manager_by_id_from_manager_pool(manager_id, db)



    return {"detail": "mnager deleted successfully"}


@app.post("/connect_bracelet_to_pool")
async def connect_bracelet_to_pool(pool_id: int, bracelet_code:int, db: Session = Depends(get_db)):
    pool = db.get(Pool, pool_id)
    if pool is None:
        raise HTTPException(status_code=404, detail="pool not found")
    bracelet = db.get(Bracelet,bracelet_code)
    if bracelet is None:
        raise HTTPException(status_code=404, detail="bracelet not found")

    if bracelet not in pool.my_braces:
        pool.my_braces.append(bracelet)
        db.commit()

    return {"message": f"bracelet '{bracelet.customer_name}' connected to pool '{pool.id}'"}


@app.post("/connect_bracelet_to_manager")
async def connect_bracelet_to_manager(pool_id: int, manager_id:int, db: Session = Depends(get_db)):
    pool = db.get(Pool, pool_id)
    if pool is None:
        raise HTTPException(status_code=404, detail="pool not found")
    manager = db.get(Manager,manager_id)
    if manager is None:
        raise HTTPException(status_code=404, detail="manager not found")

    if manager not in pool.my_manager:
        pool.my_manager.append(manager)
        db.commit()

    return {"message": f"manager '{manager.name}' connected to pool '{pool.id}'"}