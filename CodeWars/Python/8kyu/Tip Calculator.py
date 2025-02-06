#The link for this kyu : https://www.codewars.com/kata/56598d8076ee7a0759000087/train/python
def calculate_tip(amount, rating):
    from math import ceil
    rating = rating.lower()
    if rating == "terrible":
        return 0
    elif rating == "poor": 
        return ceil(amount * (5/100))
    elif rating == "good": 
        return ceil(amount * (10/100) )   
    elif rating == "great": 
        return ceil(amount * (15/100)) 
    elif rating == "excellent": 
        return ceil( amount * (20/100))  
    else:
        return 'Rating not recognised'
