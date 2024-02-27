from abc import abstractclassmethod, abstractmethod

class InterfaceView(abstractclassmethod):
    def __init__(self):
        self.__callbacks = {}

    @property
    def getCallbacks(self):
        return self.__callbacks

    def add_callbacks(self, key, method):
        self.__callbacks[key] = method

    @abstractmethod
    def bind_comands(self):
        pass