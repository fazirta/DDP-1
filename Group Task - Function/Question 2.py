def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_primes_in_range(lower, upper):
    """Print and return the sum of prime numbers in a given range."""
    primes = [num for num in range(lower, upper + 1) if is_prime(num)]
    prime_sum = sum(primes)
    print(*primes, sep='\n')
    return prime_sum

# Example usage:
lower_limit = 10
upper_limit = 50
prime_sum = sum_of_primes_in_range(lower_limit, upper_limit)
print(f"The sum of prime numbers between {lower_limit} and {upper_limit} is {prime_sum}.")
