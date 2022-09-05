from Models.man import Man
from Models.bottle import Bottle

class Controller:

    def __init__(self, name, bottleType):
        person = Man()
        bottle = Bottle()
        person.set_name(name)
        bottle.set_type(bottleType)
        self.personName = person.get_name()
        self.bottleType = bottle.get_type()


    def checkInputs(self):
        if (self.personName!="" and self.bottleType!=""):
            print(self.personName, "drinks water from", self.bottleType, "bottle")
        else:
            print("Please enter valid inputs")
