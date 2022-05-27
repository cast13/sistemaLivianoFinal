class Producto:
	def __init__(self, idProducto, nombreProducto, codigoProducto, valor, descripcionProducto):
		self.idProducto = idProducto
		self.nombreProducto = nombreProducto
		self.codigoProducto = codigoProducto
		self.valor = valor
		self.descripcionProducto = descripcionProducto

	def crearProducto(self, ):
		pass

	def borrarProducto(self, ):
		pass

producto = Producto(1,'superboard','sboard',100,'un superboard')
print('----Producto----')
print('id:',producto.idProducto,'nombre:',producto.nombreProducto,'codigo:',producto.codigoProducto,'valor:',producto.valor,'descripcion:',producto.descripcionProducto)