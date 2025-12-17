from book import Book

library = [
    Book('Идиот', 'Достоевский Ф.М.'),
    Book('Анна Каренина', 'Толстой Л.Н.'),
    Book('Гранатовый браслет', 'Куприн А.И.')
]

for book in library:
    print(f"{book.title} - {book.author}")
