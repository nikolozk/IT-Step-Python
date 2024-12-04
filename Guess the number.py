import random
import time

# თამშის ტექსტის გამოტანა ანიმაციურად 
satauri = "თ ა მ ა შ ი   გ ა მ ო ი ც ა ნ ი  რ ი ც ხ ვ ი \n"
for a in satauri:
    print(a, end="", flush=True)
    time.sleep(0.1)
print("თამშის პირობაა რომ შეიყვანოთ სასურველი დიაპაზონი მთელი რიცხვებით\nლთამაში გაგრძლედება მანამ სანამ არ გამოიცნობთ კომპიუტერის მიერ ჩაფიქრებულ რიცხვს.")
def guess_the_number():
    # სანამა მინიმალური რიცხვი არ იქნება მაქციმალურზე პატარა მანამდე დაა fale_ებს და მოთხოვს ხელახლა შეიყვანოს მომხმარებელს სწორი დიაპაზონი
    valid_input = False
    while not valid_input:
        try:
            print()

            min_number = int(input("შეიყვანეთ მინიმალური რიცხვი: "))
            max_number = int(input("შეიყვანეთ მაქსიმალური რიცხვი: "))
            
            if min_number < max_number:
                valid_input = True  # თუ მინიმალური რიცხვი იქნება მაქსიმალურ რიცხვზე მაღალი მომხმარებელი გადავა გამოსაცნობ რეჟიმში
            else:
                print("მინიმალური რიცხვი უნდა იყოს ნაკლები მაქსიმალურზე. სცადეთ ხელახლა.")
        except ValueError:
            print("გთხოვთ, შეიყვანოთ მხოლოდ მღელი რიცხვები.")

    # შემთხვევითი რიცხვის გენერირება მოცემული დიაპაზონის მიხედვით
    number_to_guess = random.randint(min_number, max_number)
    attempts = 0
    guessed = False

    print(f"შეეცადე გამოიცნო შემთხვევითი რიცხვი {min_number}-დან {max_number}-მდე!")

    # სანამ მომხმარებელი არ გამოიცნობს სწორ რიცხვს
    while not guessed:
        try:
            # მომხმარებლისგან ფამოსაცნობი რიცხივის შეყვანა და ცდების დათვლა
            guess = int(input("შეიყვანეთ თქვენი მოსაზრება: "))
            attempts += 1

            # სწორი პასუხის შემთხვევაში
            if guess == number_to_guess:
                print(f"გილოცავთ! თქვენ გამოიცნეთ ჩაფიქრებული რიცხვი {number_to_guess}. \nჩაფიქრებული რიცხვი გამოიცანით: {attempts} მცდელობაში.\n")
                guessed = True
            # თუ რიცხვი უფრო მაღალია
            elif guess < number_to_guess:
                print("თქვენი რიცხვი ჩაფიქრებულ რიცხვზე დაბალია. სცადეთ უფრო მაღალი რიცხვის შეყვანა.")
            # თუ რიცხვი უფრო დაბალია
            else:
                print("თქვენი რიცხვი ჩაფიქრებულ რიცხვზე მაღალია. სცადეთ უფრო მაღალი რიცხვის შეყვანა.")
        except ValueError:
            print("გთხოვთ შეიყვანოთ მხოლოდ მთელი  რიცხვი.")

# თამშის დასასრულისას ტექსქტის გამოტანა 

guess_the_number()

dasasruli = "თ ა მ ა შ ი ს     დ ა ს ა რ უ ლ ი \n"
for a in dasasruli:
    print(a, end="", flush=True)
    time.sleep(0.1)
