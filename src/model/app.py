import random

class Invalidinterest(Exception):
    pass

class Invalidmonths(Exception):
    pass

class InvalidDataType(Exception):
    pass

class Saving:
    
    def __init__(self, amount: float, interest: float, period: int):
        self.amount: float = amount
        self.interest: float = interest
        self.period: int = period
        #self.id: int = self.create_id()

    def calculate_programmed_savings(self,):

        minimum = 0
        maximus = 1

        if self.interest <= minimum or self.interest > maximus:
            raise Invalidinterest( "ERROR: La tasa de interes es invalida" )
    
        if self.period > maximus or self.period < minimum:
            raise Invalidmonths( "ERROR: El periodo es invalido" )

        constant = 1
        return self.amount * (constant + self.interest ) * self.period - constant / self.interest
    
    def do_tuple(self,):
        return (self.amount, self.interest, self.period)
    
    def create_id(self,):
        return random.randint(1, 100)