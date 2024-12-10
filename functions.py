def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)

n = int(input("Enter any number: "))

if n<0:
    print("Sorry, factorial does not exist for negative number")
elif n == 0:
    print("factorial of 0 is 1")
else:
    print("The factorial of", n,"is", recur_factorial(n))

print("\n")

def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y

x = int(input("Enter any number: "))
y = int(input("Enter any number: "))

print("sum", addition(x,y))
print("difference", subtraction(x,y))
print("product", multiplication(x,y))
print("division", division(x,y))