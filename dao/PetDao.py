import datetime

from configs import db
from models import PetModel, PetSchema


class PetDao:
    petSchema_many = PetSchema(many=True, strict=True)
    petSchema = PetSchema(strict=True)

    def __init__(self):
        pass

    def GetAll(self):
        allPet = PetModel.query.all()

        result = self.petSchema_many.dump(allPet)
        return result.data

    def FindById(self, id):

        if type(id) is not int:
            return None

        pet = PetModel.query.get(id)

        result = self.petSchema.dump(pet)
        return result.data

    def Save(self, petData):

        if type(petData) is not PetModel:
            return None

        petData.createdAt = datetime.datetime.now()
        db.session.add(petData)
        db.session.commit()

        result = self.petSchema.dump(petData)

        return result.data

    def Update(self, id, petData):

        if type(id) is not int:
            return None

        if type(petData) is not PetModel:
            return None

        currentPet = PetModel.query.filter_by(id=id).first()

        if not currentPet:
            return None

        if petData.name:
            currentPet.name = petData.name

        if petData.owner:
            currentPet.owner = petData.owner

        if petData.age:
            currentPet.age = petData.age

        if petData.photo:
            currentPet.photo = petData.photo

        db.session.commit()

        result = self.petSchema.dump(currentPet)
        return result.data

    def Delete(self, id):

        if type(id) is not int:
            return None

        pet = PetModel.query.filter_by(id=id).delete()
        db.session.commit()
        result = self.petSchema.dump(pet)

        return result.data
