from datetime import date

class Factura:
	def __init__(self, idFactura, idCarro, fechaFactura, valorTotalCompra, cantidadProductosComprados):
		self.idFactura = idFactura
		self.idCarro = idCarro
		self.fechaFactura = fechaFactura
		self.valorTotalCompra = valorTotalCompra
		self.cantidadProductosComprados = cantidadProductosComprados

	def calcularValorPorCantidad(self, ):
		pass

factura = Factura(1, 1, date.today(), 100, 2)
print('----Factura----')
print('id:',factura.idFactura,'id carro:',factura.idCarro,'fecha:',factura.fechaFactura,'valor total:',factura.valorTotalCompra,'cantidad productos:',factura.cantidadProductosComprados)