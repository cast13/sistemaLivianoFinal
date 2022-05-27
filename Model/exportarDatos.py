import pandas as pd
from datetime import date

from Usuario import Usuario
from Cliente import Cliente

class exportarDatos:
    def __init__(self):
        pass

    def imprimirClientesCSV():
        print('imprimiendo clientes en archivo plano')
        clientes = []
        clientes.append(Cliente(1, 'Calle 1', 'cliente@correo.com', '12345678'))
        clientes.append(Cliente(2, 'Calle 2', 'cliente2@correo.com', '12345679'))
        clientes.append(Cliente(3, 'Calle 3', 'cliente3@correo.com', '22345679'))
        pd.DataFrame([cliente.__dict__ for cliente in clientes]).to_csv('./archivosPlanos/clientes.csv', index=False)

    def imprimirUsuariosCSV():
        print('imprimiendo usuarios en archivo plano')
        usuarios = []
        usuarios.append(Usuario(1, 'Carlos Serrano', 'carlos123', '123carlos', date.today()))
        usuarios.append(Usuario(2, 'Andres Cano', 'andres456', '123456', date.today()))
        pd.DataFrame([usuario.__dict__ for usuario in usuarios]).to_csv('./archivosPlanos/usuarios.csv', index=False)


exportarDatos.imprimirClientesCSV()
exportarDatos.imprimirUsuariosCSV()