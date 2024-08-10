"""company model"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.infrastructure.database import Base


class CompanyModel(Base):
    """company model"""
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    cnpj = Column(String)
    phone = Column(String)
    email = Column(String, unique=True)
    address = relationship(
        "AddressModel", back_populates="company_owner", uselist=False)
    representant_id = Column(Integer, ForeignKey("people.id"))
    representant = relationship(
        "PersonModel", back_populates="company", foreign_keys=[representant_id])

    # can be a tenant
    tenant_id = Column(Integer, ForeignKey("tenants.id"))
    tenant = relationship("TenantModel", back_populates="company", foreign_keys=[tenant_id])
