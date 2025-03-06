import math

def sieve_of_eratosthenes(limit):
    #Sieve of Eratosthenes
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime
    for start in range(2, int(math.isqrt(limit)) + 1):  
        if sieve[start]:
            for multiple in range(start * start, limit + 1, start):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]

def segmented_sieve(low, high):
    # Step 1: Find all primes up to sqrt(high) using the regular sieve
    small_primes = sieve_of_eratosthenes(math.isqrt(high) + 1)
    
    # Step 2: Create a boolean array
    range_size = high - low + 1
    range_primes = [True] * range_size

    for prime in small_primes:
        start = max(prime * prime, low + (prime - low % prime) % prime)

        for i in range(start, high + 1, prime):
            range_primes[i - low] = False

    if low == 1:
        range_primes[0] = False

    return [num for num, is_prime in enumerate(range_primes, low) if is_prime]
#Last step: Select Range
low = 10**8
high = 10**9
primes_in_range = segmented_sieve(low, high)
print(f"Primes in the range {low} to {high}: {primes_in_range[:20]}...")  # Print the first 20 primes
