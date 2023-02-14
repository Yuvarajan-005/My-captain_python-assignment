s = list(map(str,input()))
m = list(set(s))
n = []
for i in m:
    c = 0
    for j in s:
        if j == i:
            c+=1
    n.append(c)
d = {}
n2 = n.copy()
for k in m:
    for v in n2:
        d[k]=v
        n2.remove(v)
        break
while len(n)>0:
    for k in m:
        if len(n)>0:
            if d[k] == max(n):
                print("{} = {}".format(k,d[k]))
                n.remove(max(n))