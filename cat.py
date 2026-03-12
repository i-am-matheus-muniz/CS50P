#While Loop:
# i = 0
# while i < 3:
#     print("meow")
#     i += 1
###
#This for loop works fine, but if we want like a million, we need to think about range...
# for i in [0, 1, 2]:
#     print("meow")
###
#This works just fine, but there's a pythonic way to do that...
# for i in range(3):
#     print("meow")
###
#Using _ as a variable indicates that this will only be used in this part of the code, is not important for using later
# for _ in range(3):
#     print("meow")
###
#This is a good way to retrieve the value from the user... but let's try to improve it using functions
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")
###
def main():
    meow(get_number())

def get_number():
    while True:
        number = int(input("How many meows it made? "))
        if number > 0:
            break
    return number

def meow(n):
    for _ in range(n):
        print("meow")

main()