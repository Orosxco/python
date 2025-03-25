def swap1(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("After swapping a =",a,"b =",b)

def swap2(a,b):
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    print("After swapping a =",a,"b =",b)

swap1(3,7)
swap2(3,7)