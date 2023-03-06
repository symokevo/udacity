names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    # Convert the name to lowercase and replace spaces with underscores
    username = name.lower().replace(" ", "_")
    # Append the username to the list
    usernames.append(username)

print(usernames)
