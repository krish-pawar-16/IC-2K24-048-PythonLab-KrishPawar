books = {
    "B1": {
        "title": "Python Basics",
        "author": "Rao",
        "copies": 2,
        "issued_to": [],
        "total_issued": 0
    },
    "B2": {
        "title": "Data Structures",
        "author": "Iyer",
        "copies": 1,
        "issued_to": [],
        "total_issued": 0
    },
    "B3": {
        "title": "Algorithms",
        "author": "Rao",
        "copies": 1,
        "issued_to": [],
        "total_issued": 0
    }
}


def add_book():

    isbn = input("Enter book ID: ").strip()

    if not isbn:
        print("Book ID cannot be empty.")
        return

    if isbn in books:

        try:
            copies = int(input("Enter additional copies: "))

            if copies <= 0:
                print("Copies must be greater than zero.")
                return

            books[isbn]["copies"] += copies
            print("Book copies updated successfully.")

        except ValueError:
            print("Enter a valid number.")

    else:

        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()

        if not title or not author:
            print("Title and author cannot be empty.")
            return

        try:
            copies = int(input("Enter number of copies: "))

            if copies <= 0:
                print("Copies must be greater than zero.")
                return

        except ValueError:
            print("Enter a valid number.")
            return

        books[isbn] = {
            "title": title,
            "author": author,
            "copies": copies,
            "issued_to": [],
            "total_issued": 0
        }

        print("Book added successfully.")


def issue_book():

    isbn = input("Enter book ID: ").strip()
    member = input("Enter member ID: ").strip()

    if isbn not in books:
        print("Book not found.")
        return

    if not member:
        print("Member ID cannot be empty.")
        return

    book = books[isbn]

    # Check whether the member already has this book
    if member in book["issued_to"]:
        print("This member already has this book.")
        return

    # Count books currently issued to the member
    member_books = sum(
        1 for data in books.values()
        if member in data["issued_to"]
    )

    if member_books >= 2:
        print("A member can borrow a maximum of two books.")
        return

    # Check book availability
    if book["copies"] <= 0:
        print("No copies available.")
        return

    book["copies"] -= 1
    book["issued_to"].append(member)
    book["total_issued"] += 1

    print("Book issued successfully.")


def return_book():

    isbn = input("Enter book ID: ").strip()
    member = input("Enter member ID: ").strip()

    if isbn not in books:
        print("Book not found.")
        return

    book = books[isbn]

    if member not in book["issued_to"]:
        print("This member has not borrowed this book.")
        return

    book["issued_to"].remove(member)
    book["copies"] += 1

    print("Book returned successfully.")


def search_book():

    isbn = input("Enter book ID: ").strip()

    if isbn in books:

        book = books[isbn]

        print("\nBook ID:", isbn)
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Available Copies:", book["copies"])
        print("Issued To:", book["issued_to"])

    else:
        print("Book not found.")


def reports():

    # Books grouped by author
    author_books = {}

    for isbn, book in books.items():

        author = book["author"]

        author_books.setdefault(author, []).append(
            book["title"]
        )

    print("\n1. Books by Author")

    for author, titles in author_books.items():
        print(author, ":", titles)

    # Books that are currently unavailable
    unavailable = [
        book["title"]
        for book in books.values()
        if book["copies"] == 0
    ]

    print("\n2. Unavailable Books")
    print(unavailable if unavailable else "None")

    # Books that have never been issued
    never_issued = [
        book["title"]
        for book in books.values()
        if book["total_issued"] == 0
    ]

    print("\n3. Books Never Issued")
    print(never_issued if never_issued else "None")

    # Members holding multiple books
    member_books = {}

    for isbn, book in books.items():

        for member in book["issued_to"]:

            member_books.setdefault(member, []).append(
                book["title"]
            )

    print("\n4. Members Holding Multiple Books")

    found = False

    for member, titles in member_books.items():

        if len(titles) > 1:
            print(member, ":", titles)
            found = True

    if not found:
        print("No member is holding multiple books.")


while True:

    print("\n===== LIBRARY RECORD SYSTEM =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        issue_book()

    elif choice == "3":
        return_book()

    elif choice == "4":
        search_book()

    elif choice == "5":
        reports()

    elif choice == "6":
        print("Exiting Library Record System.")
        break

    else:
        print("Invalid choice. Try again.")