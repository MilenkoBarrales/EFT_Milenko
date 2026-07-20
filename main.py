from funciones import *


while True:
    print("1. Stock por plataforma")
    print("2. Búsqueda de juegos por rango precio")
    print("3. Actualizar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6. Salir")

    opc = leer_opcion()
    match opc:
            case 1:

                platform = input("Ingrese plataforma: ").lower().strip()
                stock_plataforma(platform)

            case 2:
                try:
                    precio_min = int(input("Ingrese precio minimo: "))
                    precio_max = int(input("Ingrese precio maximo: "))

                except ValueError:
                    print("El tipo de dato es invalido, solo se aceptan numeros enteros")
                    precio_min = int(input("Ingrese precio minimo: "))
                    precio_max = int(input("Ingrese precio maximo: "))
                
                rango_precio(precio_min, precio_max)

            case 3:
                codigo = validar_codigo()
                precio = int(input("Ingrese precio"))
                if precio >= 0:
                    precio_actualizado = actualizar_precio(codigo, precio)

                    if precio_actualizado:
                        print("Precio actualizado con éxito")
                    else:
                        print("El código no existe")
            
            case 4:
                codigo = validar_codigo()
                titulo = validar_vacio_espacios("titulo")
                plataforma = validar_vacio_espacios("plataforma")
                genero = validar_vacio_espacios("genero")
                clasificacion = validar_clasificacion()
                multiplayer = validar_multiplayer()
                editor = validar_vacio_espacios("editor")
                precio = validar_precio()
                stock = validar_stock()

                if (codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock):
                    agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock != True)
                    print("El código ya existe")
                else:
                    print("Juego agregado con exito")
                    
            case 5:
                codigo = validar_codigo()
                eliminar_juego(codigo)
            case 6:
                print("Programa Finalizado")
                break