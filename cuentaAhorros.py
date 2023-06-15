from cuenta import Cuenta


class CuentaAhorros(Cuenta):
    def __init__(self, numero: str, nombre_propietario: str, saldo: float, interes: float):
        super().__init__(numero, nombre_propietario, saldo)
        self._interes = interes

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
    def interes(self):
        return self._interes

    @interes.setter
    def interes(self, valor):
        self._interes = valor

    def credito(self, valor: float):
        self._saldo += valor

    def debito(self, valor: float):
        if self._saldo >= valor:
            self._saldo -= valor
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        return self._saldo

    def pagar_interes(self):
        interes_generado = self._saldo * self._interes
        self._saldo += interes_generado


if __name__ == '__main__':
    cuenta = CuentaAhorros("0988887665", "Jame Yepez", 1000.0, 0.05)
    print(f"Saldo actual de {cuenta.nombre_propietario}: {cuenta.mostrar_saldo()}")
    cuenta.credito(500.0)
    print(f"Credito Saldo actual : {cuenta.mostrar_saldo()}")
    cuenta.debito(200.0)
    print(f"Debito Saldo actual: {cuenta.mostrar_saldo()}")
    cuenta.pagar_interes()
    print(f"Pago interes Saldo actual: {cuenta.mostrar_saldo()}")