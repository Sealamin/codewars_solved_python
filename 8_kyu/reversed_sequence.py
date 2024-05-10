def reverse_seq(n):
    list = [n]
    for i in range(n-1):
        list.append(list[-1]-1)
    return list
