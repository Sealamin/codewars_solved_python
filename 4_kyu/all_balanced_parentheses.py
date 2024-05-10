def balanced_parens(n):
    if n == 0:
        return ['']
    elif n == 1:
        return ["()"]
    else:
        parens = []
        for i in range(n):
            for left in balanced_parens(i):
                for right in balanced_parens(n-1-i):
                    parens.append('({}){}'.format(left, right))
        return parens
