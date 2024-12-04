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
        print("მოცემული მონაცემები არასწორია. გთხოვთ, შეიყვანოთ რიცხვები ხელახლა.")
        return get_input()

def show_menu():
    print("-" * 60)
    print("\n კ ა ლ კ უ ლ ა ტ ო რ ი \n")
    print("-" * 60 )  
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

            if operation == "1":
                print(f"\nპასუხი: {num1} + {num2} = {mimateba(num1, num2)}\n")
                print("-" * 60)
            elif operation == "2":
                print(f"პასუხი: {num1} - {num2} = {gamokleba(num1, num2)}\n")
                print("-" * 60)
            elif operation == "3":
                print(f"პასუხი: {num1} * {num2} = {gamravleba(num1, num2)}\n")
                print("-" * 60)
            elif operation == "4":
                print(f"პასუხი: {num1} / {num2} = {gakopa(num1, num2)}\n")
                print("-" * 60)
        else:
            print("\nარასწორი მოქმებდება! გთხოვთ ხელახლა შეიყვანოთ სასურველი ოპერაცია.")

main()
