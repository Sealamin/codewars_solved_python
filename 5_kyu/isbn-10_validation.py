import re
def valid_ISBN10(isbn): 
    position = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if isbn.isdigit() or (isbn.replace('X', '').isdigit() and 'X' in isbn):
        isbn_2 = [10 if x == 'X' else int(x) for x in isbn]
        if all(x != 10 or i == len(isbn_2) - 1 for i, x in enumerate(isbn_2[:-1])) and all(re.match(r'^[0-9X]$', char) for char in isbn) and len(isbn) == 10 and sum(x * y for x, y in zip(isbn_2, position)) % 11 == 0:
            return True
        else:
            return False
    else:
        return False
