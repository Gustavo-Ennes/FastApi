from .address import AddressModel
from .company import CompanyModel
from .tenant import TenantModel
from .person import PersonModel
from .user import UserModel


models = {
    'Address': AddressModel,
    'Company': CompanyModel,
    'Person': PersonModel,
    'Tenant': TenantModel,
    'User': UserModel
}
