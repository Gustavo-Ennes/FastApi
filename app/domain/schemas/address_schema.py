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
