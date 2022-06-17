from .contract import Contract

class Crypto(Contract):
    """  
    Cryptocurrency contract.

    Examples:
    >>> bitcoin = Crypto("BTC")
    >>> ethereum = Crypto("ETH")
    """
    def __init__(self, symbol: str, currency: str = "USD") -> None:
        super().__init__(symbol, "PAXOS", "CRYPTO", currency)