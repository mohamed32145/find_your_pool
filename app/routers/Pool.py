from fastapi import Depends, HTTPException, APIRouter,status
from sqlalchemy.orm import Session
from app.database import get_db
from app.help_functions import delete_rows_by_pool_id, delete_pool_from_pool_manager_table,get_current_user
from app.models.models import PoolSchema, PoolResponse, ConnectBraceletManagerResponse
from app.models.schema import Pool, Manager

router = APIRouter(
    prefix="/pool",
    tags=['Pool']
)


@router.post("/add_pool", response_model= PoolResponse,status_code=status.HTTP_201_CREATED)
async def add_pool(length: float, width: float, depth: float,  db: Session = Depends(get_db)):
    new_pool = Pool(length=length, width=width, depth=depth)
    db.add(new_pool)
    db.commit()
    db.refresh(new_pool) # after this refresh new_pool will get the id which is generated automaticlly in postgre table
    response = PoolResponse(message="pool was added", pool=PoolSchema.model_validate(new_pool))
    return response

@router.get("/get_pool", response_model=PoolResponse)
async def get_pool(poolcode: int, db: Session = Depends(get_db), get_current_user: int =
                   Depends(get_current_user)):
    pool = db.get(Pool, poolcode)
    if pool is None:
        raise HTTPException(status_code=404, detail="pool not found")
    response = PoolResponse(message="this is the pool ", pool=PoolSchema.model_validate(pool))
    return response


@router.get("/show_my_manager")
async def show_manager(poolCode: int, db: Session = Depends(get_db)):
    pool = db.get(Pool, poolCode)
    if pool is None:
        raise HTTPException(status_code=404, detail="Pool not found")

    if pool.my_manager:
        return {
            "pool_id": pool.id,
            "manager": {
                "id": pool.my_manager.id,
                "name": pool.my_manager.name
            }
        }
    else:
        return {"detail": f"No manager yet for this pool with id {pool.id}"}


@router.get("/show_my_bracelets")
async  def show_bracelets(poolCode: int, db: Session = Depends(get_db)):
    pool = db.get(Pool, poolCode)
    if pool is None:
        raise HTTPException(status_code=404, detail="Pool not found")
    bracelets = [{"bars_code": brac.code, "name": brac.customer_name} for brac in pool.my_braces]
    return {
        "pool_id": pool.id,
        "bracelets": bracelets
    }


@router.delete("/delete_bracelet_from_pool")
async def delete_bracelet_from_pool(pool_id: int, bracelet_code: int, db: Session = Depends(get_db)):

    # Get the pool
    pool = db.get(Pool, pool_id)
    if pool is None:
        raise HTTPException(status_code=404, detail="Pool not found")

    # Find the bracelet in the pool's list of associated bracelets
    bracelet_to_remove = next((bracelet for bracelet in pool.my_braces if bracelet.code == bracelet_code), None)

    if bracelet_to_remove is None:
        raise HTTPException(status_code=404, detail="Bracelet not found in this pool")

    # Remove the bracelet from the pool
    pool.my_braces.remove(bracelet_to_remove)

    # Commit the changes
    db.add(pool)
    db.commit()
    db.refresh(pool)

    return {
        "message": f"Bracelet with ID {bracelet_code} has been removed from pool {pool_id}"
    }


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

@router.post("/connect_pool_to_manager",response_model= ConnectBraceletManagerResponse)
async def connect_bracelet_to_manager(pool_id: int, manager_id:int, db: Session = Depends(get_db)):
    pool = db.get(Pool, pool_id)
    if pool is None:
        raise HTTPException(status_code=404, detail="pool not found")
    manager = db.get(Manager,manager_id)
    if manager is None:
        raise HTTPException(status_code=404, detail="manager not found")

        # Check if the pool already has a manager
    if pool.my_manager is not None:
        return {"message": f"There is already a manager assigned to pool {pool.id}"}

        # Assign the Manager object to the Poo
    pool.my_manager = manager

    # Commit  changes to the database
    db.add(pool)
    db.commit()
    db.refresh(pool)


    return ConnectBraceletManagerResponse(message=f"Manager '{manager.name}' connected to pool '{pool.id}'",pool_id=pool.id,
        manager_name=manager.name
    )
