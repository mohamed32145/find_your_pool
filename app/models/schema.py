from sqlalchemy import Column, Integer, String, ForeignKey, Table, TIMESTAMP, text
from  sqlalchemy.orm import relationship
from app.database  import Base


class Pool(Base):
    __tablename__ = 'pools'  # Define the table name

    id = Column(Integer, primary_key=True, index=True)
    length = Column(Integer)
    width = Column(Integer)
    depth = Column(Integer)
    my_braces = relationship("Bracelet", secondary= "bracelets_pools", back_populates="my_pools")
    my_manager = relationship("Manager", secondary="managers_pools", back_populates= "my_pools")

    def __repr__(self):
        return f"<Pool(length={self.length}, width={self.width}, depth={self.depth})>"



class Bracelet(Base):
    __tablename__ = 'bracelets'

    code = Column(Integer, primary_key=True, index = True)
    customer_name = Column(String)
    age = Column(Integer)
    register_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    my_pools = relationship("Pool", secondary="bracelets_pools", back_populates= "my_braces")

    def __repr__(self):
        return f" bracelet is [the code is {self.code}, the name is {self.customer_name} ,the age is {self.age}"

class Manager(Base):
    __tablename__= "managers"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    name = Column(String)
    salary = Column(Integer)
    my_pools = relationship("Pool", secondary="managers_pools", back_populates="my_manager")


bracelets_pools = Table(
    'bracelets_pools',
    Base.metadata,
    Column('bracelet_code', Integer, ForeignKey('bracelets.code'), primary_key=True),
    Column('pool_id', Integer, ForeignKey('pools.id'), primary_key=True)
)


managers_pools = Table(
    'managers_pools',
    Base.metadata,
    Column('manager_id', Integer, ForeignKey('managers.id'), primary_key=True),
    Column('pool_id', Integer, ForeignKey('pools.id'), primary_key=True)
)

