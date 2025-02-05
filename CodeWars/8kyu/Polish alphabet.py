#The link for this kyu : https://www.codewars.com/kata/57ab2d6072292dbf7c000039/train/python
def correct_polish_letters(st): 
    new_str =''
    for i in range(0,len(st)):
    
        # print(st)
        if st[i] == 'ą': new_str+='a'
        elif st[i] == 'ę' :new_str+='e'
        elif st[i] == 'ć': new_str+='c'
        elif st[i] == 'ł': new_str+='l'
        elif st[i] == 'ń' : new_str+= 'n'
        elif st[i] == 'ó': new_str+='o'
        elif st[i] == 'ś': new_str+='s'
        elif st[i] == 'ź' : new_str+='z'
        elif st[i] == 'ż' : new_str+='z'

        else :  new_str+= st[i]
    return new_str
