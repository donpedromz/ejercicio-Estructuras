from banco import Banco
from bancoUi import BancoUi
from bancoUi import CrearCuentaForm
from bancoUi import VentanaInfoCuenta
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
            cuenta = self.banco.consultarCuenta(cuenta)
        except ValueError as err:
            self.vista.mostrarErrorCuenta(str(err))
            return
        self.ventanaInfoCuenta = VentanaInfoCuenta(self,cuenta)