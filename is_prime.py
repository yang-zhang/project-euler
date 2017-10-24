def is_prime(n):
    i = 2
    max_p = n
    while i < max_p:
        if n % i == 0:
            return False
        else:
            max_p = n // i
        i += 1
    return True

big_n = 600851475143
n = big_n
while not is_prime(n):
    n -= 1

print('---', n, is_prime(n))