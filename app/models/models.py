from pydantic import  BaseModel

class PoolSchema(BaseModel):
    length: int
    width: int
    depth: int
    manager_id: int

    class Config:
        orm_mode = True

class PoolResponse(BaseModel):
    message: str
    pool: PoolSchema

    class Config:
        orm_mode = True
