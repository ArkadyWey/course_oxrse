# Class should have attributes, methods, and PROPERTIES.

# Properties are methods which behave like attributes
# To define a property, we need to use a DECORATOR function 
# This tells the class that the method we define should actually be a property
# Decorators are modified verision of the decorator design pattern - Erich Gamma 1994

class Academic:
    def __init__(self,name):
        self.name = name
        self.papers = []
    
    def write_paper(self,title,date):
        paper = {
            "title" : title,
            "date" : date
        }
        self.papers.append(paper)
        return paper
    
    @property # this is a decorator function called property which modifies teh behaviour o fthe following
    def last_paper(self): # properties are usually things that could start with GET so they're called getters in other languages    
        """
        Get last paper
        """
        return self.papers[-1]

    
alice = Academic(name="Alice")

alice.write_paper(title="first paper", date=1)
alice.write_paper(title="second paper", date=2)

last_paper = alice.last_paper
print(last_paper)