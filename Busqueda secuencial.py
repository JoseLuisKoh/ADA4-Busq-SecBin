
def busqueda_secuencial(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i
    return -1

def main_secuencial():
    numeros = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
    objetivo = int(input("Ingrese el número a buscar: "))

    resultado = busqueda_secuencial(numeros, objetivo)

    if resultado != -1:
        print(f"El elemento {objetivo} se encuentra en la posición {resultado} usando Búsqueda Secuencial.")
    else:
        print(f"El elemento {objetivo} no se encuentra en la lista usando Búsqueda Secuencial.")

if __name__ == "__main__":
    main_secuencial()
