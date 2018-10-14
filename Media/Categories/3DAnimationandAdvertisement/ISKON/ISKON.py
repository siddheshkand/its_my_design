t = int(input())

for i in range(t):
    total = input()
    total = total.split(' ')
    n = int(total[0])
    k_in = int(total[1])
    x1 = int(total[2])
    y1 = int(total[3])
    c = int(total[4])
    d = int(total[5])
    e1 = int(total[6])
    e2 = int(total[7])
    f = int(total[8])

    x = [x1]
    y = [y1]
    # arr = [x1+y1]
    arr = []
    for j in range(2, n + 1):
        x.append((x[j - 2] * c + y[j - 2] * d + e1) % f)
        y.append((x[j - 2] * d + y[j - 2] * c + e2) % f)

    for each in range(len(x)):
        arr.append((x[each] + y[each]) % f)
        # print(arr[each])
    tot = []
    temp = []
    for j in range(n):
        for k in range(n - j):
            temp = []
            for l in range(j + 1):
                # print(j, k, l)
                temp.append(arr[l + k])
            tot.append(temp)
    fin = [0] * n
    for each in range(1, k_in + 1):
        for num in range(1, n + 1):
            fin[num - 1] += (pow(num, each))
    answer = 0
    for each in tot:
        for each_li in range(len(each)):
            answer += each[each_li] * fin[each_li]
            # print(answer)
            # print(each[each_li], fin[each_li])
    # print(answer % 1000000007)
    # print(tot)
