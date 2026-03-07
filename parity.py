def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
#Definition of Even or Odd in Pythonic way:
def is_even(n):
    return n % 2 == 0

main()

# Other ways to do this:
#     Slightly enhanced way:
#         def is_even(n):
#             return True if n % 2 == 0 else False
#     Worst way:
#         def is_even(n):
#             if n % 2 == 0:
#                 return True
#             else:
#                 False