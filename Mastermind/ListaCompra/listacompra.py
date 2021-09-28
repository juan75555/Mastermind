SALIDA="SALIR"

def guardar(lista_compra):
    nombre = input("Que nombre desea dar a la lista: ")
    nombre+=".txt"
    with open(nombre, "w") as a:
        a.write("\n".join(lista_compra))

def input_usuario():
    elemento_lista = input("Inserta elemento en lista (los elementos son {}): ".format(lista()))
    return elemento_lista

def lista():
   lista_fija = [ "Pan" , "Pollo" , "Pipas"]
   return lista_fija 

def main():

    lista_compra=[]
    lista_fija = [ "Pan" , "Pollo" , "Pipas"]
    elemento_lista = input_usuario()
    for i in  range(len(lista_fija)):
        while elemento_lista != SALIDA and i<len(lista_fija):
            if lista_fija[i] == elemento_lista:
                lista_compra.append(elemento_lista)
                elemento_lista = input_usuario()
                i = 0
            else:
                i += 1
        else:
            if elemento_lista == SALIDA:
                i = (len(lista_fija) + 1)
            else:
                print("Has introducido una palabra no valida. Las palabras validas son {}".format(lista_fija))
                break
        
    guardar(lista_compra)

if __name__ == "__main__":
    main()
