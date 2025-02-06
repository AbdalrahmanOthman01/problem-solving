#The link for the 8kyu : https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/train/python
def multi_table(n):
    s = ""
    for i in range(1,11):
        s += f"{i} * {n} = {i*n}"
        if i != 10:
            s += f"\n"
    return s
