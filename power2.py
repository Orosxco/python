def power2(number):
    if number <= 0:
        return False
    return (number & (number - 1)) == 0

number = int(input("Enter any number: "))
if power2(number):
    print("The number is a power of two")
else:
    print("The number is not a power of two")