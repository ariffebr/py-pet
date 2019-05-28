from flask import Flask
from configs import app

from controllers import PetController

PetController.register(app)

if __name__ == '__main__':
    app.run()
