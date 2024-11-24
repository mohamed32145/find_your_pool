from datetime import datetime
from pydantic import  BaseModel,EmailStr


class PoolSchema(BaseModel):
    length: int
    width: int
    depth: int

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
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
        from_attributes = True


class ManagerResponseWithoutSensitive(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr

    class Config:
        orm_mode = True





class braceletSchema(BaseModel):
    customer_name : str
    age : int
    register_at: datetime

    class Config:
        from_attributes = True


class braceletResponse(BaseModel):
    bracelet: braceletSchema
    class Config:
        orm_mode = True
        from_attributes = True

class ConnectBraceletManagerResponse(BaseModel):
    message: str
    pool_id: int
    manager_name: str

    class Config:
        orm_mode = True


class ConnectBraceletPoolResponse(BaseModel):
    message: str
    pool_id: int
    bracelet_name: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None