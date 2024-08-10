from app.domain.models.address import AddressModel
from app.domain.schemas.address_schema import AddressCreate
from app.infrastructure.repositories.address import create_address
from ..fixture import db


def test_get_addresses(db):
    address1 = create_address(db['session'], AddressCreate(city="ilha solteira",
                                                                    complement="complemento",
                                                                    country="Brazil",
                                                                    neighborhood="Vila Rio",
                                                                    number="11",
                                                                    postal_code="12312322",
                                                                    state="São Paulo",
                                                                    street="Rua Filha da Puta de Almeida"
                                                                    ))
    address2 = create_address(db['session'], AddressCreate(city="selvíria",
                                                                    complement="complemento",
                                                                    country="Brazil",
                                                                    neighborhood="véstia",
                                                                    number="112",
                                                                    postal_code="12312122",
                                                                    state="São Paulo",
                                                                    street="Rua 15"
                                                                    ))
    response = db['client'].get(
    "/api/address/")

    data = response.json()
    assert response.status_code == 200
    assert len(data) == 2
    assert data[0]['city'] == address1.city
    assert data[1]['city'] == address2.city
    
    
def test_get_address(db):
    address = create_address(db['session'], AddressCreate(city="ilha solteira",
                                                                    complement="complemento",
                                                                    country="Brazil",
                                                                    neighborhood="Vila Rio",
                                                                    number="11",
                                                                    postal_code="12312322",
                                                                    state="São Paulo",
                                                                    street="Rua Filha da Puta de Almeida"
                                                                    ))    
    response = db['client'].get(
    f"/api/address/{address.id}")

    data = response.json()
    assert response.status_code == 200
    assert data['city'] == "ilha solteira"
    assert data['state'] == 'São Paulo'
    
def test_throw_when_not_found(db):
    address = create_address(db['session'], AddressCreate(city="ilha solteira",
                                                                    complement="complemento",
                                                                    country="Brazil",
                                                                    neighborhood="Vila Rio",
                                                                    number="11",
                                                                    postal_code="12312322",
                                                                    state="São Paulo",
                                                                    street="Rua Filha da Puta de Almeida"
                                                                    ))    
    response = db['client'].get(
    "/api/address/666")

    data = response.json()
    assert response.status_code == 404
    assert data['detail'] == "Address not found."
    
    
    