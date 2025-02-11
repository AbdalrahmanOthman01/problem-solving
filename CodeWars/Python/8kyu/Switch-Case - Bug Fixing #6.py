#The link for this kyu : https://www.codewars.com/kata/55c933c115a8c426ac000082/train/python
def eval_object(v):
    match v["operation"]:  # Match the operation key from the dictionary
        case "+":
            return v["a"] + v["b"]
        case "-":
            return v["a"] - v["b"]
        case "/":
            return v["a"] / v["b"]
        case "*":
            return v["a"] * v["b"]
        case "%":
            return v["a"] % v["b"]
        case "**":
            return v["a"] ** v["b"]
        case _:
            return 1
