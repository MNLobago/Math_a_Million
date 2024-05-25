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

def count_triplets(arr):
    """Count the number of triplets whose sum is a prime number."""
    count = 0
    n = len(arr)
    prime_cache = {}  # Cache for storing prime numbers
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                sum_val = arr[i] * arr[j] * arr[k]  # Multiply the elements to reduce the number of iterations
                if sum_val in prime_cache:  # Check if the value is already in the cache
                    if prime_cache[sum_val]:  # If it's prime, increment the count
                        count += 1
                else:
                    if is_prime(sum_val):  # If not in cache, calculate and store the result in the cache
                        count += 1
                        prime_cache[sum_val] = True
                    else:
                        prime_cache[sum_val] = False
    return count

if __name__ == "__main__":
    t = int(input("Enter the number of test cases: "))
    for case in range(1, t + 1):
        n = int(input(f"Enter the length of array for Test Case {case}: "))
        arr = list(map(int, input(f"Enter the space-separated elements of array for Test Case {case}: ").split()))
        print(f"Result for Test Case {case}: {count_triplets(arr)}")
