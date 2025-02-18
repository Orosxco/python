def OnTime(n):
    iterations = 0
    print(n)
    for i in range(1,n+1):
        iterations+=1
    print("The number of iterations by computer are ", iterations)

OnTime(10)
OnTime(20)
OnTime(256)

#for every n the time taken will increase linearly
#time complexity = O(n)
#Average case scenario