points = 174  # use this input to make your submission

# write your if statement here
if points <= 50:
    print("Congratulations! You won a wooden rabbit!")
elif points >= 50 and points <= 150:
    print("Oh dear, no prize this time.")
elif points >= 150 and points <= 180:
    print("Congratulations! You won a water-thin mint!")
else:
    print("Congratulations! You won a penguin!")

results = points
print(results)
