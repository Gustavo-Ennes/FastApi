from typing import TYPE_CHECKING, Optional
from pydantic import BaseModel, ConfigDict, field_validator

from ..validations.address import number_validator, postal_code_validator

if TYPE_CHECKING:
    from app.domain.schemas.company_schema import CompanySchema
    from app.domain.schemas.person_schema import PersonSchema


class AddressBase(BaseModel):
    street: str
    number: str
    neighborhood: str
    complement: Optional[str] = None
    city: str
    state: str
    country: str
    postal_code: str


class AddressCreate(AddressBase):

    @field_validator('postal_code')
    def postal_code_validation(cls, value, _):
        return postal_code_validator(value)

    @field_validator('number')
    def number_validation(cls, value, _):
        return number_validator(value)


class AddressSchema(AddressBase):
    id: int
    person_owner: Optional['PersonSchema'] = None
    company_owner: Optional['CompanySchema'] = None

    model_config = ConfigDict(from_attributes=True)
    
class AddressUpdate(BaseModel):    
    id: int
    street: Optional[str] = None
    number: Optional[str] = None
    neighborhood: Optional[str] = None
    complement: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None
    
    @field_validator('postal_code')
    def postal_code_validation(cls, value, _):
        return postal_code_validator(value) if value is not None else True

    @field_validator('number')
    def number_validation(cls, value, _):
        return number_validator(value) if value is not None else True
