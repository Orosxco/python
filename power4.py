def power4(n):
    return n > 0 and (n & (n - 1) == 0) and (n - 1) % 3 == 0

n = int(input("Enter any number: "))
if power4(n):
    print("The number is a power of 4")
else:
    print("The numbe is not a power of 4")