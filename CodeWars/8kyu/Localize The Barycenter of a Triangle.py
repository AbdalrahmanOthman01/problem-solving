#The link for the kyu : https://www.codewars.com/kata/5601c5f6ba804403c7000004/train/python
def bar_triang(p_a, p_b, p_c): 
    c_x = (p_a[0]+p_b[0]+p_c[0])/3
    c_y = (p_a[1]+p_b[1]+p_c[1])/3
    lst = []
    lst.append(round(c_x,4))
    lst.append(round(c_y,4))
    return lst
