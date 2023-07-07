from empleado import *


class Nomina:

  def __init__(self, empleados, presupuesto, cantidad):
    self.empleados = empleados
    self.presupuesto = presupuesto
    self.dinero = cantidad

  def mostrar(self):
    for empleado in self.empleados:
      empleado.printempleado()
      print("\n")

  def pagar_e(self, pago):
    self.dinero -= pago

  def agregar(self, pago):
    self.presupuesto += pago
