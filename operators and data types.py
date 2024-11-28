name = "Penguin"
age=15
Employed = False
weight = 43.7

print("The data type of name is ", type(name))
print("The data type of age is ", type(age))
print("The data type of Employed is ", type(Employed))
print("the data type of weight is ", type(weight))

print("\n After type casting... ")
age = str(age)
print("The data type of age is now ", type(age))
print("\n")

num1 = 32
num2 = 21
print("Addition: ",num1+num2)
print("Difference: ",num1-num2)
print("Multiplication: ",num1*num2)
print("Division: ",num1/num2)
print("Floor Division: ",num1//num2)
print("Modulus: ",num1%num2)
print("Exponent: ",num1**num2)
print("\n")
result = num1/2+10**3-27
print("The result of num1/2+10^3-27 is ",result)
print("\n")

first_name = "Affan"
last_name = " Asif"
full_name = first_name+last_name
print("My name is ",full_name)
word = "operator"
print(word)
print("length of the word: ",len(word))
print("First letter of word: ",word[0])
print("Last letter of word: ",word[7])
print("Word sliced: ",word[0:4])
