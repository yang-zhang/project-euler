a = 0
for x in range(1000):
    if (x % 3==0) | (x % 5==0):
        a += x
print(a)