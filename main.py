k = eval(input())
w = eval(input())
n = eval(input())

s = 0
for i in range(1, n + 1):
    s += i * k

hazine = s - w
if hazine <= 0:
    print(0)
else:
    print(hazine)