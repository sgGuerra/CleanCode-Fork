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
    def calculate_programmed_savings(self):

        minimum_interest = 0
        maximus_interest = 1
        
        minimum_period = 1
        maximus_period = 120

        if self.interest <= minimum_interest or self.interest > maximus_interest:
            raise Invalidinterest( "ERROR: La tasa de interes es invalida" )
    
        if self.period > maximus_period or self.period < minimum_period:
            raise Invalidmonths( "ERROR: El periodo es invalido" )

        constant = 1
        tasa_mensual = (1 + self.interest) ** (1/12) - 1
        return self.amount * (((constant + tasa_mensual) ** self.period - constant) / tasa_mensual)
    
    def do_tuple(self,):
        return (self.amount, self.interest, self.period)
    
    def create_id(self,):
        return random.randint(1, 100)