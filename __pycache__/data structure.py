lst = ["mango","apple","guava","kiwi"]
print("First Element:",lst[0])
print("Last ELement:",lst[-1])
print("Length of List:",len(lst))
lst.append("grapes")
print("Updated list:",lst)
lst.remove("guava")
print("Updated list:",lst)
lst.sort()
print("Sorted List:",lst)
lst.pop(2)
print("Updated list:",lst)
lst.reverse()
print("Reversed List:",lst)
print("Multiplication on list:",lst*2)
lst = lst[:4]
print("Sliced List:",lst)
lst.clear()
print("Cleared List:",lst)
print("\n")

mydict = {}
mydict = {1: "Jack", 2: "Kiwi"}
mydict = {"name": "Jack", "age": 26}
print(mydict["name"])
print(mydict["age"])

mydict["age"] = 27
print(mydict)

mydict["address"] = "Downtown"
print(mydict)

mydict.pop("address")
print(mydict)

mydict.clear()
print(mydict)