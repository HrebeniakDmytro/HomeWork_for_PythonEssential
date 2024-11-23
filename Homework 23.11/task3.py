def prime_generator(n):
    count = 0  
    num = 2    
    
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = 10
primes = prime_generator(n)
print(list(primes))
