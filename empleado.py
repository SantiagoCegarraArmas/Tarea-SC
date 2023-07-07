class Empleado():

  def __init__(self, rol, nombre, cedula,salario):
    self.rol = rol
    self.nombre = nombre
    self.cedula = cedula
    self.salario = salario
    self.balance = 0

  def retirar(self):
    self.balance = 0

  def pagar(self, pago):
    self.balance += pago

  def printempleado(self):
    print(f"Nombre: {self.nombre}\nRol: {self.rol}\nCedula {self.cedula}\nSalario = {self.salario}\nbalance: {self.balance}\n")