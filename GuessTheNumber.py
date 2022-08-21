Number = 41
Guess = 5

while True:
    print ("Remaining Guesses : ", Guess)
    UserInput = int(input ("Guess the Number : "))
    if UserInput == Number:
        print ("Congratulation!")
        break
    elif  Guess >0 and UserInput > Number:
        print("Decrease the Number")
        Guess = Guess -1
        continue
    elif Guess >0 and UserInput < Number:
        print("Increase the Number")
        Guess = Guess -1
        continue
    elif Guess == 0:
        print("Game Over!")
        break