n = eval(input())
pmd = []
pm = []

s = 0
for i in range(1, n + 1):
    m = eval(input())
    pmd.append(m)
    s = s + m
    miangin = s / n

for j in range(len(pmd)):
    if (pmd[j] - miangin) > 0:
        pm.append((pmd[j] - miangin))
    else:
        pm.append((miangin - pmd[j]))

s = max(pm)

for k in range(len(pmd)):
    if pm.index(max(pm)) == k:
        print(pmd[k])