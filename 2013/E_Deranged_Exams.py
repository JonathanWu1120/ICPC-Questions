from math import factorial as f
def memoize(func):
    S = {}
    def wrappingfunction(*args):
        if args not in S:
            S[args] = func(*args)
        return S[args]
    return wrappingfunction

@memoize
def S(n,k):
    if k == 0:
        return f(n)
    return S(n,k-1) - S(n-1,k-1)
    
n = int(input())
for i in range(n):
    a = [int(x) for x in input().split(" ")]
    print("{} {}".format(a[0],S(a[1],a[2])))