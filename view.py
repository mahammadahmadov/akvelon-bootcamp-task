from controller import Controller

name = input("Enter your name: ")
bottleType = input("Enter the type(plastic, glass etc.) of bottle: ")

controller = Controller(name, bottleType)
controller.checkInputs()
