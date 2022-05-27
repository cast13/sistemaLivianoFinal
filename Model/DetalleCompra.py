class DetalleCompra:
	def __init__(self, idDetalleCompra, idCarro, idProducto, cantidadCompra):
		self.idDetalleCompra = idDetalleCompra
		self.idCarro = idCarro
		self.idProducto = idProducto
		self.cantidadCompra = cantidadCompra

	def verificarExistenciaProducto(self, ):
		pass

detalleCompra = DetalleCompra(1, 1, 1, 2)
print('----Detalle de Compra----')
print('id:',detalleCompra.idDetalleCompra,'id carro:',detalleCompra.idCarro,'id producto:',detalleCompra.idProducto,'cantidad compra:',detalleCompra.cantidadCompra)