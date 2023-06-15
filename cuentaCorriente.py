from cuenta import Cuenta

class CuentaCorriente(Cuenta):
    def __init__(self, numero: str, nombre_propietario: str, saldo: float, tiene_chequera: bool):
        super().__init__(numero, nombre_propietario, saldo)
        self._tiene_chequera = tiene_chequera

    @property
    def numero(self):
        return self._numero

    @property
    def nombre_propietario(self):
        return self._nombre_propietario

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    @property
    def tiene_chequera(self):
        return self._tiene_chequera

    @tiene_chequera.setter
    def tiene_chequera(self, valor):
        self._tiene_chequera = valor

    def credito(self, valor: float):
        self._saldo += valor

    def debito(self, valor: float):
        if self._saldo >= valor:
            self._saldo -= valor
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        return self._saldo

    def pagar_cheque(self, valor: float):
        if self._saldo >= valor:
            self._saldo -= valor
            print("Cheque pagado.")
        else:
            print("Insuficientes fondos para pagar el cheque.")


if __name__ == '__main__':
    cuenta = CuentaCorriente("1237888", "Jame Yepez", 2000.0, True)
    print(f"Saldo actual de {cuenta.nombre_propietario}: {cuenta.mostrar_saldo()}")

    cuenta.credito(500.0)
    print(f"Saldo actual de Cuenta credito {cuenta.nombre_propietario}: {cuenta.mostrar_saldo()}")

    cuenta.debito(1000.0)
    print(f"Saldo actual de Cuenta debito {cuenta.nombre_propietario}: {cuenta.mostrar_saldo()}")

    cuenta.pagar_cheque(1500.0)
    print(f"Saldo actual de cheque pagado {cuenta.nombre_propietario}: {cuenta.mostrar_saldo()}")