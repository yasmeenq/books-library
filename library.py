#Build a library management system using dictionaries 
#where the keys are book titles and the values are dictionaries 
#containing information about each book (e.g., author, genre, publication year).

library = {
            "the night circus":{"author": "Erin Morgenstern",
                                "genre": "Fantasy",
                                "publication year": 2011
                                },
            
            "1984": {"author": "George Orwell",
                    "genre": "Dystopian",
                    "publication year": 1949
            },

            "the martian":{"author": "Andy Weir",
                    "genre": "Science Fiction",
                    "publication year": 2011
            } 
}
print("Library Books: ")
for book, info in library.items():
    print(f"{book}:{info} \n")
    

action = input("Enter 'a' to add a book, 'd' to display book info, or 'r' to remove a book: ")

#add a new book
if action == 'a':
    new_book = str(input("enter a new book name: "))
    library[new_book] = {"author":"", "genre":"", "publication year":0}
    author = str(input("enter author name: "))
    genre = str(input("enter genre: "))
    year = int(input("enter publication year"))
    library[new_book]["author"] = author
    library[new_book]["genre"] = genre
    library[new_book]["publication year"] = year
    print()
    print("Book Added Successfully! \n")
    print("Library Books: ")
    for book, info in library.items():
        print(f"{book}:{info} \n")

#display a book:
if action == 'd':
    book_to_show = str(input("enter a book title: ")).lower().strip()

    if book_to_show in library:
        book_info = library[book_to_show]
        print(f"Title: {book_to_show}")
        for key, value in book_info.items():
            print(f"{key.capitalize()}: {value}")

    else:
        print("book not found")

#remove a book
if action == 'r':
    book_to_delete = str(input("enter book name: ")).lower().strip()
    if book_to_delete in library:
        del library[book_to_delete]
        print()
        print("Deleted! \n")
        print("Library Books: ")
        for book, info in library.items():
            print(f"{book}:{info} \n")
    else:
        print("book not found in library")    