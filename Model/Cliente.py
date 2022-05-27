from Usuario import Usuario

class Cliente(Usuario):
	def __init__(self, idCliente, direccion, correoElectronico, numeroDocumento):
		self.idCliente = idCliente
		self.direccion = direccion
		self.correoElectronico = correoElectronico
		self.numeroDocumento = numeroDocumento

	def agregarProductoCarro(self, ):
		pass

	def borrarProductoCarro(self, ):
		pass

	def verificarCliente(self, ):
		pass

	def realizarPedido(self, ):
		pass

cliente = Cliente(1, 'Calle 1', 'cliente@correo.com', '12345678')
print('----Cliente----')
print('id:',cliente.idCliente,'direccion:',cliente.direccion,'correo electronico:',cliente.correoElectronico,'numero documento:',cliente.numeroDocumento)