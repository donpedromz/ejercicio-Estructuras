from datetime import date
from cuentaBancaria import CuentaBancaria
class Banco:
    numeroCuentas = 0
    def __init__(self, cuentasBanco):
        self.cuentasBanco = cuentasBanco
    def __init__(self):
        self.cuentasBanco = []
    def crearCuenta(self, titular, saldo_inicial):
        self.numeroCuentas += 1
        try:
            cuentaNueva = CuentaBancaria(titular, saldo_inicial, self.numeroCuentas)
        except ValueError as err:
            self.numeroCuentas -= 1
            raise err
        cuentaDict = dict()
        cuentaDict[cuentaNueva.getNumeroCuenta()] = cuentaNueva
        self.cuentasBanco.append(cuentaDict)
    def depositar(self, cuenta, monto):
        saldoNuevo = cuenta.getSaldo()
        try:
            saldo = int(monto)
        except ValueError:
            raise ValueError("VALOR INCORRECTO")
        if saldo < 10000:
            raise ValueError("NO SE PERMITEN CONSIGNACIONES MENORES A $10.000")
        saldoNuevo += saldo
        infoTransaccion = 'DEPOSITADO: ${0} | {1}'.format(saldo,date.today())
        cuenta.setSaldo(saldoNuevo)
        cuenta.registrarTransaccion(infoTransaccion)
    def retirar(self, cuenta, monto):
        saldoCuenta = cuenta.getSaldo()
        try:
            saldoRetiro = int(monto)
        except ValueError:
            raise ValueError("VALOR INVALIDO")
        if(saldoRetiro < 10000):
            raise ValueError("VALOR MENOR QUE 10000 INVALIDO")
        if(saldoRetiro > saldoCuenta):
            raise ValueError("SALDO A RETIRAR EXCEDE SALDO DE LA CUENTA")
        saldoCuenta -= saldoRetiro
        infoTransaccion = 'RETIRADO: ${0} | {1}'.format(saldoRetiro, date.today())
        cuenta.setSaldo(saldoCuenta)
        cuenta.registrarTransaccion(infoTransaccion)
    def consultarCuenta(self, numeroCuenta):
        for cuenta in self.cuentasBanco:
            if numeroCuenta in cuenta.keys():
                return cuenta[numeroCuenta]
        raise ValueError("CUENTA NO ENCONTRADA")
    def transferir(self, cuentaOrigen, numeroCuentaDestino, monto):
        if(cuentaOrigen.getNumeroCuenta() == numeroCuentaDestino):
            raise ValueError("INGRESE OTRO NUMERO DE CUENTA")
        try:
            cuentaDestino = self.consultarCuenta(numeroCuentaDestino)
        except ValueError as e:
            raise e
        try:
            saldoTransferencia = int(monto)
        except ValueError:
            raise ValueError("VALOR INVÁLIDO")
        if saldoTransferencia > cuentaOrigen.getSaldo():
            raise ValueError("SALDO EXCEDE EL SALDO DISPONIBLE EN LA CUENTA")
        saldoCuentaOrigen = cuentaOrigen.getSaldo() - saldoTransferencia
        saldoCuentaDestino = cuentaDestino.getSaldo() + saldoTransferencia
        infoCuentaOrigen = "${0} TRANSFERIDOS A {1} ({2}) | {3}".format(saldoTransferencia, cuentaDestino.getTitular(), cuentaDestino.getNumeroCuenta(), date.today())
        infoCuentaDestino = "${0} RECIBIDOS DE {1} ({2}) | {3}".format(saldoTransferencia, cuentaOrigen.getTitular(), cuentaOrigen.getNumeroCuenta(), date.today())
        cuentaOrigen.setSaldo(saldoCuentaOrigen)
        cuentaOrigen.registrarTransaccion(infoCuentaOrigen)
        cuentaDestino.setSaldo(saldoCuentaDestino)
        cuentaDestino.registrarTransaccion(infoCuentaDestino)
        