#Listas:
lista = ["Santiago","Alejandro",10,True]
print(lista)
lista.append("Piracon")
print(lista)
lista.insert(0,2)
print(lista)

lista.append([2,4])
print(lista)
lista.extend([2,4])
print(lista)
lista.remove(10)
print(lista)
lista.index("Alejandro")
print(lista)
print(lista.count("Alejandro"))
lista.clear()
print(lista)
#lista.copy
#lista.reverse

print("=PILA=")
Pila = [1,2,3,4]
Pila.append(5)
print(Pila)
print(Pila.pop())

print("=TUPLA=")
Tupla = ("hola",2,True)
print(Tupla)
#Tupla.append(5)
#print(Tupla)

print("==Conjuntos==")
A = {"A","B","C","D"}
B = {"A","B","F","G"}
print(A)
print(B)
print(A-B)
print(A|B)
print(A&B)

print("==Diccionarios==")
diccionario = {"uno":1,"true":True,"nombre":"Alejandro"}
print(diccionario)
print(diccionario["nombre"])
diccionario["nombre"] = "Santiago"
print(diccionario)
print(sorted(diccionario.keys()))

