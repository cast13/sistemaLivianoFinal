from Usuario import Usuario

class Administrador(Usuario):
	def __init__(self, idAdministrador, cargo, estado):
		self.idAdministrador = idAdministrador
		self.cargo = cargo
		self.estado = estado

	def verificarAdministrador(self, ):
		pass

	def modificarProducto(self, ):
		pass

administrador = Administrador(2, 'Administrador', True)
print('----Administrador----')
print('id:',administrador.idAdministrador,'cargo:',administrador.cargo,'estado:',administrador.estado)