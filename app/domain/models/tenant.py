"""tenant model"""

from sqlalchemy import JSON, Boolean, Column, DateTime, Integer, ForeignKey, func
from sqlalchemy.orm import relationship

from app.infrastructure.database import Base


class TenantModel(Base):
    """tenant model"""
    __tablename__ = "tenants"

    id = Column(Integer, primary_key=True)
    person = relationship(
        "PersonModel", back_populates="tenant", uselist=False)
    company = relationship(
        "CompanyModel", back_populates="tenant", uselist=False)
    is_active = Column(Boolean, default=True)
    annotations = Column(JSON, default=[])
    created = Column(DateTime, server_default=func.now())
    updated = Column(DateTime, server_default=func.now(),
                     server_onupdate=func.now())
