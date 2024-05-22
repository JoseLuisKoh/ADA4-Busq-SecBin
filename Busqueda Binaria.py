

def busqueda_binaria(arr, objetivo):
    inicio = 0
    fin = len(arr) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1

def main_binaria():
    numeros = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
    numeros.sort()  
    objetivo = int(input("Ingrese el número a buscar: "))

    resultado = busqueda_binaria(numeros, objetivo)

    if resultado != -1:
        print(f"El elemento {objetivo} se encuentra en la posición {resultado} usando Búsqueda Binaria.")
    else:
        print(f"El elemento {objetivo} no se encuentra en la lista usando Búsqueda Binaria.")

if __name__ == "__main__":
    main_binaria()
