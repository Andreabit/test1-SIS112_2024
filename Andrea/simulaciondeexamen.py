

def ingresar_matriz():
    matriz = []
    print("Ingrese los elementos de la matriz (3x3):")
    for i in range(3):
        fila = []
        for j in range(3):
            valor = int(input(f"Elemento [{i+1},{j+1}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    print("Matriz ingresada:")
    for fila in matriz:
        print(" ".join(map(str, fila)))

def suma_total(matriz):
    total = sum(sum(fila) for fila in matriz)
    return total

def suma_filas_columnas(matriz):
    suma_filas = [sum(fila) for fila in matriz]
    suma_columnas = [sum(matriz[i][j] for i in range(3)) for j in range(3)]
    return suma_filas, suma_columnas

def maximo_minimo(matriz):
    maximo = max(max(fila) for fila in matriz)
    minimo = min(min(fila) for fila in matriz)
    return maximo, minimo
