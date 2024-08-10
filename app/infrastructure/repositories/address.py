from sqlalchemy.orm import Session

from app.domain.schemas.address_schema import AddressCreate
from app.domain.models import AddressModel


def get_address(db: Session, address_id: int):
    return db.query(AddressModel).filter(AddressModel.id == address_id).first()


def get_addresses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AddressModel).offset(skip).limit(limit).all()


def create_address(db: Session, addressCreate: AddressCreate):
    db_address = AddressModel(street=addressCreate.street, number=addressCreate.number, neighborhood=addressCreate.neighborhood, complement=addressCreate.complement,
                              city=addressCreate.city, state=addressCreate.state, country=addressCreate.country, postal_code=addressCreate.postal_code)
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address
