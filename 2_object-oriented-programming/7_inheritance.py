# Inheritance is about IDENTITY
# x IS y
# For example, we say Academics ARE people 
# So one class can inherit attributes, methods, and properties from another 

class Paper:
    def __init__(self, title:str, date:int):
        self.title : str = title
        self.date : int  = date

    def __str__(self):
        return self.title

# Person is the superclass
class Person:
    def __init__(self, name:str):
        self.name : str = name
    
    def __str__(self):
        return self.name

# Academic is the subclass
class Academic(Person):
    def __init__(self, name):
        super().__init__(name) # call the __init__() method of the superclass since it's not called by default
        self.papers = []

    def write_paper(self, title:str, date:int):
        paper = Paper(title=title, date=date)
        self.papers.append(paper)
        return paper


bob   = Person(name="Bob") # bob is a person
alice = Academic(name="Alice") # alice is an academic

print(str(alice))
paper = alice.write_paper(title="Title of Alice's paper", date=1234) # alice has a name and can write papers
print(paper)

print(bob.name)
paper = bob.write_paper(title="Title of Bob's paper", date=5678) # bob has a name but cannot write papers

print(paper)
print(bob.papers)



# Composition vs inheritance: 
# When should we use each one? 
# Ask yourself: Does a class HAVE something or IS IT something? 
# If it HAS something, then use composition. 
# If a class IS something, then use inheritance. 
# If both are applicable, then use composition (because it's simpler)