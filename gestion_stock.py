stock_productos = {'enlatados': [], 'frutas': [], 'congelados': [], 'panaderia': []}
stock_cantidades = {'enlatados': [], 'frutas': [], 'congelados': [], 'panaderia': []}

def inicializar():
    for categoria in stock_productos:
        stock_productos[categoria] = []
    for categoria in stock_cantidades:
        stock_cantidades[categoria] = []

def cargar_stock():
    categoria = input("categoria: ")
    if categoria in stock_productos:
        producto = input("producto: ")
        cantidad = int(input("cantidad: "))
        stock_productos[categoria].append(producto)
        stock_cantidades[categoria].append(cantidad)
    else:
        print("categoria incorrecta")

def mostrar_stock():
    for categoria in stock_productos:
        print(categoria)
        for i in range(len(stock_productos[categoria])):
            print(stock_productos[categoria][i], stock_cantidades[categoria][i])

def contar(lista_productos):
    suma = 0
    for cantidad in lista_productos:
        suma = suma + cantidad
    print("cantidad de productos:", len(lista_productos))
    print("suma de cantidades:", suma)
