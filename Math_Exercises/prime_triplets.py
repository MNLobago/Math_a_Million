def is_prime(n):
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
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if is_prime(arr[i] + arr[j]) and is_prime(arr[j] + arr[k]) and is_prime(arr[k] + arr[i]):
                    count += 1
    return count

if __name__ == "__main__":
    t = int(input("Enter the number of test cases: "))
    for _ in range(t):
        n = int(input("Enter the length of the array: "))
        arr = list(map(int, input("Enter the space-separated elements of the array: ").split()))
        print(count_triplets(arr))
