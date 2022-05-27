from datetime import date
import pandas as pd

class Usuario:
	def __init__(self, idUsuario, nombre, nombreUsuario, contrasena, fechaRegistro):
		self.idUsuario = idUsuario
		self.nombre = nombre
		self.nombreUsuario = nombreUsuario
		self.contrasena = contrasena
		self.fechaRegistro = fechaRegistro

	def crearUsuario(self, ):
		pass

	def borarUsuario(self, ):
		pass

	def verificarUsuario(self, ):
		pass

	def iniciarSesion(self, ):
		pass

usuario1 = Usuario(1, 'Carlos Serrano', 'carlos123', '123carlos', date.today())
usuario2 = Usuario(2, 'Andres Cano', 'andres456', '123456', date.today())
print('------Usuarios------')
print('id:',usuario1.idUsuario,'nombre:',usuario1.nombre,'nombre usuario:',usuario1.nombreUsuario,'contraseña:',usuario1.contrasena,'fecha registro:',usuario1.fechaRegistro)
print('id:',usuario2.idUsuario,'nombre:',usuario2.nombre,'nombre usuario:',usuario2.nombreUsuario,'contraseña:',usuario2.contrasena,'fecha registro:',usuario2.fechaRegistro)


	

