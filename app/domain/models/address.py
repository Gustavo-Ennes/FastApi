"""address model"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.infrastructure.database import Base

class AddressModel(Base):
    """address model"""
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    street = Column(String)
    number = Column(String)
    neighborhood = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    country = Column(String)
    person_owner = relationship("PersonModel", back_populates="address")
    company_owner = relationship("CompanyModel", back_populates="address")   

