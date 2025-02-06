#The link for this kyu : https://www.codewars.com/kata/56f3f6a82010832b02000f38/train/python
def describe_age(a): 
    return f"You're a(n) {a<13 and 'kid' or a<18 and 'teenager' or a<65 and 'adult' or 'elderly'}"
