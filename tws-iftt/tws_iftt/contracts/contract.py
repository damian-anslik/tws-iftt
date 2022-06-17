from random import randint


class Contract:
    """  
    This is the base contract class. It is meant to be subclassed.
    """
    def __init__(self, symbol: str, exchange: str, security_type: str, currency: str = "USD") -> None:
        self.symbol = symbol
        self.exchange = exchange
        self.secType = security_type
        self.currency = currency