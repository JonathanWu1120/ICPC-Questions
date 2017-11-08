n = int(input())
for i in range(n):
    arr = [1]*10
    a = [int(x) for x in input().split()]
    for i in range(a[1]-1):
    	#this is a formula I managed to find while toying with the problem
        arr = [sum(arr[:i]) for i in range(1,11)]
    print("{} {}".format(a[0],sum(arr)))