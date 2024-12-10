num = int(input("Enter any number: "))
digits = int(input("Enter the number of digits: "))
temp = num
sum = 0

while num>=0:
    rem = temp%10
    sum += rem**digits
    num /= 10

if sum == num:
    print("The number is an armstrong number")
else:
    print("The number is not an armstrong number")
    