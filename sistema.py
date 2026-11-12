from menu import mostrar_menu
from gestion_stock import cargar_stock, mostrar_stock, contar, stock_cantidades, inicializar

inicializar()

while True:
    opcion = mostrar_menu()

    if opcion == "1":
        cargar_stock()
    elif opcion == "2":
        mostrar_stock()
    elif opcion == "3":
        categoria = input("categoria: ")
        if categoria in stock_cantidades:
            contar(stock_cantidades[categoria])
        else:
            print("categoria incorrecta")
    elif opcion == "4":
        break
    else:
        print("opcion incorrecta")

