class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"სათაური: {self.title}, ავტორი: {self.author}, გამოშვების წელი: {self.year}"


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)
        print(f"წიგნი  '{title}' წარმატებით დაემატა.")

    def view_books(self):
        if not self.books:
            print("წიგნები ჯერ არარის ბაზაში დამატებული.")
        else:
            for book in self.books:
                print(book)

    def search_book_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print("მსგავსი სათაურით წიგნი არ მოიძებნა.")


def validate_input(prompt, data_type):
    while True:
        user_input = input(prompt)
        if data_type == "string":
            if user_input.strip(): #თუ ცარიელ ველს შეიყვანს  დააბეჭდინოს რომ ველი არ უნდა იყოს ცარიელი
                return user_input
            else:
                print("შესაყვანი ველი არ უნდა იყოს ცარიელი. გთხოვთ შეავსოთ ველი.")
        return user_input


def main():
    manager = BookManager()

    while True:
        print("\n1. წიგნის დამატება")
        print("2. წიგნების ჩამონათვალი")
        print("3. წიგნის მოძებნა სათაურით")
        print("4. პროგრამიდან გამოსვლა")
        choice = input("აირჩიეთ სასურველი მოქმედება: ")

        if choice == '1':
            title = validate_input("შეიყვანეთ წიგნის სათაური: ", "string")
            author = validate_input("შეიყვანეთი წიგნის ავტორი: ", "string")
            year = validate_input("შეიყვანეთ გამოცემის წელი: ", "year")
            manager.add_book(title, author, year)
        elif choice == '2':
            print("\nწიგნების სია:")
            manager.view_books()
        elif choice == '3':
            search_title = validate_input("შეიყვანეთ წიგნის სათაური: ", "string")
            print("\nძიების რეზულტატი:")
            manager.search_book_by_title(search_title)
        elif choice == '4':
            print("პროგრამიდან გამოსვლა.")
            break
        else:
            print("არასწორი მოქმედება. გთხოვთ სცადოთ ხელახლა.")

main()
