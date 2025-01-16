file = open("text.txt","r")
print(file.read())
file.close()

file = open("text.txt")
print("Reading first line...")
print(file.readline())
file.close()
