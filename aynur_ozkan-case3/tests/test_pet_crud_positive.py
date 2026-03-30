import pytest
from api.pet_api import PetAPI


@pytest.fixture
def pet_api():
    return PetAPI()

#crud test one, create
def test_create_pet_positive(pet_api):
    payload = {
        "id": 987654,
        "name": "Karabas",
        "status": "available"
    }

    response = pet_api.create_pet(payload)

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 987654
    assert data["name"] == "Karabas"
    assert data["status"] == "available"

#verified that exist id should be return as success
def test_get_pet_positive(pet_api):
    pet_id = 987654
    response = pet_api.get_pet(pet_id)

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == pet_id

#crud test two, test to update
def test_update_pet_positive(pet_api):
    payload = {
        "id": 987654,
        "name": "KarabasUpdated",
        "status": "sold"
    }

    response = pet_api.update_pet(payload)

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "KarabasUpdated"
    assert data["status"] == "sold"

#crud test three, test to delete
def test_delete_pet_positive(pet_api):
    pet_id = 987654
    response = pet_api.delete_pet(pet_id)

    assert response.status_code == 200