from typing import TYPE_CHECKING
from pydantic import BaseModel, field_validator

from ..validations.address import number_validator, postal_code_validator

if TYPE_CHECKING:
    from app.domain.schemas.company_schema import CompanySchema
    from app.domain.schemas.person_schema import PersonSchema


class AddressBase(BaseModel):
    street: str
    number: str
    neighborhood: str
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
    person_owner: 'PersonSchema'
    company_owner: 'CompanySchema'

    class Config:
        from_attributes = True
