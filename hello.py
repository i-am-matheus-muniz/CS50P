# Ask user for their name, then Capitalize user's name and remove whitespace from str
name = input("What's your name? ").strip().title()

# Split users name into first name and last name
first, last = name.split(" ")

# Say hello to user
print(f"Hello, {first}")