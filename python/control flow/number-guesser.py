# '''
# You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 32 #provide answer
guess = 23 #provide guess

if answer > guess: #provide conditional
    result = "Oops!  Your guess was too low."
elif answer < guess: #provide conditional
    result = "Oops!  Your guess was too high."
elif answer == guess: #provide conditional
    result = "Nice!  Your guess matched the answer!"

print(result)