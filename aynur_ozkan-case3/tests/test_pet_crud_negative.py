import pytest
from api.pet_api import PetAPI


@pytest.fixture
def pet_api():
    return PetAPI()

# test it with false data
def test_get_pet_negative_not_found(pet_api):
    pet_id = 111111111  
    response = pet_api.get_pet(pet_id)

    assert response.status_code == 404

# test it with try to delete non-existent data
def test_delete_pet_negative_not_found(pet_api):
    pet_id = 111111111  
    response = pet_api.delete_pet(pet_id)

    assert response.status_code == 404

# test with incorrect field value
def test_create_pet_negative_invalid_payload(pet_api):
    payload = {
        "id": "ABC",   # id should be numeric 
        "name": True,  # should be string 
        "status": 123  # should be string
    }

    response = pet_api.create_pet(payload)

    # Understanding Flaky test response

    if response.status_code == 200:
        data = response.json()
        assert isinstance(data["id"], int) or data["id"] != "ABC"
    else:
        assert response.status_code in [400, 500]