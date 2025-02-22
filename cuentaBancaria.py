class CuentaBancaria:
    def __init__(self, titular, saldo, numeroCuenta):
        self.__titular = titular
        self.__saldo = saldo
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
        if(len(self.__historialTransacciones) == 0):
            return 'NO HAY TRANSACCIONES REGISTRADAS'
        return 'SU HISTORIAL DE TRANSACCIONES: {0}'.format(self.__historialTransacciones)
    def registrarTransaccion(self, infoTransaccion):
        self.__historialTransacciones.append(infoTransaccion)