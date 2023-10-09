class Book:
    def __init__(self, name:str, author:str):
        self.name:str = name
        self.author:str = author
    
    def __str__(self):
        return self.name + " by " + self.author

    def __eq__(self,book):
        if self.name == book.name and self.author == book.author:
            equal = True
        else: 
            equal = False
        return equal

class Library:
    def __init__(self):
        self.books = []
    
    def __len__(self):
        return len(self.books)
    
    def __getitem__(self, index):
        return self.books[index]

    def add_book(self, name:str, author:str):
        book = Book(name=name,author=author)
        self.books.append(book)
        return book

    def by_author(self, author:str):
        """
        Return a sublist of self.books that are written by author.
        """
        books_by_author = []
        for book in self.books:
            if book.author == author:
                books_by_author.append(book)
            else: 
                pass
        
        if books_by_author == []:
            raise KeyError("Author does not exist")
        else: 
            pass
        
        return books_by_author

    @property
    def titles(self):
        titles = []
        for book in self.books:
            titles.append(book.name)
        return titles

    @property
    def authors(self):
        authors = []
        for book in self.books:
            authors.append(book.author)
        return authors
    
    def union(self, library):
        shared_books = []
        for book in self.books:
            for another_book in library.books:
                if book.__eq__(book=another_book) == True:
                    shared_books.append(book)
                else: 
                    pass
        library_union = Library()
        for book in shared_books:
            name = book.name
            author = book.author
            library_union.add_book(name=name,author=author)
        return library_union

library = Library()

library.add_book('My First Book', 'Alice')
library.add_book('My Second Book', 'Alice')
library.add_book('A Different Book', 'Bob')


print(len(library))

book = library[2]
print(book)

books = library.by_author('Alice')
for book in books:
    print(book)

print(library.titles)
print(library.authors)

another_library = Library()

another_library.add_book('My First Book', 'Alice')
another_library.add_book('My Second Book', 'Alice')

union_library = library.union(library=another_library)

for book in union_library.books:
    print(book.__str__())
#books = library.by_author('Carol')
#print(books)