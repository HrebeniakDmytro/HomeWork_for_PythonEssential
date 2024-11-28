import prime_numbers
from prime_numbers import is_prime, generate_primes

def main():
    print("Імпортовані окремі функції:")

    num = 29
    print(f"Число {num} є простим: {is_prime(num)}")

    limit = 50
    primes = generate_primes(limit)
    print(f"Прості числа до {limit}: {primes}")

    print("\nВикористання повного модуля:")

    num = 15
    print(f"Число {num} є простим: {prime_numbers.is_prime(num)}")
    primes = prime_numbers.generate_primes(20)
    print(f"Прості числа до 20: {primes}")

main()
