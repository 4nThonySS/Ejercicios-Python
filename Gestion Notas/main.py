diccionario = {}

def registrar_nota():
    nombre = input("escriba el nombre del estudiante: ").lower()
    if nombre not in diccionario:
        diccionario[nombre] = {}  

    nombre_asignatura = input("Escriba el nombre de la asignatura: ")  

    while True:
        try:
            nota_asignatura = float(input(f"Escriba la nota de {nombre} en la asignatura {nombre_asignatura}: "))  # ← CORREGIDO (Esgriba → Escriba)
        except ValueError:
            print("Error de formato.")
            input("Presione ENTER para continuar...")
            continue

        if nota_asignatura < 1 or nota_asignatura > 7:
            print("Error la nota debe estar entre 1-7.")
            input("Presione ENTER para continuar...")
            continue
        else:
            diccionario[nombre][nombre_asignatura] = {"nota": nota_asignatura}
            break  


def ver_notas():
    if len(diccionario) > 0:
        for nombre, asignaturas in diccionario.items():  
            for asignatura, datos in asignaturas.items():  
                print(f"nombre: {nombre} - N. Asignatura: {asignatura} - nota: {datos['nota']}")  # ← CORREGIDO
    else:
        print("No hay estudiantes registrados.")


def promedio_estudiante():
    if len(diccionario) > 0:
        for nombre, asignaturas in diccionario.items():  
            suma = 0  
            cantidad = 0  
            for datos in asignaturas.values():  
                suma += datos['nota']
                cantidad += 1
            promedio = suma / cantidad if cantidad > 0 else 0  
            print(f"nombre: {nombre} - promedio: {promedio:.2f}") 
    else:
        print("No hay estudiantes registrados.")


def programa():
    while True:
        print("""
                    --- MENÚ ---
            1. Registrar nota de estudiante
            2. Ver notas de un estudiante
            3. Ver promedio general por estudiante
            4. Salir
            """)
        try:
            opc_menu = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error de formato.")
            input("Presione ENTER para continuar...")
            continue
        if opc_menu not in [1, 2, 3, 4]:
            print("Error opción inválida")
            input("Presione ENTER para continuar...")
            continue
        elif opc_menu == 4:
            print("Finalizando...")
            break
        elif opc_menu == 3:
            promedio_estudiante()
        elif opc_menu == 2:
            ver_notas()
        elif opc_menu == 1:
            registrar_nota()

programa()
