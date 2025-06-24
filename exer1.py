lista = []
n = int(input("deseja digitar quantos números?"))
for i in range(n):
    lista.append(int(input("Digite o {} número".format(i))))

ind = int(input("digite o valor que deseja saber o index"))
for i in range(len((lista))):
    if lista[i] == ind:
        print(i)
