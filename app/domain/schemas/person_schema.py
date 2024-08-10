from typing import TYPE_CHECKING, Optional
from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from app.domain.schemas.address_schema import AddressSchema
    from app.domain.schemas.company_schema import CompanySchema
    from app.domain.schemas.tenant_schema import TenantSchema


class PersonBase(BaseModel):
    name: str
    email: str
    phone: str
    cpf: str


class PersonCreate(PersonBase):
    address_id: int


class PersonSchema(PersonCreate):
    id: int
    address: 'AddressSchema'
    company: Optional['CompanySchema'] = None
    tenant: Optional['TenantSchema'] = None

    model_config = ConfigDict(from_attributes=True)
