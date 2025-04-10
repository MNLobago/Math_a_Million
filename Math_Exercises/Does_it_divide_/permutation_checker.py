import math

def is_divisible(n):
    """
    Check if the factorial of n is divisible by the sum of the first n natural numbers.
    
    :param n: Length of the permutation (integer)
    :return: True if divisible, False otherwise
    """
    sum_elements = n * (n + 1) // 2  # Sum of first n natural numbers
    product_elements = math.factorial(n)  # Factorial of n
    return product_elements % sum_elements == 0

def main():
    """
    Main function to read input, process each test case, and print the results.
    """
    t = int(input("Enter the number of test cases: "))  # Number of test cases
    results = []
    for _ in range(t):
        n = int(input(f"Enter the length of the permutation for test case {_ + 1}: "))  # Length of the permutation
        if is_divisible(n):
            results.append("YES")
        else:
            results.append("NO")
    
    # Print results for all test cases
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
