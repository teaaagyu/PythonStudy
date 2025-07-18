number = 7
tries = 0

while tries < 3:
    guess = int(input("guess a number: "))
    tries += 1

    if guess == number:
        print(f"correct! you guessed it in {tries} tries.")
        break
    elif guess < number:
        print("too low, try again")
    elif guess < number:
        print("too high, try again")    
else:
    print(f"game over the correct number was {number}.")
    