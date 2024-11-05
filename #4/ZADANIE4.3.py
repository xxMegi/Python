def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

factorial_result = factorial(5)
expected_factorial_result = 120
assert factorial_result == expected_factorial_result