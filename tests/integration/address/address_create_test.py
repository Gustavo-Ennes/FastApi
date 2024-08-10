from app.domain.models.address import AddressModel
from ..fixture import db


def test_create_incomplete_address(db):
    response = db['client'].post(
        "/api/address",
        json={
            "street": "Rua",
            "number": "321",
            "neighborhood": "bairro",
            "city": "cidade",
            "state": "estado",
            "country": "país",
            "postal_code": "12312313"
        })

    assert response.status_code == 200
    data = response.json()
    assert data["street"] == "Rua"
    assert "id" in data

    # Verificar se o item foi salvo no banco de dados
    address_from_db = db['session'].query(
        AddressModel).filter_by(street="Rua").first()
    assert address_from_db.id is not None
    assert address_from_db.postal_code == "12312313"


def test_create_complete_address(db):
    response = db['client'].post(
        "/api/address",
        json={
            "street": "Rua",
            "number": "320",
            "complement": "complemento",
            "neighborhood": "bairro",
            "city": "cidade",
            "state": "estado",
            "country": "país",
            "postal_code": "12312313"
        })
    assert response.status_code == 200
    data = response.json()
    assert data["street"] == "Rua"
    assert "id" in data

    # Verificar se o item foi salvo no banco de dados
    address_from_db = db['session'].query(
        AddressModel).filter_by(number="320").first()
    assert address_from_db.id is not None
    assert address_from_db.postal_code == "12312313"
    assert address_from_db.complement == "complemento"


def test_throw_when_number_are_letters(db):
    response = db['client'].post(
        "/api/address",
        json={
            "street": "Rua",
            "number": "aa320",
            "complement": "complemento",
            "neighborhood": "bairro",
            "city": "cidade",
            "state": "estado",
            "country": "país",
            "postal_code": "12312313"
        })

    data = response.json()
    assert response.status_code == 400
    assert data['detail'] == "Number must have only digits."


def test_throw_when_postal_code_has_letters(db):
    response = db['client'].post(
        "/api/address",
        json={
            "street": "Rua",
            "number": "320",
            "complement": "complemento",
            "neighborhood": "bairro",
            "city": "cidade",
            "state": "estado",
            "country": "país",
            "postal_code": "cc312t13"
        })

    data = response.json()
    assert response.status_code == 400
    assert data['detail'] == "Postal code must be exactly 8 digits long."


def test_throw_when_postal_code_wrong_length(db):
    response1 = db['client'].post(
        "/api/address",
        json={
            "street": "Rua",
            "number": "320",
            "complement": "complemento",
            "neighborhood": "bairro",
            "city": "cidade",
            "state": "estado",
            "country": "país",
            "postal_code": "123"
        })
    response2 = db['client'].post(
        "/api/address",
        json={
            "street": "Rua",
            "number": "320",
            "complement": "complemento",
            "neighborhood": "bairro",
            "city": "cidade",
            "state": "estado",
            "country": "país",
            "postal_code": "123123123123123123"
        })

    data1 = response1.json()
    data2 = response2.json()
    assert response1.status_code == 400
    assert response2.status_code == 400
    assert data1['detail'] == "Postal code must be exactly 8 digits long."
    assert data2['detail'] == "Postal code must be exactly 8 digits long."
