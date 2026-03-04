x = float(input("What's x? "))
y = float(input("What's y? "))

# Rounds the result with 2 digits after the comma
result = round(x / y, 2)

# It is printing result within 2 digits after the comma, even if it doesnt exists
print(f"{result:.2f}")