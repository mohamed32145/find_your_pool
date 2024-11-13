from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.database import get_db
from app.help_functions import delete_bracelets_by_code
from app.models.models import braceletResponse, braceletSchema, ConnectBraceletPoolResponse
from app.models.schema import Bracelet, Pool, Manager


router = APIRouter(
    prefix="/bracelet",
    tags=['Bracelet']


)


@router.post("/addbracelet", response_model= braceletResponse)
async def add_brac(customer_name: str, age: int, db: Session = Depends(get_db)):
    new_brac = Bracelet(customer_name=customer_name, age=age)
    db.add(new_brac)
    db.commit()
    db.refresh(new_brac)

    response = braceletResponse(bracelet = braceletSchema.model_validate(new_brac))

    return response



@router.delete("/deletabrac/{brac_code}")
async  def delete_brac(brac_code: int, db: Session = Depends(get_db)):
    brac = db.get(Bracelet, brac_code)

    if brac is None:
        raise HTTPException(status_code=404, detail="Bracelet not found")
    db.delete(brac)
    db.commit()

    delete_bracelets_by_code(brac_code, db)
    return {"detail": "Bracelet deleted successfully"}


@router.get("/showProfile/{brac_code}")
async  def show_profile(brac_code: int, db: Session = Depends(get_db)):
    brac = db.get(Bracelet, brac_code)






@router.post("/connect_bracelet_to_pool", response_model=ConnectBraceletPoolResponse)
async def connect_bracelet_to_pool(pool_id: int, bracelet_code: int, db: Session = Depends(get_db)):
    pool = db.get(Pool, pool_id)
    if pool is None:
        raise HTTPException(status_code=404, detail="pool not found")
    bracelet = db.get(Bracelet,bracelet_code)
    if bracelet is None:
        raise HTTPException(status_code=404, detail="bracelet not found")

    if bracelet not in pool.my_braces:
        pool.my_braces.append(bracelet)
        db.commit()

    return ConnectBraceletPoolResponse(
        message=f"Bracelet '{bracelet.customer_name}' connected to pool '{pool.id}'",
        pool_id=pool.id,
        bracelet_name= bracelet.customer_name
    )

