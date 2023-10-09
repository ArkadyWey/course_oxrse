class Academic:
    def __init__(self, name):
        self.name : str = name # attributes are things that a class HAS
        self.papers : list = []

    def write_paper(self,title,date): # methods are things that a class can DO
        """
        Add a dictionary containing name and date 
        of paper to self.papers.
        """
        paper = {
            "title":title,
            "date":date
        }
        self.papers.append(paper)
        return paper

alice = Academic(name="Alice")
print(alice.name)

alice.write_paper(title="A new paper", date="Right Now")
print(alice.papers)
