SALIDA="SALIR"

def guardar(lista_compra):
    nombre = input("Que nombre desea dar a la lista: ")
    nombre+=".txt"
    a = open(nombre, "w")
    a.write("\n".join(lista_compra))
    a.close()

def input_usuario():
    elemento_lista = input("Inserta elemento en lista: ")
    return elemento_lista
def main():

    lista_compra=[]
    lista_fija = [ "Pan" , "Pollo" , "Pipas"]
    elemento_lista = input_usuario()
    for i in  range(len(lista_fija)):
        if elemento_lista != SALIDA:
            if lista_fija[i] == elemento_lista:
                lista_compra.append(elemento_lista)
                elemento_lista = input_usuario()
                i = 0
            else:
                i += 1
        else:
            exit()
        
    guardar(lista_compra)

if __name__ == "__main__":
    main()