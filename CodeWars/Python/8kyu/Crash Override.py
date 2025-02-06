#The link for the kyu : https://www.codewars.com/kata/578c1e2edaa01a9a02000b7f/train/python
def alias_gen(f_name, l_name):
    try:
    	return FIRST_NAME[f_name.upper()[0]]+' '+SURNAME[l_name.upper()[0]]
    except:
    	return 'Your name must start with a letter from A - Z.'
