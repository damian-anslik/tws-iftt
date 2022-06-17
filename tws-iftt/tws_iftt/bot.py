from .app import App

from abc import ABC, abstractmethod


class TWSBot(ABC):
    def __init__(self, id: int, app: App) -> None:
        """  
        Set up any state management you need for the bot.
        """
        self.id = id
        self.app = app


    @abstractmethod
    def if_this(self) -> bool:
        """
        The condition you want to check for. If returns true, execute 'then that' function.
        """
        pass


    @abstractmethod
    def then_that(self) -> None:
        pass


    def run(self):
        """  
        Run a single iteration of the bot.
        """
        if not self.if_this():
            return None
        self.then_that()