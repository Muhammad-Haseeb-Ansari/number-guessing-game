import random
number = random.randint(1, 100)

guesses = 0
flag = False
while flag == False :

    try:
        guessed_number = int(input("Please guess a number between 1 and 100: "))
        if(guessed_number >= 1 and guessed_number <= 100):
            guesses = guesses + 1
            if number == guessed_number:
                flag = True
            elif number > guessed_number:
                print("Guess higher")
            elif number < guessed_number:
                print("Guess lower")
        else:
            print("Please enter a number between 1 and 100")
    except ValueError:
        print("Please enter a valid number")

print(f"Congrats!!! You have guessed the correct number in {guesses} tries")