# Prime Triplets Counter

## Problem Description

You are given an array `arr` having `n` integers. Find the number of triplets `(i, j, k)` such that `arr[i] + arr[j] + arr[k]` is a prime number.

## Input Format

The first line of input contains an integer `t` denoting the number of test cases. The description of each test case is as follows:

- The first line of each test case contains an integer `n`.
- The second line of each test case contains `n` integers, the elements of array `arr`.

## Output Format

For each test case, print the number of triplets that satisfy the given conditions in a separate line.

## Constraints

- 1 <= t <= 100
- 1 <= n <= 100
- 1 <= arr[i] <= 1000

## Sample Input

2
,

4
4 5 6 2
,
4
1 1 4 5

## Sample Output
0
,
1

## Explanation

In the first test case, there are no triplets that satisfy the given conditions.

In the second test case, the triplet `(1, 1, 5)` satisfies the condition because `1 + 1 + 5 = 7`, which is a prime number.
