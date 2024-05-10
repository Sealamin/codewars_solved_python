def find_uniq(arr):
    arr.sort()
    if arr[0] == arr[1] and arr[-1] != arr[-2]:
        return arr[-1]
    else:
        return arr[0]
