lst = [2,5,2,8,5,3,2,9]
a = []

for e in lst:
    if e not in a:
        a.append(e)
        print(e)
