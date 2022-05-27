from datetime import date

class Cotizacion:
	def __init__(self, idCotizacion, idCliente, tipoCotizacion, fechaCotizacion, detalleCotizacion):
		self.idCotizacion = idCotizacion
		self.idCliente = idCliente
		self.tipoCotizacion = tipoCotizacion
		self.fechaCotizacion = fechaCotizacion
		self.detalleCotizacion = detalleCotizacion

	def crearCarroComprasCotizacion(self, ):
		pass

cotizacion = Cotizacion(1, 1, 'estructura liviana', date.today(), 'detalle')
print('----Cotizacion----')
print('id:',cotizacion.idCotizacion,'id cliente:',cotizacion.idCliente,'tipo cotizacion:',cotizacion.tipoCotizacion,'fecha cotizacion:',cotizacion.fechaCotizacion,'detalle cotizacion:',cotizacion.detalleCotizacion)