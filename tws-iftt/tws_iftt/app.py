from .client import Client
from .wrapper import Wrapper
from .bot import TWSBot
from time import sleep

class App(Client, Wrapper):


    def __init__(self) -> None:
        self.__bots = []


    def register_bots(self, bots: list[TWSBot]):
        self.__bots = bots
    

    def run(self) -> None:
        while True:
            try:
                for bot in self.__bots:
                    bot.run()
                    sleep(0.5)
            except KeyboardInterrupt:
                break