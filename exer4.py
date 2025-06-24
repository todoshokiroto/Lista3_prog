import random
lista = [random.randint(1,100) for i in range(100)]
def media(arr):
    soma = 0
    for i in range(len(arr)):
        soma += arr[i]
    return soma/len(arr)

def prox_media(arr):
    m_lista = media(arr)
    n_prox = 10000000000
    dif = 10000000000
    for j in range(len(arr)):
        if abs(abs(arr[j]) - abs(m_lista)) < dif:
            prox = arr[j]
            dif = abs(abs(arr[j]) - abs(m_lista))
    return prox

print(lista)
print(media(lista))
print(prox_media(lista))
