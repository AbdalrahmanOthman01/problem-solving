#The link for this kyu : https://www.codewars.com/kata/57241e0f440cd279b5000829/train/python
def sum_mul(n, m):
    if m>0 and n>0:
        return sum(range(n, m, n))
    else:
        return 'INVALID'
