import tkinter as tki
from tkinter import ttk 
class BancoUi(tki.Frame):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.crearElementos()
        self.pack()
    def crearElementos(self):
        self.titulo = tki.Label(self, text="Bienvenido a BancUAM\n")
        self.instrucciones=tki.Label(self, text=" Por favor, ingrese su numero de cuenta: \n")
        self.entradaCuenta = tki.Entry(self)
        self.entradaCuenta.configure(bg="lightblue")
        self.errorCuenta = tki.Label(self, text="", fg="red")
        self.saltodelinea= tki.Label(self, text="\n")
        self.botonContinuar= tki.Button(self, text="Continuar", command=self.controlador.buscarCuenta)
        self.botonContinuar.configure(bg="lightblue")
        self.saltodelinea1 = tki.Label(self, text="\n")
        self.etiquetaCrearcuenta = tki.Label(self, text="¿Todavia no tiene una cuenta? !Cree una¡ \n")
        self.botonCrearCuenta = tki.Button(self, text="Crear cuenta", command=self.controlador.formularioCrearCuenta)
        self.botonCrearCuenta.configure(bg="lightblue")
        self.titulo.pack()
        self.instrucciones.pack()
        self.entradaCuenta.pack()
        self.errorCuenta.pack()
        self.saltodelinea.pack()
        self.botonContinuar.pack()
        self.saltodelinea1.pack()
        self.etiquetaCrearcuenta.pack()
        self.botonCrearCuenta.pack()
    def mostrarVentanaPrincipal(self):
        self.mainloop()
    def mostrarErrorCuenta(self, mensaje):
        self.errorCuenta.configure(text=mensaje)
    #acciones de entradas o botones
    def crearCuenta(self):
        pass
    def nCuntaIngresado(self):
        nCuentaInput = self.entradaCuenta.get()
    def botonSiguiente(self):
        pass
    # definicion de titulos, labels, botones..
class CrearCuentaForm(tki.Toplevel):
    def __init__(self, controlador):
        super().__init__()
        self.title("FORMULARIO CREAR CUENTA")
        self.controlador = controlador
        self.crearElementos()
        self.geometry("300x400")
    def crearElementos(self):
        self.titulo = tki.Label(self,text="¡CREA UNA NUEVA CUENTA DE AHORROS CON NOSOTROS!")
        self.instruccion = tki.Label(self,text='¡POR FAVOR INGRESA TU NOMBRE!')
        self.salto = tki.Label(self, text="\n")
        self.entradaNombre = tki.Entry(self)
        self.salto1 = tki.Label(self, text="\n")
        self.instruccion2 = tki.Label(self,text='¡POR FAVOR INGRESE UN SALDO INICIAL!')
        self.salto2 = tki.Label(self, text="\n")
        self.entradaSaldo = tki.Entry(self)
        self.label_error = tki.Label(self, text="", fg="red")
        self.salto3 = tki.Label(self, text="\n")
        self.botonCrearCuenta = tki.Button(self, text='CREAR TU CUENTA', command=self.controlador.crearCuenta)
        self.botonCrearCuenta.configure(bg='lightblue')
        self.instruccion.pack()
        self.salto.pack()
        self.entradaNombre.pack()
        self.salto1.pack()
        self.instruccion2.pack() 
        self.salto2.pack()
        self.entradaSaldo.pack()
        self.label_error.pack() 
        self.salto3.pack()
        self.botonCrearCuenta.pack()
    def mostrarError(self, mensaje):
        self.label_error.config(text=mensaje) 
class VentanaInfoCuenta(tki.Toplevel):
    def __init__(self, controlador, cuenta):
        super().__init__()
        self.cuentaSesion = cuenta
        self.controlador = controlador
        self.title("BIENVENID@ A SU CUENTA, {0}".format(self.cuentaSesion.getTitular()))
        self.geometry("500x500")
        self.iniciarComponentes()
    def iniciarComponentes(self):
        self.tv = ttk.Treeview(self)
        self.infoCuenta = self.tv.insert("","end", text="Información de tu cuenta")
        self.tv.insert(self.infoCuenta,"end",text="TITULAR DE LA CUENTA: {0}".format(self.cuentaSesion.getTitular()))
        self.tv.insert(self.infoCuenta,"end",text="SALDO DISPONIBLE: {0}".format(self.cuentaSesion.getSaldo()))
        self.infoTransacciones = self.tv.insert("","end",text="Informacion de tus transacciones")
        transacciones = self.cuentaSesion.getHistorialTransacciones()
        if len(transacciones) == 0:
            self.tv.insert(self.infoTransacciones,"end",text="NO HAS HECHO TRANSACCIONES")
        else:
            for transaccion in transacciones:
                self.tv.insert(self.infoTransacciones,"end",text=str(transaccion))
        self.labelBoton = tki.Label(self, text="¿DESEA DEPOSITAR DINERO?")
        self.botonDepositar = tki.Button(self,text="DEPOSITAR")
        self.botonDepositar.configure(bg="lightblue")
        self.labelBoton2 = tki.Label(self,text="¿DESEA RETIRAR DINERO?")
        self.botonRetirar = tki.Button(self,text="RETIRAR",bg="lightblue")
        self.tv.pack(fill=tki.X, side=tki.TOP, padx=10, pady=10)
        self.labelBoton.pack()
        self.botonDepositar.pack()
        self.labelBoton2.pack()
        self.botonRetirar.pack()
