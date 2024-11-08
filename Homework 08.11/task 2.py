# Створіть клас, який описує відгук до книги. Додайте до класу книги поле – список відгуків. 
# Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї. 

class Review:
    def __init__(self, reviewer, text, rating):
        self.reviewer = reviewer
        self.text = text
        self.rating = rating

    def __str__(self):
        return f"{self.reviewer} rated {self.rating}/5: {self.text}"


class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)


    def __str__(self):
        book_info = f"'{self.title}' by {self.author} ({self.year}) - Genre: {self.genre}"
        if self.reviews:
            reviews_info = "\n".join(map(str, self.reviews))
        else:
            reviews_info = " No reviews yet."
        return f"{book_info}\n{reviews_info}"


book1 = Book("George Orwell", "1984", 1949, "Dystopian")
review1 = Review("Alice", "An eye-opening dystopian novel.", 5)
review2 = Review("Bob", "A bit too dark for my taste, but well-written.", 4)

book1.add_review(review1)
book1.add_review(review2)

print(book1)