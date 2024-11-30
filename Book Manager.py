class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"სათაური: {self.title} | ავტორი: {self.author} | გამოშვების წელი: {self.year}, \n  "
    print("-" * 60)


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
         
        new_book = Book(title, author, year)
        
        if any(book.title == title and book.author == author and book.year == year for book in self.books):
            print("მსგავსი წიგნი სათაურით, ავტორით და გამოშვების წლით უკვე დამატებულია ბაზაში")
        # თუ წიგნი არსებობს ბაზაში დაბეჭდავს რომ  მსგავსი წიგნი სათაურით, ავტორით და თარიღით უკვე არსებობს    
        else:
            # თუკი წიგნი არარსებობს მსგავსი სათაურით ავტორით და გამოშვების წელით  დაემატოს სიას
            self.books.append(new_book)
            print(f"\nწიგნი '{title}' წარმატებით დაემატა ბაზაში.")

    def delete_book(self, title, author, year):
        #წიგნის წაშლა თუ კი შეყვანილი სათაური, ავტორი და გამოშვების თარიღი ემთხვევა ერთმანეთს წიგნი წაიშლება სიიდან
        book_to_delete = None
        for book in self.books:
            if book.title == title and book.author == author and book.year == year:
                book_to_delete = book
                break

        if book_to_delete:
            self.books.remove(book_to_delete)  #წიგნის წაშლა ლისტიდან
            print(f"\nწიგნი '{title}' წარმატებით წაიშალა.")
        else:
            print(f"\nწიგნი '{title}' ავტორის '{author}' და წლის '{year}' მიხედვით ვერ მოიძებნა.") # თუ კი ვერ მოიძებნა გამოიტანს ინფორმაციას რომ მსგავსი სახლით ავტორით და წელით წიგნი არ არსებობს

    def view_books(self):
        # ფუნქცია რომ გამოიტანოს ყველა წიგნი ბაზიდან
        if not self.books:
            print("წიგნები ჯერ არარის ბაზაში დამატებული.")
        else:
            for book in self.books:
                print(book)  # გამოიოტანს სათითაოდ ყველა წიგნს
     
    def search_book_by_title(self, title):
        # წიგნის ძებნა სათაურით
        found_books = [book for book in self.books if title.lower() in book.title.lower()]  # თუ კი შეყვანილი იქნება წიგნის სათაური დიდი ან პატარა ასოებით მაინც მოძებნის წიგნს თუა სიაში
        if found_books:
            for book in found_books:
                print(book)  
        else:
            print("მსგავსი სათაურით წიგნი არ მოიძებნა.")

    def search_book_by_year(self, year):
        # წიგნის ძებნა გამოშვების წლის მიხედვით
        found_books = [book for book in self.books if book.year == year]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print("წიგნი გამოშვების წლით არ მოიძებნა.")


def validate_input(prompt, data_type):
    # ვალიდაციის ფუნქცია რათა მოხდეს შემოწმება მომხმარებლის მიერ შეყვანი ინფორმაციის კორექტულად შეყვანისა
    while True:
        user_input = input(prompt)
        if data_type == "string":
            if user_input.strip(): 
                return user_input
   # თუ კი მომხმარებელი სათაურს და ავტორს სწროად შეიყვანს დაუბრუნებს user_input-ს და გადავა შემდგომ წლის შესაყვანად არაფერს შეიყვანს 
   # ხოლო თუ კი მომხმარებელი ცარიელს დატოვებს სათაურს ან ავტორს დააბეჭდინებს  print("შესაყვანი ველი არ უნდა იყოს ცარიელი. გთხოვთ შეავსოთ ველი.") და ხელახლა მოთხოვს ინფორმაციის შეყვანას           
            else:
                print("შესაყვანი ველი არ უნდა იყოს ცარიელი. გთხოვთ შეავსოთ ველი.")
        elif data_type == "year":
            # ახდენს თარიღის შეყვანის ვალიდაციას თუ კი შესაყვანი ინფორმაცია არის რიცხვი და ოთხნიშნა, მაშინ იგი დაამატებს ბაზაში თუარადა დაააბეჭდნებს print("შესაყვანი წელი უნდა იყოს ოთხნიშნა ციფრი.")
            if user_input.isdigit() and len(user_input) == 4:
                return user_input
            else:
                print("შესაყვანი წელი უნდა იყოს ოთხნიშნა ციფრი.")
        else:
            return user_input

#მპროგრამის მთაბარი მენიუ User Interface
def main():
    manager = BookManager()  

    while True:
        print("-" * 60)
        print("\n1. წიგნის დამატება")
        print("2. წიგნების ჩამონათვალი")
        print("3. წიგნის მოძებნა სათაურით ან გამოშვების წლის მიხედვით")
        print("4. წიგნის წაშლა")
        print("5. პროგრამიდან გამოსვლა")
        print("-" * 60)
        choice = input("აირჩიეთ სასურველი მოქმედება: ")
        print("-" * 60)

        if choice == '1':
            # წიგნის დამატება შესაყვანია სათაური ავტორი დაა წიგნის გამოშვების თარიღი
            title = validate_input("შეიყვანეთ წიგნის სათაური: ", "string")
            author = validate_input("შეიყვანეთი წიგნის ავტორი: ", "string")
            year = validate_input("შეიყვანეთ გამოცემის წელი: ", "year")
            manager.add_book(title, author, year)  
        elif choice == '2':
            #ყველა წიგნის ჩამონათვალის ნახვა
            print("\nწიგნების სია:" "\n")
            manager.view_books()  
        elif choice == '3':
            print("-" *60)
            search_type = input("აირჩიეთ როგორ გსურთ წიგნის მოძებნა:" "\n" "1 - წიგნის ძიება სათაურით" "\n" "2 - წიგნის ძიება გამოშვების წლის მიხედვით" "\n" ":")
            print("-" *60)

            while True :
                if search_type == '1':
                    title = input("შეიყვანეთ წიგნის სათაური: ")
                    print("\nძიების შედეგი:")
                    manager.search_book_by_title(title)
                    break
                elif search_type == '2':
                    year = input("შეიყვანეთ გამოშვების წელი: ")
                    print("\nძიების შედეგი:")
                    manager.search_book_by_year(year)
                    break
                else:
                    print("არასწორი არჩევანი. გთხოვთ შეიყვანოთ სწორი მონაცემები" "\n","-"*60)
                    search_type = input("აირჩიეთ როგორ გსურთ წიგნის მოძებნა:" "\n" "1 - წიგნის ძიება სათაურით" "\n" "2 - წიგნის ძიება გამოშვების წლის მიხედვით" "\n" ":")
        elif choice == '4':
            # წიგნის წაშლა
            title = validate_input("შეიყვანეთ წიგნის სათაური, რომ წაშალოთ: ", "string")
            author = validate_input("შეიყვანეთ ავტორი: ", "string")
            year = validate_input("შეიყვანეთ წიგნის გამოშვების წელი: ", "year")
            manager.delete_book(title, author, year)  # წიგნის წასაშლელად საჭიროა ზუსტად იქნას შეყვანილი წიგნის სათაური, ავტორი და გამოშვების წელი.
        elif choice == '5':
            print("პროგრამიდან გამოსვლა.")
            break 
        else:
            print("მონაცემები არასწორად იქნა შეყვანილი. გთხოვთ შეიყვანოთ სწორი პარამეტრი.")  

main()
