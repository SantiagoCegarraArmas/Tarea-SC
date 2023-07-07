from empleado import *

def registrar(nomina):
  cedulas = []
  for empleado in nomina.empleados:
    cedulas.append(empleado.cedula)
  
  while True:
    try:
      rol = input(
        "Ingrese el rol del empleado Junior(J), Senior(S), Manager(M)):\n==> "
      ).lower()
      if rol not in ["j", "s", "m"]:
        raise Exception
      print("\n")
      break
    except:
      print("Ingrese un rol valido")

  while True:
    try:
      nombre = input("Ingrese el nombre del empleado:\n==> ")
      if not nombre.isalpha():
        raise Exception
      print("\n") 
      break
    except:
      print("Ingrese caracteres alfabeticos")

  while True:
    try:
      cedula = int(input("Ingres la cedula del empleado:\n==> "))
      print("\n")
      break
    except:
      print("Ingrese una cedula valida")

  if cedula in cedulas:
    print("El empleado ya esta registrado")
    print("\n")
  else:
    if rol == 'j':
      rol = "Junior"
      presupuesto = 50
    elif rol == 's':
      rol = "Senior"
      presupuesto = 100
    else:
      rol = "Manager"
      presupuesto = 150
  
    empleado = Empleado(rol, nombre, cedula,presupuesto)
    nomina.empleados.append(empleado)
    nomina.agregar(presupuesto)
  
    print("Empleado registrado")
    print("\n")
  
  return nomina
