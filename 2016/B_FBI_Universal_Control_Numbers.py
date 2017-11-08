dict = {'B':'8','G':'C','I':'1','O':'0','Q':'0','S':'5','U':'V','Y':'V','Z':'2'}
cases = int(input())
st = "0123456789ACDEFHJKLMNPRTVWX"
for i in range(cases):
    case, data = input().split()
    #2,4,5,7,8,10,11,
    check, is_valid = 0, True
    for i,k in enumerate(data):
        k = int(st.find(k)) if k in st else int(st.find(dict[k]))
        if i == 0:
            check += 2*k
        elif i == 1:
            check += 4*k
        elif i == 2:
            check += 5*k
        elif i == 3:
            check += 7*k
        elif i == 4:
            check += 8*k
        elif i == 5:
            check += 10*k
        elif i == 6:
            check += 11*k
        elif i == 7:
            check += 13*k
        elif i == 8:
            if check%27 != k:
                print(case,"Invalid")
                is_valid = False
    if is_valid:
        base, total = 7, 0
        for i in range(8):
            num = 27**base
            k = int(st.find(data[i])) if data[i] in st else int(st.find(dict[data[i]]))
            total += num*k
            base -= 1
        print(case,total)
        