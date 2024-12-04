def mimateba(x, y):
    return x + y

def gamokleba(x, y):
    return x - y

def gamravleba(x, y):
    return x * y

def gakopa(x, y):
    if y != 0:
        return x / y
    else:
        return "ნულზე გაყოფა არ შეიძლება."

def get_input():
    try:
        num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
        num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
        return num1, num2
    except ValueError:
        print("მოცემული მონაცემები არასწორია. გთხოვთ, შეყაროთ რიცხვები.")
        return None, None

def show_menu():
    print("\nკალკულატორი\ ") 
    print("1. დამატება (+) - ორ რიცხვს დავამატებთ.")
    print("2. გამოკლება (-) - პირველ რიცხვს მეორე რიცხვით გამოვაკლავთ.")
    print("3. გამრავლება (*) - ორ რიცხვს გავამრავლებთ.")
    print("4. გაყოფა (/) - პირველ რიცხვს მეორე რიცხვზე დავყოთ.")
    print("5. გამოსვლა - პროგრამის დასრულება.")

def main():
    while True:
        show_menu()
        operation = input("\nაირჩიეთ ოპერაცია (1-5): ")

        if operation == "5":
            print("პროგრამა დასრულდა.")
            break
        
        if operation in ["1", "2", "3", "4"]:
            num1, num2 = get_input()
            
            if num1 is None or num2 is None:
                continue

            if operation == "1":
                print(f"შედეგი: {mimateba(num1, num2)}")
            elif operation == "2":
                print(f"შედეგი: {gamokleba(num1, num2)}")
            elif operation == "3":
                print(f"შედეგი: {gamravleba(num1, num2)}")
            elif operation == "4":
                print(f"შედეგი: {gakopa(num1, num2)}")
        else:
            print("არასწორი მოქმებდება! გთხოვთ ხელახლა შეიყვანოთ სასურველი ოპერაცია.")

main()
