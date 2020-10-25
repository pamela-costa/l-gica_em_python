# Algoritmo de ordenacao

listaD = [10, 91, 62, 33, 4, 62, 1000, 88, 2, 0]

i = 0
while i < len(listaD):
    j = i + 1
    while j < len(listaD):
        if listaD[i] > listaD[j]:
            temp = listaD[i]
            listaD[i] = listaD[j]
            listaD[j] = temp
        j = j + 1
    i = i+1

print(listaD)