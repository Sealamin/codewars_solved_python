def sum_two_smallest_numbers(numbers):
    numbers.sort(reverse = True)
    return numbers[-1]+numbers[-2]
