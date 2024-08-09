from typing import TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
  from app.domain.schemas.address_schema import AddressSchema
  from app.domain.schemas.person_schema import PersonSchema
  from app.domain.schemas.tenant_schema import TenantSchema


class CompanyBase(BaseModel):
    name: str
    cnpj: str
    phone: str
    email: str


class CompanyCreate(CompanyBase):
    address_id: int
    representant_id: int


class CompanySchema(CompanyCreate):
    id: int
    address: 'AddressSchema'
    representant: 'PersonSchema'
    tenant: 'TenantSchema'

    class Config:
        from_attributes = True
