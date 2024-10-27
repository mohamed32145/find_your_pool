from sqlalchemy import Column, Integer, String
from app.database  import Base  # Assuming you have a Base defined in your database module

class Pool(Base):
    __tablename__ = 'pools'  # Define the table name

    id = Column(Integer, primary_key=True, index=True)
    length = Column(Integer)
    width = Column(Integer)
    depth = Column(Integer)
    manager_id= Column(Integer)  # Foreign key to manager if needed

    def __repr__(self):
        return f"<Pool(length={self.length}, width={self.width}, depth={self.depth}, manager_id={self.manager_id})>"



class Bracelet(Base):
    __tablename__ = 'bracelets'

    code = Column(Integer, primary_key=True, index = True)
    customer_name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f" bracelet is [the code is {self.code}, the name is {self.customer_name} ,the age is {self.age}"

class Manager(Base):
    __tablename__= "managers"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    name = Column(String)
    salary = Column(Integer)





