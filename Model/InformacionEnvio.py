from datetime import date

class InformacionEnvio:
	def __init__(self, idInformacionEnvio, idEnvio, direccionEnvio, telefonoContacto, descripcionEntrega, fechaEstimadaEntrega):
		self.idInformacionEnvio = idInformacionEnvio
		self.idEnvio = idEnvio
		self.direccionEnvio = direccionEnvio
		self.telefonoContacto = telefonoContacto
		self.descripcionEntrega = descripcionEntrega
		self.fechaEstimadaEntrega = fechaEstimadaEntrega

	def modificarInformacionEnvio(self, ):
		pass

infoEnvio = InformacionEnvio(1, 1, 'Calle 1', '12345678', 'entrega en domicilio', date.today())
print('----Informacion de envio----')
print('id:',infoEnvio.idInformacionEnvio,'id envio:',infoEnvio.idEnvio,'direccion:',infoEnvio.direccionEnvio,'telefono:',infoEnvio.telefonoContacto,'descripcion:',infoEnvio.descripcionEntrega,'fecha estimada:',infoEnvio.fechaEstimadaEntrega)