from main import juegos, inventario

def validar_codigo():
    codigo = input("Ingrese codigo: ").strip().lower()

    if codigo == "":
        print("El codigo no puede estar vacío")
        return False, None

    if codigo in juegos or codigo in inventario:
        print("El código ya existe en los invenatarios")
        return False, None
    
    else:
        return True, codigo
    

def validar_vacio_espacios(texto):
    text = input(f"Ingrese {texto} del juego:").strip().lower()

    if text == "":
        print(f"El {texto} no puede estar vacio")
        return False, None

    return True, text

def validar_clasificacion():
    opc = ["e", "t", "m"]
    clasificacion = input("Ingrese clasificacion: E - T- M").lower().strip()

    if clasificacion == "":
        print("La clasificacion no puede estar vacía")
        return False, None
    
    if clasificacion in opc:
        return True, clasificacion
    
def validar_multiplayer():
    multi = input("El juego es multiplayer? s/n:").strip().lower()

    if multi == "s":
        multi = True
        return True, multi
    elif multi == "n":
        multi = False
        return True, multi
    
def validar_precio():
    try:
        precio = int(input("Ingrese precio del juego: "))
        if precio > 0:
            return True, precio
        else:
            print("El precio debe de ser mayor a 0")
    except ValueError:
        print("Tipo de dato invalido.")

def validar_stock():
    try:
        stock = int(input("Ingrese stock: "))

        if stock >= 0:
            return True, stock
        
        else:
            print("El stock no puede ser negativo y debe de ser un numero entero")
            return False, None
    except ValueError:
        print("El tipo de dato ingresado es invalido, solo se aceptan numeros enteros")


def stock_plataforma(plataforma):
    total_stock = 0

    for codigo, datos_juego in juegos.items():
        plataforma_juego = datos_juego[1]

        if plataforma_juego == plataforma:
            stock_plataforma = inventario[codigo][1]
            total_stock += stock_plataforma

        print(f"El total de stock para la plataforma {plataforma} es: {total_stock}")
        return total_stock
    
def rango_precio(p_min, p_max):
    lista_precios = []

    if p_min >= 0 and p_max >= 0:
        for codigo , dato in inventario.items():
            nombre_juego = dato[0]
            stock_valido = inventario[codigo][1]
            codigo_inventario = inventario[codigo]

            if stock_valido != 0 and p_min <= p_max:
                lista_precios.append(codigo_inventario, nombre_juego)

            else:
                print("No hay juegos en ese rango de precio o el juego no esta disponible")
        
        for juego in lista_precios:
            print(f"{juego[1]}--{juego[0]}")


def buscar_codigo(codigo):
    codigo = codigo.lower()
    for code in inventario:
        if code == codigo:
            return True
        else:
            return False, None
    
def actualizar_precio(codigo, nuevo_precio):
    codigo_valido = buscar_codigo(codigo)

    if codigo_valido:
        for code, precio in inventario.items():
            inventario[code][0] = nuevo_precio
            return True
    else:
        return False
    

def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock):

    if codigo in inventario or codigo in juegos:
        return False, f"El {codigo} ya esta registrado"
    
    else:
        juegos[codigo] = [titulo, plataforma, genero, clasificacion, multiplayer, editor]

        inventario[codigo] = [precio, stock]

        return True

def eliminar_juego(codigo):
    codigo_valido = buscar_codigo(codigo)

    if codigo_valido:
        juegos.remove(codigo_valido)
        inventario.remove(codigo_valido)
        return True

    else:
        return False
    

