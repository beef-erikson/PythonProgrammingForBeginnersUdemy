class Book:
    def __init__(self, id: int, name: str, author: str):
        """Initialization of Book class.
        """
        self.id = id
        self.name = name
        self.author = author
        self.reviews = []

    def __repr__(self):
        """Representation of output when object is called.
        """
        return repr((self.id, self.name, self.author, self.reviews))

    def add_review(self, review: object) -> None:
        """Uses the supplied Review object and appends to self.reviews.
        """
        self.reviews.append(review)


class Review:
    def __init__(self, id: int, description: str, rating: float):
        """Initialization of Review class.
        """
        self.id = id
        self.description = description
        self.rating = rating

    def __repr__(self):
        """Representation of output when object is called.
        """
        return repr((self.id, self.description, self.rating))


# Creates and prints a book
book = Book(123, 'Object Orientated Programming with Python', 'Udemy Ranga')
print(book)

# Creates and adds reviews, printing final result
book.add_review(Review(10, 'Great Book!', 5))
book.add_review(Review(101, 'Awesome!', 4.5))
print(book)
