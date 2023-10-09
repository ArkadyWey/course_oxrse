class Academic:
    def __init__(self,name): ## dunder-init method - stands for double-underscore
        self.name = name
        self.papers = []


alice = Academic(name="Alice")
print(alice.name)