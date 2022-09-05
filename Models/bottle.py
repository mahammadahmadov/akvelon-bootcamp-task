class Bottle:
    def __init__(self, type=""):
         self._type = type

    # getter method
    def get_type(self):
        return self._type

    # setter method
    def set_type(self, type):
        self._type = type
