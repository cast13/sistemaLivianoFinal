from Administrador import Administrador
from Usuario import Usuario
from Cliente import Cliente
from Producto import Producto
from Cotizacion import Cotizacion
from CarroCompras import CarroCompras
from Envio import Envio
from Factura import Factura
from DetalleCompra import DetalleCompra
from InformacionEnvio import InformacionEnvio
from exportarDatos import exportarDatos


def main():
    Usuario()
    Administrador()
    Cliente()
    Cotizacion()
    CarroCompras()
    DetalleCompra()
    Producto()
    Factura()
    Envio()
    InformacionEnvio()
    exportarDatos()