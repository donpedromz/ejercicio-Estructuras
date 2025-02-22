class CuentaBancaria:
    def __init__(self, titular, saldo, numeroCuenta):
        self.__titular = titular
        try:
            saldoNum = int(saldo)
        except ValueError:
            raise ValueError("VALOR INCORRECTO")
        if saldoNum < 0:
            raise ValueError("MONTO MENOR QUE 0 NO PERMITIDO")
        self.__saldo = saldoNum
        self.__numeroCuenta = 'CJPPD-{0}'.format(numeroCuenta)
        self.__historialTransacciones = []
    def __str__(self):
        return 'Numero de cuenta: {0}, Titular de la Cuenta: {1}, Saldo disponible en la cuenta: {2}, {3}'.format(self.__numeroCuenta,self.__titular,self.__saldo, self.getHistorialTransacciones())
    def getNumeroCuenta(self):
        return self.__numeroCuenta
    def getSaldo(self):
        return self.__saldo
    def setSaldo(self, monto):
        self.__saldo = monto
    def getHistorialTransacciones(self):
        return self.__historialTransacciones
    def registrarTransaccion(self, infoTransaccion):
        self.__historialTransacciones.append(infoTransaccion)
    def getTitular(self):
        return self.__titular