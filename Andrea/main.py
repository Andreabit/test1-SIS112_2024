

from simulaciondeexamen import ingresar_matriz, mostrar_matriz, suma_total, suma_filas_columnas, maximo_minimo

def main():
    
    matriz = ingresar_matriz()
    
    mostrar_matriz(matriz)
    
    total = suma_total(matriz)
    print(f"\nSuma total de los elementos: {total}")
    
    suma_filas, suma_columnas = suma_filas_columnas(matriz)
    print(f"Suma de cada fila: {suma_filas}")
    print(f"Suma de cada columna: {suma_columnas}")
    
    maximo, minimo = maximo_minimo(matriz)
    print(f"\nNúmero máximo: {maximo}")
    print(f"Número mínimo: {minimo}")

if __name__ == "__main__":
    main()
