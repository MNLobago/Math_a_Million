# Permutation Divisibility Checker

## Problem Statement

Consider a permutation of numbers 1 to n written on a paper. Let’s denote the product of its elements as `P` and the sum of its elements as `S`. Given a positive integer `n`, the task is to determine whether `P` is divisible by `S` or not.

## Input Format

- The input starts with an integer `t`, the number of test cases.
- Each test case contains an integer `n`, the length of the permutation.

## Output Format

- For each test case, print “YES” if `P` is divisible by `S`, otherwise print “NO”.

## Sample Input

2
2
3


## Sample Output

NO
YES


## Explanation

For the first test case with n = 2:
- P = 1 * 2 = 2
- S = 1 + 2 = 3
- 2 is not divisible by 3, hence the output is "NO".

For the second test case with n = 3:
- P = 1 * 2 * 3 = 6
- S = 1 + 2 + 3 = 6
- 6 is divisible by 6, hence the output is "YES".

## Time Limit: 2 seconds
## Memory Limit: 256 MB

## Implementation

The solution is implemented in Python. The function `is_divisible(n)` calculates whether the factorial of `n` is divisible by the sum of the first `n` natural numbers. The `main` function handles multiple test cases and outputs the results accordingly.

### Code

```python
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
