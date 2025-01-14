file = open("text.txt","r")
print("File in read mode")
print(file.read())
file.close()

write = open("text.txt","w")
print("File in Write mode")
write.write("Yo! wyd?")
write.close()

append = open("text.txt","a")
print("File in append mode")
append.write("Yo! wyd?")
append.close()

w = open("text.txt")
counter = 0
content = w.read()
colist = content.split("\n")
for i in colist:
    if i:
        counter += 1

print(counter)
