from nomina import *
from gestion_empleado import *
from gestion_pago import *

def main():
  print("Arreglo arreglado")
  print("Version final")
  nomina = Nomina([], 0, 10000)
  while True:
    print("Bienvenidos")
    print("\n")
    while True:
      try:
        option = int(
          input(
            "Ingresa la opcion que deseee realizar:\n1.-Registrar empleado\n2.-Pagar empleados de la nomina\n3.-Salir\n==> "
          ))
        if option not in range(1, 4):
          raise Exception
        break
      except:
        print("Ingresa un valor valido")
        print("\n")

    if option == 1:
      print("\n")
      db = registrar(nomina)
      nomina.mostrar()
      print("\n")
      pass
    elif option == 2:
      print("\n")
      if len(nomina.empleados) == 0:
        print("No hay empleados registrados")
      else:
        nomina = pago(nomina)
        print("Mostrar cambios en los empleados y nomina")
        nomina.mostrar()
        print(f"Empleados: {nomina.empleados}\nPresupuesto:{nomina.presupuesto}\nDinero disponible:{nomina.dinero}")
      print("\n")
    else:
      print("\n")
      print("Hasta Pronto")
      break


main()
