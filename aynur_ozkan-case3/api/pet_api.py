import requests


class PetAPI:
    BASE_URL = "https://petstore.swagger.io/v2/pet"

    def create_pet(self, payload):
        return requests.post(self.BASE_URL, json=payload)

    def get_pet(self, pet_id):
        return requests.get(f"{self.BASE_URL}/{pet_id}")

    def update_pet(self, payload):
        return requests.put(self.BASE_URL, json=payload)

    def delete_pet(self, pet_id):
        return requests.delete(f"{self.BASE_URL}/{pet_id}")