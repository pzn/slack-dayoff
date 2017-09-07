from abc import ABC, abstractmethod
from threading import Thread


class T(ABC):

    def __init__(self, req):
        thread = Thread(target=self.handle, args=[req])
        thread.setDaemon(True)
        thread.start()

    @abstractmethod
    def handle(self, slack_command):
        pass
