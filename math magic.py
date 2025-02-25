number = int(input("Enter a number: "))
result = 0
temp = number
while temp!=0:
    digit = temp % 10
    result = result + digit**3
    temp = temp//10
print(result)
if number == result:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")