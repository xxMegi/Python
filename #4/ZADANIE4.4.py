def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

fibonacci_result = fibonacci(6)
expected_fibonacci_result = 8
assert fibonacci_result == expected_fibonacci_result