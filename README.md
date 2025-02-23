Documentación del Sistema Bancario BancUAM
Sistema bancario simple implementado con Python y Tkinter que incluye interfaz gráfica.

Clases Principales
[CuentaBancaria](Estructuras de Datos/ejercicioParcial/cuentaBancaria.py)
Representa una cuenta bancaria individual con:

Nombre del titular
Saldo
Número de cuenta (formato: CJPPD-XXX)
Historial de transacciones
[Banco](Estructuras de Datos/ejercicioParcial/banco.py)
Administra todas las cuentas bancarias y transacciones:

Creación de cuentas
Depósitos (mínimo $10.000)
Retiros
Transferencias entre cuentas
Consultas de cuenta
[ControladorCuentas](Estructuras de Datos/ejercicioParcial/controlador.py)
Controlador que conecta la interfaz de usuario con la lógica bancaria:

Inicializa el banco y la interfaz principal
Maneja todas las interacciones del usuario
Gestiona formularios y ventanas
Control de errores
Clases de Interfaz de Usuario
[BancoUi](Estructuras de Datos/ejercicioParcial/bancoUi.py)
Ventana principal de la aplicación:

Inicio de sesión con número de cuenta
Opción de crear nueva cuenta
Visualización de errores
Otros Formularios
[CrearCuentaForm](Estructuras de Datos/ejercicioParcial/bancoUi.py) - Creación de cuenta nueva
[VentanaInfoCuenta](Estructuras de Datos/ejercicioParcial/bancoUi.py) - Panel de cuenta
[formularioDepositarDinero](Estructuras de Datos/ejercicioParcial/bancoUi.py) - Formulario de depósito
[formularioRetirarDinero](Estructuras de Datos/ejercicioParcial/bancoUi.py) - Formulario de retiro
[FormularioTransferirDinero](Estructuras de Datos/ejercicioParcial/bancoUi.py) - Formulario de transferencia
Características Principales
Gestión de Cuentas

Crear nuevas cuentas
Ver detalles de cuenta
Consultar historial de transacciones
Transacciones

Depósitos (mínimo $10.000)
Retiros (con validación de saldo)
Transferencias entre cuentas
Seguridad

Validación de entradas
Manejo de errores
Funcionalidad de salida segura
Interfaz de Usuario

GUI limpia e intuitiva
Formularios responsivos
Mensajes de error
Confirmación de transacciones

Uso
La aplicación iniciará mostrando la ventana principal de inicio de sesión donde los usuarios pueden:

Iniciar sesión con cuenta existente
Crear nueva cuenta
Realizar transacciones
Ver detalles e historial de cuenta