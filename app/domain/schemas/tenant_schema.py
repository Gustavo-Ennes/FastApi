from typing import List, Optional, TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
  from app.domain.schemas.company_schema import CompanySchema
  from app.domain.schemas.person_schema import PersonSchema


class TenantBase(BaseModel):
    pass


class TenantCreate(TenantBase):
    person_id: Optional[int]
    company_id: Optional[int]


class TenantSchema(TenantCreate):
    id: int
    person: 'PersonSchema'
    company: 'CompanySchema'
    is_active: bool
    annotations: List[str] = []

    class Config:
        from_attributes = True
