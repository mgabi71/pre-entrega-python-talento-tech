medication_stock = []
id_actual = 1

while True:
    print("\n-----Menu-----")
    print("1. Agregar un medicamento")
    print("2. Mostrar un medicamento")
    print("3. Buscar un medicamento")
    print("4. Eliminar un medicamento")
    print("5. Exit")

    option = input("Seleccione una opción (1-5): ")

    if option not in ["1", "2", "3", "4", "5"]:
        print("Opción inválida, seleccione una opción (1-5)")
        continue

# 1. AGREGAR

    if option == "1":
        name = input("Nombre de Medicamento: ")
        category = input("Categoría de Medicamento: ")
        price = input("Precio de Medicamento: ")

# 2. VALIDACIONES BÁSICAS

        if name == "" or category == "" or price == "":
            print("Datos inválidos")
            continue

        if not price.isdigit(): 
            print("El precio debe ser un dígito")
            continue

        medication = [id_actual, name, category, int(price)]
        medication_stock.append(medication)        
        id_actual += 1
        print("Producto agregado con éxito")

# 2. VER
    elif option == "2":
        if len(medication_stock) == 0:
            print("No hay productos disponibles")
        else:
            for i in range (len(medication_stock)):
                medication = medication_stock[i]
                print(f"{i+1}. ID:{medication[0]} | {medication[1]} | {medication[2]} | ${medication[3]}")

# 3. BUSCAR
    elif option == "3":
        search = input("Buscar por nombre: ")

        finded = False

        for medication in medication_stock:
            if search.lower() in medication[1].lower():
                print(f"ID:{medication[0]} | {medication[1]} | {medication[2]} | ${medication[3]}")
                finded = True

        if not finded:
            print("No se encontraron resultados")

# 4. ELIMINAR

    elif option == "4":
        if len(medication_stock) == 0:
            print("No hay medicamentos para eliminar.")
            continue

        for i, medication in enumerate(medication_stock):
            print(f"{i+1}. {medication[1]}")

        erase = input("Ingrese el número de medicamento a eliminar: ")

        if not erase.isdigit():
            print("El dato es inválido.")
            continue

        erase = int(erase)

        if erase < 1 or erase > len(medication_stock):
            print("El número está fuera de rango")
            continue

        medication_stock.pop(erase - 1)
        print("Medicamento eliminado exitosamente.")
        
# 5. SALIR

    elif option == "5":
        print("Fin del programa.")
        break
        
 