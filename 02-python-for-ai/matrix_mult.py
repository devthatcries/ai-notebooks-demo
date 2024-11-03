def multiplicar_matrices(matriz_a, matriz_b):
    # Verifica si el número de columnas de la primera matriz es igual al número de filas de la segunda
    if len(matriz_a[0]) != len(matriz_b):
        print("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")
        return -1

    # Inicializa la matriz resultado con ceros
    num_filas = len(matriz_a)
    num_cols = len(matriz_b[0])
    resultado = []
    for i in range(num_filas):
        fila = []
        for j in range(num_cols):
            fila.append(0)
        resultado.append(fila)

    # Realiza la multiplicación de matrices
    for i in range(len(matriz_a)):
        for j in range(len(matriz_b[0])):
            for k in range(len(matriz_b)):
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]

    return resultado


