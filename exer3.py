import math
a = [int(input()) for i in range(int(input()))]
# 3 - A 
def troca_lista(lista,i = 0):
    #caso base
    if i == math.floor(float(len(lista))/2):
        lista[i],lista[len(lista)-1-i] = lista[len(lista)-1-i],lista[i]
    else:
        lista[i],lista[len(lista)-1-i] = lista[len(lista)-1-i],lista[i]
        troca_lista(lista,i+1)

# 3 - B
def fatorial(n):
    #caso base 
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)
    
troca_lista(a)
b = [fatorial(i) for i in a ]
print(b)
