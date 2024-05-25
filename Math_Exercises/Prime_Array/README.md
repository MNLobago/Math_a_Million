# Prime Triplets Counter

## Problem Description

You are given an array `arr` containing `n` integers. Find the number of triplets `(i, j, k)` such that the product of the elements `arr[i] * arr[j] * arr[k]` is a prime number.

### Input Format

- The first line of input contains an integer `t` denoting the number of test cases.
- For each test case:
  - The first line contains an integer `n`, the number of elements in the array.
  - The second line contains `n` space-separated integers, the elements of the array.

### Output Format

For each test case, print the number of triplets that satisfy the given condition.

### Constraints

- 1 <= t <= 100: Number of test cases
- 1 <= n <= 100: Number of elements in each array
- 1 <= arr[i] <= 1000: Range of array elements

### Sample Input

2
4
4 5 6 2
4
1 1 4 5


### Sample Output

Result for Test Case 1: 0
Result for Test Case 2: 1


### Explanation

In the first test case, there are no triplets that satisfy the given condition.
In the second test case, the triplet `(1, 1, 5)` satisfies the condition because `1 * 1 * 5 = 5`, which is a prime number.
