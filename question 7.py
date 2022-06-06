def mode(numlist):

    mylist = numlist
    dic = {}

    for num in mylist:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1

    vals = max(dic.values())
    return [k for k, v in dic.items() if v == vals]


print(mode([6, 1, 1, 6]))