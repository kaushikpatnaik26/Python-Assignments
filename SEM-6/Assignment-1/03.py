class Chapter:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

class Book:
    def __init__(self, title):
        self.title = title
        self.chapters = []

    def add_chapter(self, chapter):
        self.chapters.append(chapter)

    def get_total_pages(self):
        return sum(chapter.pages for chapter in self.chapters)

book = Book("Maths")

book.add_chapter(Chapter("Matrix", 30))
book.add_chapter(Chapter("Trigo", 50))
book.add_chapter(Chapter("Integration", 40))

print(f"Total pages in '{book.title}': {book.get_total_pages()}")
