import numpy as np
import matplotlib.pyplot as plt
import time
def ordenar_ingenuo(arreglo):
    for i in range(0,arreglo.shape[0]):
        for j in range(i+1,arreglo.shape[0]):
            if arreglo[j]<arreglo[i]:
                arreglo[i],arreglo[j] = arreglo[j],arreglo[i]

arreglo1 = np.array([4,2,1,0,3,5,5,5,1,1,6])
ordenar_ingenuo(arreglo1)
print(arreglo1)

def insertion_sort(arreglo):
    for j in range(2, arreglo.shape[0]+1):
        key = arreglo[j-1]
        i = j-1
        while i>0 and arreglo[i-1]>key:
            arreglo[i] = arreglo[i-1]
            i = i-1
        arreglo[i] = key 

arreglo1 = np.array([4,2,1,0,3,5,5,5,1,1,6])
insertion_sort(arreglo1)
print(arreglo1)



tiemposOI = []
tiemposIS = []
tamanios = [100,1000,5000,7500]
for n in tamanios:
    arregloX = np.random.randint(0,100000,(n))
    ini = time.time()
    ordenar_ingenuo(arregloX)
    fin = time.time()
    tiemposOI.append(fin-ini)

    arregloX = np.random.randint(0,100000,(n))
    ini = time.time()
    insertion_sort(arregloX)
    fin = time.time()
    tiemposIS.append(fin-ini)

print(tiemposOI)
print(tiemposIS)

fig = plt.figure(dpi=300)
plt.plot(tamanios,tiemposOI,"r-", label="Algoritmo ingenuo")
plt.plot(tamanios,tiemposIS,"b-",label="Insertion Sort")
plt.xlabel("Tamaño")
plt.ylabel("Segundos")
plt.legend()
plt.tight_layout()
plt.show()