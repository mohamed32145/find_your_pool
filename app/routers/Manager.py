from fastapi import Depends, HTTPException, APIRouter,status
from sqlalchemy.orm import Session
from app.database import get_db
from app.help_functions import delete_manager_by_id_from_manager_pool
from app.models.models import  managerSchema, ManagerResponseWithoutSensitive
from app.models.schema import  Manager
from app.help_functions import hash





router = APIRouter(
    prefix="/manager",
    tags=['Manager']
)



@router.post("/addmanager", response_model= ManagerResponseWithoutSensitive,status_code=status.HTTP_201_CREATED)
async def add_manager(name: str, age: int, salary: int,email: str, password: str ,db: Session = Depends(get_db)):
    hashed_password = hash(password)
    new_manager = Manager(name=name, age=age, salary=salary, email= email, password= hashed_password)
    db.add(new_manager)
    db.commit()
    db.refresh(new_manager)

    manager_data = managerSchema.model_validate(new_manager)

    # Exclude sensitive fields from the response
    manager_data_dict = manager_data.model_dump(exclude={"salary", "password"})
    #this line was added to make sure that id is in the final dictionary
    manager_data_dict['id'] = new_manager.id

    return ManagerResponseWithoutSensitive(**manager_data_dict)


@router.delete("/deletmanager/{manager_id}")
async  def delete_brac(manager_id: int, db: Session = Depends(get_db)):
    mang = db.get(Manager ,manager_id)

    if mang is None:
        raise HTTPException(status_code=404, detail="manager not found")
    db.delete(mang)
    db.commit()
    delete_manager_by_id_from_manager_pool(manager_id, db)

    return {"detail": "mnager deleted successfully"}

@router.get("/manager_pools/{manager_id}")
async def manager_pools(manager_id: int, db: Session = Depends(get_db)):
    manager = db.get(Manager, manager_id)
    if manager is None:
        raise HTTPException(status_code=404, detail="Manager not found")

    pools = [{"id": pool.id, "length": pool.length, "width": pool.width, "depth": pool.depth} for pool in manager.my_pools]
    return {
        "manager_id": manager.id,
        "manager_name": manager.name,
        "pools": pools
    }
