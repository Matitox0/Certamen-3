import os

vehiculos = []

def registrar_vehiculo():
    marca = input("Ingrese la marca del vehiculo: ")
    año = int(input("Ingrese el año de fabricacion del vehiculo: "))
    kilometraje = int(input("Ingrese el kilometraje del vehiculo: "))
    costo_reparacion = float(input("Ingrese el costo de reparacion estimado: "))
    
    impuesto_servicio = costo_reparacion * 0.08
    costo_total = costo_reparacion + impuesto_servicio
    
    vehiculo = {
        'marca': marca,
        'año': año,
        'kilometraje': kilometraje,
        'costo_reparacion': costo_reparacion,
        'impuesto_servicio': impuesto_servicio,
        'costo_total': costo_total
    }
    
    vehiculos.append(vehiculo)
    print("Vehiculo registrado!")

def listar_vehiculos():
    if not vehiculos:
        print("No hay vehiculos registrados.")
    else:
        for i, vehiculo in enumerate(vehiculos, start=1):
            print(f"Vehiculo {i}:")
            print(f"  Marca: {vehiculo['marca']}")
            print(f"  Año de fabricacion: {vehiculo['año']}")
            print(f"  Kilometraje: {vehiculo['kilometraje']}")
            print(f"  Costo de reparación estimado: {vehiculo['costo_reparacion']}")
            print(f"  Impuesto de servicio: {vehiculo['impuesto_servicio']}")
            print(f"  Costo total a pagar: {vehiculo['costo_total']}\n")

def imprimir_orden_reparacion():
    filtro = input("¿Desea filtrar por marca? [SI/NO]: ").strip().lower()
    if filtro == 'SI':
        marcas_predefinidas = ['Toyota', 'Ford', 'Chevrolet']
        print("Marcas disponibles para filtrar:", ", ".join(marcas_predefinidas))
        marca_filtro = input("Ingrese la marca por la que desea filtrar: ").strip()
        
        vehiculos_filtrados = [v for v in vehiculos if v['marca'].lower() == marca_filtro.lower()]
        
        if not vehiculos_filtrados:
            print("No hay vehiculos con el filtro de marca.")
            return
    else:
        vehiculos_filtrados = vehiculos
    
    with open('orden_reparacion.txt', 'w') as file:
        for vehiculo in vehiculos_filtrados:
            file.write(f"Marca: {vehiculo['marca']}\n")
            file.write(f"Año de fabricacion: {vehiculo['año']}\n")
            file.write(f"Kilometraje: {vehiculo['kilometraje']}\n")
            file.write(f"Costo de reparacion estimado: {vehiculo['costo_reparacion']}\n")
            file.write(f"Impuesto de servicio: {vehiculo['impuesto_servicio']}\n")
            file.write(f"Costo total a pagar: {vehiculo['costo_total']}\n")
            file.write("\n")
    print("¡¡¡Orden de reparacion impresa exitosamente!!!")

def menu():
    while True:
        print("\n---------Taller de Mecanica Automotriz---------")
        print("1. Registrar vehiculo")
        print("2. Listar todos los vehiculos registrados")
        print("3. Imprimir orden de reparacion")
        print("4. Salir del programa")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == '1':
            registrar_vehiculo()
        elif opcion == '2':
            listar_vehiculos()
        elif opcion == '3':
            imprimir_orden_reparacion()
        elif opcion == '4':
            print("Nos vemos pronto.")
            break
        else:
            print("Opcion erronea, intentelo nuevamente.")

if __name__ == "__main__":
    menu()