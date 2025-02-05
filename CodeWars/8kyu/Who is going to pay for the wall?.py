#the link for this kyu : https://www.codewars.com/kata/58bf9bd943fadb2a980000a7/train/python
def who_is_paying(name):
    lst = [name]
    if len(name) <= 2 :
        return lst
    else:
        n = name[0]+name[1]
        lst.append(n)
        return lst
