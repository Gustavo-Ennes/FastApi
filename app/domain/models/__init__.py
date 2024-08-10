from app.infrastructure.database import Base
from .address import AddressModel
from .company import CompanyModel
from .tenant import TenantModel
from .person import PersonModel
from .user import UserModel


Address = AddressModel
Company = CompanyModel
Tenant = TenantModel
Person = PersonModel
User = UserModel
metadata = Base.metadata
