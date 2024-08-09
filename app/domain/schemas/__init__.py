from .address_schema import AddressSchema
from .company_schema import CompanySchema
from .person_schema import PersonSchema
from .tenant_schema import TenantSchema

AddressSchema.model_rebuild()
CompanySchema.model_rebuild()
PersonSchema.model_rebuild()
TenantSchema.model_rebuild()
