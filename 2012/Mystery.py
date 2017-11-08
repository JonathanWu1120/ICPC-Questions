cases = int(input())
for i in range(cases):
    num_case = int(input())
    a = input()
    len_c = input()
    c = [int(x) for x in input().split()]
    tracker = 0
    s = ""
    d = len(a)
    for i in c:
        tracker += i
        while abs(tracker) >= d:
            tracker = tracker % d
        s += a[tracker]
    print("{} {}".format(num_case,s))

#I like how in the solution it prints the names of all the teams who participated