#The link for this kyu : https://www.codewars.com/kata/568dc014440f03b13900001d/train/python
d = {
    "jabroni": "Patron Tequila",
    "school counselor": "Anything with Alcohol",
    "programmer": "Hipster Craft Beer",
    "bike gang member": "Moonshine",
    "politician": "Your tax dollars",
    "rapper": "Cristal"
}

def get_drink_by_profession(s):
    return d.get(s.lower(), "Beer")
