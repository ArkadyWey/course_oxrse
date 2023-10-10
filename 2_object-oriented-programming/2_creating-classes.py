class Academic:
    def __init__(self,name): ## dunder-initialiser method - stands for double-underscore
                             # this sets up the initial configuration of the class and is called when 
                             # we create an instance of the class.
        self.name : str = name # attributes
        self.papers : list = []

    # self is the instance of the object
    # when instance is created, the value of the object is saved to the self variable

alice = Academic(name="Alice")
print(alice.name)