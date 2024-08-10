"""address model"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.infrastructure.database import Base


class AddressModel(Base):
    """address model"""
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    street = Column(String)
    number = Column(String)
    neighborhood = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    country = Column(String)
    complement = Column(String, nullable=True)
    person_id = Column(Integer, ForeignKey("people.id"))
    person_owner = relationship("PersonModel", back_populates="address", foreign_keys=[person_id])
    company_id = Column(Integer, ForeignKey("companies.id"))
    company_owner = relationship("CompanyModel", back_populates="address", foreign_keys=[company_id])
