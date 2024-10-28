## **Problem Statement**

Write an algorithm to determine if a number `n` is a happy number.

We use the following process to check if a given number is a happy number:

    - Starting with the given number n, replace the number with the sum of the squares of its digits.
    - Repeat the process until:
        - The number equals 1, which will depict that the given number n is a happy number.
        - It enters a cycle, which will depict that the given number n is not a happy number.

Return TRUE if `n` is a happy number, and FALSE if not.

### Constraints

> 1 ≤ n ≤ 2<sup>31</sup> - 1

## **Examples**

### Example 1: Determining a Happy Number

**Input:** `n = 19`

**Process:**

1. Start with `n = 19`.
2. Calculate the sum of the squares of its digits: $1^2 + 9^2 = 1 + 81 = 82$.
3. Replace 19 with 82.
4. Calculate the sum of the squares of the digits of 82: $8^2 + 2^2 = 64 + 4 = 68$.
5. Replace 82 with 68.
6. Calculate the sum of the squares of the digits of 68: $6^2 + 8^2 = 36 + 64 = 100$.
7. Replace 68 with 100.
8. Calculate the sum of the squares of the digits of 100: $1^2 + 0^2 + 0^2 = 1 + 0 + 0 = 1$.

Since the process reaches 1, **19 is a happy number**.

**Output:** `TRUE`

### Example 2: Determining a Non-Happy Number

**Input:** `n = 20`

**Process:**

1. Start with `n = 20`.
2. Calculate the sum of the squares of its digits: $2^2 + 0^2 = 4 + 0 = 4$.
3. Replace 20 with 4.
4. Calculate the sum of the squares of the digits of 4: $4^2 = 16$.
5. Replace 4 with 16.
6. Calculate the sum of the squares of the digits of 16: $1^2 + 6^2 = 1 + 36 = 37$.
7. Replace 16 with 37.
8. Calculate the sum of the squares of the digits of 37: $3^2 + 7^2 = 9 + 49 = 58$.
9. Replace 37 with 58.
10. Calculate the sum of the squares of the digits of 58: $5^2 + 8^2 = 25 + 64 = 89$.
11. Replace 58 with 89.
12. Calculate the sum of the squares of the digits of 89: $8^2 + 9^2 = 64 + 81 = 145$.
13. Replace 89 with 145.
14. Calculate the sum of the squares of the digits of 145: $1^2 + 4^2 + 5^2 = 1 + 16 + 25 = 42$.
15. Replace 145 with 42.
16. Calculate the sum of the squares of the digits of 42: $4^2 + 2^2 = 16 + 4 = 20$.

The process returns to 20, indicating a cycle. **20 is not a happy number**.

**Output:** `FALSE`

