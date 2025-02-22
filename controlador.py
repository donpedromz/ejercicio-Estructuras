from banco import Banco
from bancoUi import BancoUi
from bancoUi import CrearCuentaForm
class ControladorCuentas:
    def __init(self):
        self.banco = Banco()
    def __init__(self):
        self.banco = Banco()
        self.vista = BancoUi(self)
    def formularioCrearCuenta(self):
        self.formularioCrear = CrearCuentaForm(self)
    def crearCuenta(self):
        titular = self.formularioCrear.entradaNombre.get()
        saldo = self.formularioCrear.entradaSaldo.get()
        self.banco.crearCuenta(titular,saldo)
        self.formularioCrear.destroy()