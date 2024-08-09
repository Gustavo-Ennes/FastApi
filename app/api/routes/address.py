from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.domain.schemas.address_schema import AddressSchema, AddressCreate
from app.infrastructure.database import get_db
from app.infrastructure.repositories.address import *

router = APIRouter()


@router.post("/address/", response_model=AddressCreate)
def api_create_address(address: AddressCreate, db: Session = Depends(get_db)):
    db_address = create_address(db, addressCreate=address)
    return create_address(db=db, addressCreate=db_address)


@router.get("/address/", response_model=list[AddressSchema])
def api_read_addresss(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    addresss = get_addresses(db, skip=skip, limit=limit)
    return addresss


@router.get("/addresss/{address_id}", response_model=AddressSchema)
def api_read_address(address_id: int, db: Session = Depends(get_db)):
    db_address = get_address(db, address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address
