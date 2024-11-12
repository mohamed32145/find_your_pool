from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.database import get_db
from app.help_functions import delete_manager_by_id_from_manager_pool
from app.models.models import managerResponse, managerSchema
from app.models.schema import  Manager


router = APIRouter(
    prefix="/manager",
    tags=['Manager']
)

@router.post("/addmanager", response_model= managerResponse)
async def add_manager(name: str, age: int, salary: int, db: Session = Depends(get_db)):
    new_manager = Manager(name=name, age=age, salary=salary)
    db.add(new_manager)
    db.commit()
    db.refresh(new_manager)

    managerscema = managerResponse(manager= managerSchema.model_validate(new_manager))

    return managerscema


@router.delete("/deletmanager/{manager_id}")
async  def delete_brac(manager_id: int, db: Session = Depends(get_db)):
    mang = db.get(Manager ,manager_id)

    if mang is None:
        raise HTTPException(status_code=404, detail="manager not found")
    db.delete(mang)
    db.commit()
    delete_manager_by_id_from_manager_pool(manager_id, db)



    return {"detail": "mnager deleted successfully"}
