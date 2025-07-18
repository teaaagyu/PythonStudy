number = 7

while True:
    guess = int(input("guess a number: "))

    if guess == number:
        print("correct")
        break
    else:
        print("try again")

