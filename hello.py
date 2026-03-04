# Creating my main function
def main():
    # Ask user for their name, then Capitalize user's name and remove whitespace from str
    name = input("What's your full name? ").strip().title()

    # Split users name into first name and last name
    first, last = name.split(" ")

    # Say hello to user
    hello(first)

# Creating a function Hello
def hello(to="world"):
    print(f"Hello, {to}")

main()