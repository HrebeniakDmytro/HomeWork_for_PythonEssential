def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def generate_primes(limit):
    return [n for n in range(2, limit + 1) if is_prime(n)]
