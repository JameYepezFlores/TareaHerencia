from abc import ABC, abstractmethod
class Cuenta(ABC):
    def __init__(self, numero: str, nombre_propietario: str, saldo: float):
        self._numero = numero
        self._nombre_propietario = nombre_propietario
        self._saldo = saldo

    def _str_(self):
        return f' Cuenta: {self._dict.str_()}'

    @property
    @abstractmethod
    def numero(self):
        pass

    @property
    @abstractmethod
    def nombre_propietario(self):
        pass

    @property
    @abstractmethod
    def saldo(self):
        pass

    @saldo.setter
    @abstractmethod
    def saldo(self, valor):
        pass

    @abstractmethod
    def credito(self, valor: float):
        pass

    @abstractmethod
    def debito(self, valor: float):
        pass

    @abstractmethod
    def mostrar_saldo(self):
        pass


