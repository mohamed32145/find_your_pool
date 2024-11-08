from pydantic import  BaseModel

class PoolSchema(BaseModel):
    length: int
    width: int
    depth: int
    manager_id: int

    class Config:
        orm_mode = True
        from_attributes = True

class PoolResponse(BaseModel):
    message: str
    pool: PoolSchema

    class Config:
        orm_mode = True

class managerSchema(BaseModel):
    age: int
    name: str
    salary: int

    class Config:
        orm_mode = True
        from_attributes = True


class managerResponse(BaseModel):
    manager : managerSchema

    class Config:
        orm_mode = True



class braceletSchema(BaseModel):
    customer_name : str
    age : int

    class Config:
        from_attributes = True


class braceletResponse(BaseModel):
    bracelet: braceletSchema
    class Config:
        orm_mode = True
        from_attributes = True

