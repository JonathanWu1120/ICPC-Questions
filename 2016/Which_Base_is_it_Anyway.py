n = int(input())
for i in range(n):
    base_num = input().split(" ")
    try:
        arr = [str(int(base_num[0])),str(int(base_num[1],8)),str(int(base_num[1])),str(int(base_num[1],16))]
        str1 = ' '.join(arr).strip(" ")
        print(str1)
    except ValueError:
        arr = [str(int(base_num[0])),str(0),str(int(base_num[1])),str(int(base_num[1],16))]
        str1 = ' '.join(arr).strip(" ")
        print(str1)
    