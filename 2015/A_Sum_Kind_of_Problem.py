cases = int(input())
for i in range(cases):
	a = [int(x) for x in input().split()]
	b = int(a[1]*(a[1]+1)/2)
	d = b*2
	c = d - b
	print("{} {} {} {}".format(a[0],b,c,d))