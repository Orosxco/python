def worst(n):
    iterations = 0
    for i in range(0,n):
        for j in range(0,n):
            print("*", end = "")
            iterations+=1
        print("")
    print("The iteration for n is", iterations)

worst(10)
worst(3)

#for every n the time taken will increase quadrilaterally
#Time complexity = O(n^2)
#worst case scenario