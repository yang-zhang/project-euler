big_n = 600851475143

n = big_n
factors = {}
i = 2
max_potential_factor = n
while i <= max_potential_factor:
    if n % i == 0:
        factors[i]=0
        while  n % i == 0:
            n = n // i
            factors[i]+=1
    else:
        max_potential_factor = n // i
    i += 1

print(n)
