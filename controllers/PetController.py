from flask import jsonify, request
from flask_classful import FlaskView, route

from dao import PetDao
from models import PetModel


class PetController(FlaskView):
    route_base = "/pet"

    petDao = PetDao()

    @route("/<int:id>", methods=['GET'])
    def find_pet(self, id):
        result = self.petDao.FindById(id)
        return jsonify(result)

    @route("/all", methods=['GET'])
    def get_all(self):
        res = self.petDao.GetAll()
        return jsonify(res)

    @route("/register", methods=['POST'])
    def register_pet(self):
        req = request.get_json()

        pet = PetModel()
        pet.name = req["name"]
        pet.age = req["age"]
        pet.owner = req["owner"]
        pet.photo = req["photo"]

        res = self.petDao.Save(pet)

        return jsonify(res)

    @route("/update/<int:id>", methods=['PUT'])
    def update_pet(self, id):
        req = request.get_json()

        pet = PetModel()
        pet.name = req["name"]
        pet.age = req["age"]
        pet.owner = req["owner"]
        pet.photo = req["photo"]

        res = self.petDao.Update(id, pet)
        return jsonify(res)

    @route("/delete/<int:id>", methods=['DELETE'])
    def delete(self, id):
        res = self.petDao.Delete(id)

        return jsonify(res)
