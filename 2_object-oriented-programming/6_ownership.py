# Composition is about OWNERSHIP
# x has y
# For example, we say Academics HAVE Papers 
# So one class can own another class as an attribute 


class Paper:
    def __init__(self, title:str, date:int):
        self.title : str = title
        self.date : int  = date

    def __str__(self):
        return self.title
    
class Academic:
    def __init__(self, name:str):
        self.name : str = name
        self.papers = []

    def write_paper(self, title:str, date:int):
        paper = Paper(title=title, date=date)
        self.papers.append(paper)
        return paper


alice = Academic(name="Alice")

paper = alice.write_paper(title="Title of paper", date=1234)

print(paper)
print(alice.papers)
