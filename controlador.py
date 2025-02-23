from banco import Banco
from bancoUi import BancoUi
from bancoUi import CrearCuentaForm
from bancoUi import VentanaInfoCuenta
from bancoUi import formularioDepositarDinero
from bancoUi import formularioRetirarDinero
class ControladorCuentas:
    def __init__(self):
        self.banco = Banco()
        self.vista = BancoUi(self)
        self.vista.mostrarVentanaPrincipal()
    def formularioCrearCuenta(self):
        self.formularioCrear = CrearCuentaForm(self)
    def crearCuenta(self):
        titular = self.formularioCrear.entradaNombre.get()
        saldo = self.formularioCrear.entradaSaldo.get()
        try:
            self.banco.crearCuenta(titular,saldo)
        except ValueError as err:
            self.formularioCrear.mostrarError(str(err))
            return
        self.formularioCrear.destroy()
    def buscarCuenta(self):
        cuenta = self.vista.entradaCuenta.get()
        try:
            self.cuentaSesion = self.banco.consultarCuenta(cuenta)
        except ValueError as err:
            self.vista.mostrarErrorCuenta(str(err))
            return
        self.ventanaInfoCuenta = VentanaInfoCuenta(self,self.cuentaSesion)
    def depositarDinero(self):
        self.formularioDeposito = formularioDepositarDinero(self,self.cuentaSesion)
    def retirarDinero(self):
        self.formularioRetiro = formularioRetirarDinero(self,self.cuentaSesion)
    def transferirDinero(self):
        pass
    def depositar(self):
        valor = self.formularioDeposito.entradaMonto.get()
        try:
            self.banco.depositar(self.cuentaSesion,valor)
            self.formularioDeposito.destroy()
        except ValueError as e:
            self.formularioDeposito.mostrarError(str(e))
    def retirar(self):
        valor = self.formularioRetiro.entradaMonto.get()
        try:
            self.banco.retirar(self.cuentaSesion,valor)
            self.formularioRetiro.destroy()
        except ValueError as e:
            self.formularioRetiro.mostrarError(str(e))