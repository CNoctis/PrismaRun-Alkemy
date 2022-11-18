from sqlalchemy import Column, String, Integer
from sqlalchemy import Column
from db import Base

class Customer(Base):
    """Modelo de la tabla info_client"""
    __tablename__ = 'info_client'
    
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    address = Column(String)
    zip_code = Column(String)
    id = Column(Integer, primary_key= True)
    
    def __init__(self, name: str, age: int, email: str, address: str, zip_code : str) -> None:
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.zip_code = zip_code

    def __repr__(self) -> str:
        return "<Customer(name='%s', age='%s', email='%s', address='%s', zip_code='%s',)>" %(self.name, self.age, self.email, self.address, self.zip_code)
