"""company model"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.infrastructure.database import Base


class CompanyModel(Base):
    """company model"""
    __tablename__ = "company"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cnpj = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    address_id = Column(Integer, ForeignKey("address.id"))
    address = relationship(
        "AddressModel", back_populates="company_owner", foreign_keys=[address_id])
    representant_id = Column(Integer, ForeignKey("person.id"))
    representant = relationship(
        "PersonModel", back_populates="company", foreign_keys=[representant_id])
    
    # can be a tenant
    tenant = relationship("TenantModel", back_populates="company")
