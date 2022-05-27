from datetime import date

class Envio:
	def __init__(self, idEnvio, idCarro, fechaEnvio, valorTotalCompra, cantitadTotalCompra):
		self.idEnvio = idEnvio
		self.idCarro = idCarro
		self.fechaEnvio = fechaEnvio
		self.valorTotalCompra = valorTotalCompra
		self.cantitadTotalCompra = cantitadTotalCompra

	def rastrearPedido(self, ):
		pass

envio = Envio(1, 1, date.today(), 100, 2)
print('----Envio----')
print('id:',envio.idEnvio,'id carro:',envio.idCarro,'fecha:',envio.fechaEnvio,'valor total:',envio.valorTotalCompra,'cantidad total:',envio.cantitadTotalCompra)
