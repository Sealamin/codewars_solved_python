def removNb(n):
    sum_of_sequence = n * (n + 1) // 2
    result = []
    for a in range(1, n + 1):
        b = (sum_of_sequence - a) // (a + 1)
        if b <= n and a * b == sum_of_sequence - a - b:
            result.append((a, b))
    return result
