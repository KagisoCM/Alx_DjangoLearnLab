# relationship_app/query_samples.py

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Set up Django environment so this script can be run standalone
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "J.K. Rowling"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"\nBooks by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with name: {author_name}")

# 2. List all books in a specific library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"\nBooks in {library_name}:")
    for book in books_in_library:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"No library found with name: {library_name}")

# 3. Retrieve the librarian for a specific library
try:
    librarian = Librarian.objects.get(library__name=library_name)
    print(f"\nLibrarian at {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian found for library: {library_name}")
