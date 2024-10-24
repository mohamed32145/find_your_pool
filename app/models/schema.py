from sqlalchemy import Column, Integer
from app.database  import Base  # Assuming you have a Base defined in your database module

class Pool(Base):
    __tablename__ = 'pools'  # Define the table name

    id = Column(Integer, primary_key=True, index=True)
    length = Column(Integer)
    width = Column(Integer)
    depth = Column(Integer)
    manager_id = Column(Integer)  # Foreign key to manager if needed

    def __repr__(self):
        return f"<Pool(length={self.length}, width={self.width}, depth={self.depth}, manager_id={self.manager_id})>"