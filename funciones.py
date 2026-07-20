juegos = {
    'g001': ['Eclipse Runner', 'pc', 'accion', 'T', True,
    'NovaStudio'],
    'g002': ['Puzzle Atlas', 'switch', 'puzzle', 'E', False,
    'BrightWorks'],
    'g003': ['Sky Legends', 'ps5', 'aventura', 'T', True,
    'OrionGames'],
    'g004': ['Racing Pulse', 'pc', 'carreras', 'E', True,
    'VelocityLab'],
    'g005': ['Mystic Farm', 'switch', 'simulacion', 'E', False,
    'GreenSeed'],
    'g006': ['Shadow Tactics', 'xbox', 'estrategia', 'M', False,
    'IronGate'],
}

inventario = {
    'g001': [9990, 7],
    'g002': [19990, 0],
    'g003': [42990, 3],
    'g004': [14990, 5],
    'g005': [17990, 9],
    'g006': [39990, 2],
}



def validar_codigo():
    codigo = input("Ingrese codigo: ").strip().lower()

    if codigo == "":
        print("El codigo no puede estar vacío")
        return False, None
    
    return codigo, True
    
    
def leer_opcion():
    try:
        opc = int(input("Ingrese opcion: "))
        if 1 <= opc <= 6:
            return opc
    except ValueError:
        print("Tipo de dato invalido")

def validar_vacio_espacios(texto):
    text = input(f"Ingrese {texto} del juego: ").strip().lower()

    if text == "":
        print(f"El {texto} no puede estar vacio")
        return False, None

    return True, text

def validar_clasificacion():
    opc = ["e", "t", "m"]
    clasificacion = input("Ingrese clasificacion E - T- M: ").lower().strip()

    if clasificacion == "":
        print("La clasificacion no puede estar vacía")
        return False, None
    
    if clasificacion in opc:
        return True, clasificacion
    
def validar_multiplayer():
    multi = input("El juego es multiplayer? s/n: ").strip().lower()

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
        
        if plataforma == plataforma_juego:
            stock_disponible = inventario[codigo][1]
            total_stock += stock_disponible
    
    print(f"El stock de la plataforma {plataforma} es: {total_stock}")
    return total_stock
    
def rango_precio(p_min, p_max):
    

    if p_min >= 0 and p_max >= 0:
        for codigo , dato in juegos.items():
            nombre_juego = dato[0]
            stock_valido = inventario[codigo][1]

            if stock_valido != 0 and p_min <= p_max:
                codigo_inventario = inventario[codigo]
                lista_precios = []
                lista_precios.append([codigo_inventario, nombre_juego])
                for juego in lista_precios:
                    print(f"{juego[1]}--{codigo}")
                    lista_precios = []

def buscar_codigo(codigo):
    for code in inventario:
        if codigo in inventario == code:
            return False
        else:
            return True
        
def actualizar_precio(codigo, nuevo_precio):
    codigo_valido = buscar_codigo(codigo)

    if codigo_valido:
        for code in inventario.items():
            inventario[code][0] = nuevo_precio
            return True
    else:
        return False
    

def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock):

    if codigo == "":
        return False, None
    
    if codigo in inventario or codigo in juegos:
        print("El codigo ya existe")
        return False, None
    
    juegos[codigo] = [titulo, plataforma, genero, clasificacion, multiplayer, editor]

    inventario[codigo] = [precio, stock]

    return True

def eliminar_juego(codigo):
    codigo_valido = buscar_codigo(codigo)
    print(codigo_valido)
    

