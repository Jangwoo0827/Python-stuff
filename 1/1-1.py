import random

num = random.randint(1, 100)
tries = 1
while True:
    num2 = input("Guess the number: ")
    try:
        num2 = int(num2)  # Convert input to an integer
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    if num2 == num:
        print("Congrats! You got the number in", tries, "tries!")
        break  # End the loop when the user guesses correctly
    elif num2 > num:
        print("The number is smaller than your guess.")
        tries += 1
    elif num2 < num:
        print("The number is bigger than your guess.")
        tries += 1
    else:
        while True:
            print("You made a freaking error.")
