from app.domain.models.address import AddressModel
from app.domain.schemas.address_schema import AddressCreate
from app.infrastructure.repositories.address import create_address
from ..fixture import db


def test_delete_address(db):
    address_to_delete = create_address(db['session'], AddressCreate(city="ilha solteira",
                                                                    complement="complemento",
                                                                    country="Brazil",
                                                                    neighborhood="Vila Rio",
                                                                    number="11",
                                                                    postal_code="12312322",
                                                                    state="São Paulo",
                                                                    street="Rua Filha da Puta de Almeida"
                                                                    ))
    response = db['client'].delete(
        f"/api/address/{address_to_delete.id}")

    assert response.status_code == 200

    address_from_db = db['session'].query(
        AddressModel).filter_by(id=address_to_delete.id).first()
    assert address_from_db is None


def test_throw_if_not_found(db):
    address_to_delete = create_address(db['session'], AddressCreate(city="ilha solteira",
                                                                    complement="complemento",
                                                                    country="Brazil",
                                                                    neighborhood="Vila Rio",
                                                                    number="11",
                                                                    postal_code="12312322",
                                                                    state="São Paulo",
                                                                    street="Rua Filha da Puta de Almeida"
                                                                    ))
    response = db['client'].delete(
        f"/api/address/12123")

    assert response.status_code == 404

    address_from_db = db['session'].query(
        AddressModel).filter_by(id=address_to_delete.id).first()
    assert address_from_db is not None

    data = response.json()
    assert response.status_code == 404
    assert data['detail'] == "Address not found."
