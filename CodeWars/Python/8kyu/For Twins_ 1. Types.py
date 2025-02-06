#The link for this kyu : https://www.codewars.com/kata/59c1302ecb7fb48757000013/train/python
def type_validation(variable, _type): 
    # your code here
    return type(variable).__name__ == _type
