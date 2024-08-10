from typing import TYPE_CHECKING, Optional
from pydantic import BaseModel, ConfigDict

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
    address: Optional['AddressSchema'] = None
    representant: Optional['PersonSchema'] = None
    tenant: Optional['TenantSchema'] = None

    model_config = ConfigDict(from_attributes=True)
