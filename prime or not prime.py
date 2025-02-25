from math import sqrt
number = int(input("Enter any number \n"))

if number>1:
    for i in range(2,int(sqrt(number))+1):
        if(number%i==0):
            print("The number is not prime")
            break
    else:
         print("The number is prime")
else:
    print("The number is not prime")