from tws_iftt import TWSBot, App
from tws_iftt.contracts import Crypto


class CryptoPriceBot(TWSBot):
    """  
    Retrieves the ask price for a specified cryptocurrency. Print a messsage to the console when the price increases
    compared to the previous value.
    """
    def __init__(self, id: int, app: App, currency: str) -> None:
        super().__init__(id, app)
        self.crypto = Crypto(currency)
        self.ask_price = None
        self.previous_ask_price = None


    def if_this(self):
        self.ask_price, self.previous_ask_price = self.app.reqMktData(), self.ask_price
        if self.previous_ask_price is None:
            return False
        return self.ask_price > self.previous_ask_price


    def then_that(self):
        print(f"({self.id}) Bitcoin price is up by {self.ask_price - self.previous_ask_price}")


if __name__ == "__main__":
    currencies = ["BTC", "ETH", "BCH"]
    bots = [CryptoPriceBot(id, currency) for id, currency in enumerate(currencies)]
    app = App()
    app.register_bots(bots)
    app.run()