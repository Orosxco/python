def romantoint(a):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    intform = 0
    for i in range(len(a)):
        if i+1 < len(a) and roman[a[i]] < roman[a[i+1]]:
            intform -= roman[a[i]]
        else:
            intform += roman[a[i]]
    return intform

a = input("Enter any roman numeral: ")
print(romantoint(a))