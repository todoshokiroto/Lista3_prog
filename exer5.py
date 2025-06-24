import random
l1 = [random.randint(1,50) for i in range(random.randint(5,20))]
l2 = [random.randint(1,50) for i in range(random.randint(5,20))]
def intercalar_recursivo(lista1, lista2, i=0, j=0, resultado=None):
    if resultado is None:
        resultado = []

    # Verifica se ambas as listas chegaram ao fim
    if i >= len(lista1) and j >= len(lista2):
        return resultado

    # Alterna começando pela lista menor
    if len(lista1) <= len(lista2):
        if i < len(lista1):
            resultado.append(lista1[i])
            return intercalar_recursivo(lista1, lista2, i + 1, j, resultado)
        elif j < len(lista2):
            resultado.append(lista2[j])
            return intercalar_recursivo(lista1, lista2, i, j + 1, resultado)
    else:
        if j < len(lista2):
            resultado.append(lista2[j])
            return intercalar_recursivo(lista1, lista2, i, j + 1, resultado)
        elif i < len(lista1):
            resultado.append(lista1[i])
            return intercalar_recursivo(lista1, lista2, i + 1, j, resultado)

    # Se ambas ainda têm elementos, intercala
    if i < len(lista1) and j < len(lista2):
        resultado.append(lista1[i])
        resultado.append(lista2[j])
        return intercalar_recursivo(lista1, lista2, i + 1, j + 1, resultado)

    return resultado