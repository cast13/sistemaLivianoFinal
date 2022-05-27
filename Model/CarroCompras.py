from datetime import date

class CarroCompras:
	def __init__(self, idCarro, idCliente, idCotizacion, fechaCreacion, estadoCarro):
		self.idCarro = idCarro
		self.idCliente = idCliente
		self.idCotizacion = idCotizacion
		self.fechaCreacion = fechaCreacion
		self.estadoCarro = estadoCarro

	def crearCarroCompras(self, ):
		pass

	def eliminarCarroCompras(self, ):
		pass

	def agregarProductoCarro(self, ):
		pass

	def borrarProductoCarro(self, ):
		pass

carroCompras = CarroCompras(1, 1, 1, date.today(), True)
print('----Carro Compras----')
print('id:',carroCompras.idCarro,'id cliente:',carroCompras.idCliente,'id cotizacion:',carroCompras.idCotizacion,'fecha creacion:',carroCompras.fechaCreacion,'estado carro:',carroCompras.estadoCarro)