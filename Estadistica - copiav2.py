import math
import numpy as np
datos=[]
np.set_printoptions(suppress=True)
#prueba=[5,4,6,14,4,3,4,11,6,1,3,5,6,1,5,4,7,3,5,8,3,6,6,2,6,5,6,12,15,9,1,4,7,4,3,6,5,4,1,2,4,2,1,4,5,8,9,7,10,12]
#prueba2 = [5, 4, 6, 14, 4, 3, 4, 11, 6, 1, 3, 5, 6, 1, 5, 4, 7, 3, 5, 8, 3, 6, 6, 2,
#          6, 5, 6, 12, 15, 9, 1, 4, 7, 4, 3, 6, 5, 4, 1, 2, 4, 2, 1, 4, 5, 8, 9, 7, 10, 12]

prueba2 = [77, 54, 58, 63, 45, 18, 56, 58, 62, 66, 63, 36, 53, 62, 80, 80, 26, 51, 65,
           71, 38, 50, 62, 61, 63, 54, 34, 43, 52, 58, 50, 44, 52, 60, 61, 59, 41, 53, 60, 71]

lim_inferior=[]
lim_superior=[]
marca_de_clase=[]
f_absoluta=[]
f_acumulada=[]
f_acumulada_des=[]
f_relativa=[]
f_relativa_acumulada=[]
puntoMedio=[]
frecPorPuntoM=[]
fM=0
media=0
puntoM=0
n=0
dato=0
frecRelativa=0
frecRelativaAcum=0
vm_max=0
vm_min=0
rango=0
numero_intervalos_k=0
tamano_clase=0
suma_Absoluta=0

n=(len(prueba2))
numero_intervalos_k=7
"""n=int(input("Ingrese el numero de datos=>"))
numero_intervalos_k=int(input("Ingrese el numero de clases que desea obtener=> "))
print("\n")

for i in range(0,n):
    dato=float(input("Ingrese el elemento "+str(i)+" => "))
    datos.append(dato)

vm_max=max(datos)
vm_min=min(datos)
rango=(vm_max-vm_min)
#numero_intervalos_k=round((1+3.322*math.log10(n)))#regla de sturgels
"""
vm_max=max(prueba2)
vm_min=min(prueba2)
rango=(vm_max-vm_min)
tamano_clase=round((rango/numero_intervalos_k))

suma1=vm_min
lim_inferior.append(suma1)


for k in range(0,numero_intervalos_k-1):
    suma1=suma1+(tamano_clase)
    lim_inferior.append(suma1)

suma2=(vm_min+(tamano_clase-1))
lim_superior.append(suma2)
for x in range(0,numero_intervalos_k-1):
    suma2=suma2+(tamano_clase)
    lim_superior.append(suma2)
                
prueba2.sort()

#Frecuencia absoluta
c=0
for i in range(0,numero_intervalos_k):
    c=0
    for x in range(0,n):
        if(prueba2[x]>=lim_inferior[i] and prueba2[x]<=lim_superior[i]):
            c+=1
    f_absoluta.append(c)
#For que suma todos los datos de la absoluta
for i in range(0, numero_intervalos_k):
    suma_Absoluta+=f_absoluta[i]
#Frecuencia acumulada ascendente
c=0
for i in range(0,numero_intervalos_k):
    for x in range(0,n):
        if(prueba2[x]>=lim_inferior[i] and prueba2[x]<=lim_superior[i]):
            c+=1
    f_acumulada.append(c)
#Frecuencia acumulada Descedente
f_acumulada_des.append(suma_Absoluta)
t=suma_Absoluta
for i in range(1,numero_intervalos_k):
    t=(t-f_absoluta[i-1])
    f_acumulada_des.append(t)
#Frecuencia Relativa
for i in range(0,numero_intervalos_k):
    frecRelativa=(f_absoluta[i]/n)
    f_relativa.append(frecRelativa)
#Frecuencia Relativa acumulada
for i in range(0,numero_intervalos_k):
    frecRelativaAcum+=f_relativa[i]
    f_relativa_acumulada.append(frecRelativaAcum)
#Punto Medio de cada clase
for i in range(numero_intervalos_k):
    puntoM=((lim_superior[i]+lim_inferior[i])/2)
    puntoMedio.append(puntoM)
#Frecuencia por Punto Medio
sma=0
for i in range(0,numero_intervalos_k):
    fM=(f_absoluta[i]*puntoMedio[i])
    frecPorPuntoM.append(fM)
    sma+=frecPorPuntoM[i]
media=(sma/n)

resultado=np.matrix([lim_inferior, lim_superior, f_absoluta, f_acumulada,f_acumulada_des, f_relativa, f_relativa_acumulada])

#resultado.T

#print(datos)
print(vm_max)
print(vm_min)
print(numero_intervalos_k)
print(tamano_clase)
print(len(prueba2))
print("lim_inferior")
print(lim_inferior)
print("lim_superior")
print(lim_superior)
print("Frecuencia absoluta")
print(f_absoluta)
print("Frecuencia acumulada Ascendente")
print(f_acumulada)
print("Frecuencia Relativa")
print(f_relativa)
print("Frecuencia Relativa Acumulada")
print(f_relativa_acumulada)
print("Punto Medio")
print(puntoMedio)
print("Frecuencia por Punto Medio")
print(frecPorPuntoM)
print("Media")
print(media)
print("Datos_Matriz")
print(resultado.T)