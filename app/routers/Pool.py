from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.database import get_db
from app.help_functions import delete_rows_by_pool_id, delete_pool_from_pool_manager_table
from app.models.models import PoolSchema, PoolResponse
from app.models.schema import Pool


router = APIRouter(
    prefix="/pool",
    tags=['Pool']
)


@router.post("/add_pool", response_model= PoolResponse)
async def add_pool(length: float, width: float, depth: float,  db: Session = Depends(get_db)):
    new_pool = Pool(length=length, width=width, depth=depth)
    db.add(new_pool)
    db.commit()
    db.refresh(new_pool) # after this refresh new_pool will get the id which is generated automaticlly in postgre table
    response = PoolResponse(message = "pool was added", pool = PoolSchema.model_validate(new_pool))
    return  response

@router.get("/get_pool", response_model=PoolResponse)
async def get_pool(poolcode: int, db: Session = Depends(get_db)):
    pool = db.get(Pool, poolcode)
    if pool is None:
        raise HTTPException(status_code=404, detail="pool not found")
    response = PoolResponse(message="this is the pool ", pool=PoolSchema.model_validate(pool))
    return response



@router.delete("/deletpool/{pool_id}")
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
