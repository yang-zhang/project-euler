a = 0
fb0 = 1
fb1 = 2
while fb0 < 4000000:
    tmp = fb1
    fb1 = fb0 + fb1
    fb0 = tmp
    if fb0 % 2 == 0:
        a += fb0

print(a)