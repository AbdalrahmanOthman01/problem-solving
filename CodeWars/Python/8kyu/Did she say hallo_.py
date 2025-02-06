#The link for this kyu : https://www.codewars.com/kata/56a4addbfd4a55694100001f/train/python
def validate_hello(greetings):
    g = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for s in g:
        if s in greetings.lower():
            return True
    return False
