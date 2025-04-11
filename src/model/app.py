class Invalidinterest(Exception):
    pass

class Invalidmonths(Exception):
    pass

class InvalidDataType(Exception):
    pass


def Calculate_programmed_savings(amount: float, interest: float, period: int):

    minimum = 0
    maximus = 100

    if interest <= minimum or interest > maximus:
       raise Invalidinterest( "ERROR: La tasa de interes es invalida" )
    
    if period > maximus:
       raise Invalidmonths( "ERROR: El periodo es invalido" )

    constant = 1
    return amount * (constant + interest ) * period - constant / interest