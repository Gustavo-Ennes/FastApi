from app.domain.models.address import AddressModel
from app.domain.schemas.address_schema import AddressCreate
from app.infrastructure.repositories.address import create_address
from ..fixture import db


def test_update_address(db):
    address_to_update = create_address(db['session'], AddressCreate(city="ilha solteira",
                                                                    complement="complemento",
                                                                    country="Brazil",
                                                                    neighborhood="Vila Rio",
                                                                    number="11",
                                                                    postal_code="12312322",
                                                                    state="São Paulo",
                                                                    street="Rua Filha da Puta de Almeida"
                                                                    ))
    response = db['client'].put(
        "/api/address",
        json={
            "id": f'{address_to_update.id}',
            "number": "222",
            "neighborhood": "bairro nobre",
            "country": "Cabo Verde",
            "postal_code": "44444444"
        })

    assert response.status_code == 200

    address_from_db = db['session'].query(
        AddressModel).filter_by(id=address_to_update.id).first()
    assert address_from_db.id is not None
    assert address_from_db.postal_code == "44444444"
    assert address_from_db.country == "Cabo Verde"
    assert address_from_db.neighborhood == "bairro nobre"

    assert address_from_db.city == "ilha solteira"
    assert address_from_db.state == "São Paulo"
    assert address_from_db.street == "Rua Filha da Puta de Almeida"


def test_update_address_add_complement(db):
    address_to_update = create_address(db['session'], AddressCreate(city="ilha solteira",
                                                                    country="Brazil",
                                                                    neighborhood="Vila Rio",
                                                                    number="11",
                                                                    postal_code="12312322",
                                                                    state="São Paulo",
                                                                    street="Rua Filha da Puta de Almeida"
                                                                    ))
    response = db['client'].put(
        "/api/address",
        json={
            "id": f'{address_to_update.id}',
            "complement": "novo complemento"
        })

    assert response.status_code == 200

    address_from_db = db['session'].query(
        AddressModel).filter_by(id=address_to_update.id).first()
    assert address_from_db.id is not None
    assert address_from_db.complement == "novo complemento"
    assert address_from_db.postal_code == "12312322"
    assert address_from_db.country == "Brazil"
    assert address_from_db.neighborhood == "Vila Rio"


def test_throw_when_number_is_letter_or_empty(db):
    address_to_update = create_address(db['session'], AddressCreate(city="ilha solteira",
                                                                    country="Brazil",
                                                                    neighborhood="Vila Rio",
                                                                    number="11",
                                                                    postal_code="12312322",
                                                                    state="São Paulo",
                                                                    street="Rua Filha da Puta de Almeida"
                                                                    ))
    response1 = db['client'].put(
        "/api/address",
        json={
            "id": f'{address_to_update.id}',
            "complement": "novo complemento",
            "number": "asS123"
        })
    response2 = db['client'].put(
        "/api/address",
        json={
            "id": f'{address_to_update.id}',
            "complement": "novo complemento",
            "number": ""
        })

    data1 = response1.json()
    data2 = response2.json()
    assert response1.status_code == 400
    assert response2.status_code == 400
    assert data1['detail'] == "Number must have only digits."
    assert data2['detail'] == "Number must have only digits."


def test_throw_when_postal_code_is_letter_or_wrong(db):
    address_to_update = create_address(db['session'], AddressCreate(city="ilha solteira",
                                                                    country="Brazil",
                                                                    neighborhood="Vila Rio",
                                                                    number="11",
                                                                    postal_code="12312322",
                                                                    state="São Paulo",
                                                                    street="Rua Filha da Puta de Almeida"
                                                                    ))
    response1 = db['client'].put(
        "/api/address",
        json={
            "id": f'{address_to_update.id}',
            "complement": "novo complemento",
            "postal_code": "12312312312"
        })
    response2 = db['client'].put(
        "/api/address",
        json={
            "id": f'{address_to_update.id}',
            "complement": "novo complemento",
            "postal_code": "132123sa"
        })

    data1 = response1.json()
    data2 = response2.json()
    assert response1.status_code == 400
    assert response2.status_code == 400
    assert data1['detail'] == "Postal code must be exactly 8 digits long."
    assert data2['detail'] == "Postal code must be exactly 8 digits long."


def test_throw_if_not_found(db):
    address_to_update = create_address(db['session'], AddressCreate(city="ilha solteira",
                                                                    complement="complemento",
                                                                    country="Brazil",
                                                                    neighborhood="Vila Rio",
                                                                    number="11",
                                                                    postal_code="12312322",
                                                                    state="São Paulo",
                                                                    street="Rua Filha da Puta de Almeida"
                                                                    ))
    response = db['client'].put(
        "/api/address",
        json={
            "id": '112'
        })

    assert response.status_code == 404

    address_from_db = db['session'].query(
        AddressModel).filter_by(id=address_to_update.id).first()
    assert address_from_db is not None

    data = response.json()
    assert response.status_code == 404
    assert data['detail'] == "Address not found."
