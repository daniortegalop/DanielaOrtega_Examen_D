#sistema de gestión de empleados
lista_empleados = []
def menu_principal():
    print("""========== MENÚ PRINCIPAL ==========
1. Agregar empleado
2. Buscar empleado
3. Eliminar empleado
4. Actualizar estado
5. Mostrar empleados
6. Salir
=====================================
    """)
def obtener_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Opción inválida, ingrese un número entre 1 y 6")
        except ValueError:
            print("Opción inválida, ingrese valor numérico entre 1 y 6")
#validaciones
def validar_nombre(nombre):
    return nombre.strip() != ""
def validar_edad(edad):
    return edad > 0
def validar_salario(salario):
    return salario > 0

def agregar_empleado(lista_empleados):
    nombre = input("Ingrese nombre del empleado: ")
    if not validar_nombre(nombre):
        print("El nombre no puede estar vacio")
        return
    try:
        edad = int(input("Ingrese edad: "))
        if not validar_edad(edad):
            print("La edad debe ser un número entero mayor que 0")
            return
    except ValueError:
        print("La edad debe ser un número entero mayor que 0")
        return
    try:
        salario = float(input("Ingrese salario: "))
        if not validar_salario(salario):
            print("El salario debe ser un número decimal mayor que 0")
            return
    except ValueError:
        print("El salario debe ser un número decimal mayor que 0")
        return
    empleado = {
        "nombre": nombre,
        "edad": edad,
        "salario": salario,
        "activo": False,
    }
    lista_empleados.append(empleado)

def buscar_empleado(lista_empleados, nombre):
    for i in range(len(lista_empleados)):
        if lista_empleados[i]["nombre"] == nombre:
            return i
    return -1
def eliminar_empleado(lista_empleados, nombre):
    posicion = buscar_empleado(lista_empleados, nombre)
    if posicion != -1:
        lista_empleados.pop(posicion)
    else:
        print(f"El empleado {nombre} no se encuentra registrado.")

def actualizar_empleados(lista_empleados):
    for empleado in lista_empleados:
        if empleado["edad"] >= 18:
            empleado["activo"] = True
        else:
            empleado["activo"] = False

def mostrar_empleados(lista_empleados):
    actualizar_empleados(lista_empleados)

    print("=== LISTA DE EMPLEADOS ===")
    for empleado in lista_empleados:
        print(f"Nombre: {empleado["nombre"]}")
        print(f"Edad: {empleado["edad"]}")
        print(f"Salario: {empleado["salario"]}")
        if empleado["activo"] == True:
            print("Estado: ACTIVO")
        else:
            print("Estado: INACTIVO")
        print("********************************************")


def ejecutar_programa():
    while True:
        menu_principal()
        opcion = obtener_opcion()
        match opcion:
            case 1:
                agregar_empleado(lista_empleados)
            case 2:
                nombre = input("Ingrese nombre del empleado a buscar: ")
                posicion = buscar_empleado(lista_empleados, nombre)
                if posicion != -1:
                    print(f"Empleado encontrado en posicion {posicion}: {lista_empleados[posicion]}")
                else:
                    print(f"Empleado {nombre} no encontrado en el registro.")
            case 3:
                nombre = input("Ingrese nombre del empleado a eliminar: ")
                eliminar_empleado(lista_empleados, nombre)
            case 4:
                actualizar_empleados(lista_empleados)
            case 5:
                mostrar_empleados(lista_empleados)
            case 6:
                print("Gracias por usar el sistema. Vuelva Pronto")
                break

ejecutar_programa()
