points = 174

if points >= 1 and points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points >= 51 and points <= 150:
    result = "Oh dear, no prize this time."
elif points >= 151 and points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
elif points >= 181 and points <= 200:
    result = "Congratulations! You won a penguin!"
else:
    result = "Invalid points value. Points must be a positive integer up to 200."

print(result)
