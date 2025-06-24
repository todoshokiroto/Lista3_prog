import random
lista = [random.randint(1,100) for i in range(500)]
for i in range(500):
    if lista[i] >=10:
        print(f'o cliente {i} tem direito a {lista[i]//10}')