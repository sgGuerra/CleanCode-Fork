from sqlalchemy import Column, Serial, Decimal
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

Base = declarative_base()

class Ahorro(Base):
    _tablename_ = 'saving'

    id = Column(Serial, primary_key=True)
    amount = Column(Decimal, nullable=False)
    interest = Column(Decimal, nullable=False)
    period = Column(Decimal, nullable=False)
    

    def _repr_(self):
        return f"<Ahorro(id='{self.id}', monto={self.amount}, interes={self.interest}, meses={self.period})>"