"""person model"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.infrastructure.database import Base


class PersonModel(Base):
    """address model"""
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String, unique=True)
    cpf = Column(String)
    address_id = Column(Integer, ForeignKey("address.id"))
    address = relationship(
        "AddressModel", back_populates="person_owner", foreign_keys=[address_id])
    
    # can be a representant
    company = relationship(
        "CompanyModel", back_populates="representant")
    # can be a tenant
    tenant = relationship(
        "TenantModel", back_populates="person")
