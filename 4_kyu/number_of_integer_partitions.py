def partitions(n):
    partitions = [1] + [0]*n
    for num in range(1, n+1):
        for i in range(num, n+1):
            partitions[i] += partitions[i-num]
    return partitions[n]
