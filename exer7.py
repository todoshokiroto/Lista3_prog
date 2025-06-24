def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr


n = int(input("quantos números deseja adicionar a lista"))
lista = []
for i in range(n):
    lista.append(int(input("Digite um número de telefoe \n")))
    print(bubble_sort(lista))