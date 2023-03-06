answer = 42 # replace 42 with the number you want to hide

guess = int(input("Guess the number: ")) # prompt user to enter their guess

if guess == answer:
    print("Congratulations! You guessed the number correctly!")
elif guess < answer:
    print("Sorry, your guess is too low.")
else:
    print("Sorry, your guess is too high.")
