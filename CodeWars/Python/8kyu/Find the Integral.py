def integrate(coefficient, exponent):
    exponent +=1
    coefficient /= exponent
    return f"{int(coefficient)}x^{exponent}"