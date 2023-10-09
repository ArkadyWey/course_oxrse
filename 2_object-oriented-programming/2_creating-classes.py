class Academic:
    def __init__(self,name): ## dunder-init method - stands for double-underscore
        self.name : str = name # attributes
        self.papers : list = []


alice = Academic(name="Alice")
print(alice.name)