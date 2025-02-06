#The link for this kyu : https://www.codewars.com/kata/54598d1fcbae2ae05200112c/train/python
def _all(seq, fun): 
    for i in seq:
        if fun(i) == False:
            return False
    return True
