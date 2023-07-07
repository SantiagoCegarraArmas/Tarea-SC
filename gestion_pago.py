from empleado import *
from nomina import *

def pago(nomina):
  pago = 0
  for empleado in nomina.empleados:
    pago += empleado.salario

  if nomina.dinero > nomina.presupuesto:
    for empleado in nomina.empleados:
      empleado.pagar(empleado.salario)
    nomina.pagar_e(pago)
    print('Pagos realizados')
  else:
    print("No se ha podido realizar ningun pago porque no se cuenta con el dinero disponible")

  return nomina