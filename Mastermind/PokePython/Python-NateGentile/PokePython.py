import random
import os

VIDA_INICIAL_PIKACHU = 100
VIDA_INICIAL_SQUIRTLE = 100
TAMAÑO_BARRA_VIDA = 20
vida_pikachu=VIDA_INICIAL_PIKACHU
vida_squirtle=VIDA_INICIAL_SQUIRTLE

while vida_pikachu>0 and vida_squirtle>0:
    #Se devuelven los numeros

    print("Turno de Pikachu")
    ataque_pikachu = random.randint(1,2)
    if ataque_pikachu==1:
        #Bola boltio
        print("Pikachu ataca con Bola Boltio.")
        vida_squirtle-=10
    else:
        #Onda Trueno
        print("Pikachu ataca con Onda Trueno.")
        vida_squirtle-=10

    if vida_pikachu<0:
        vida_pikachu=0
    if vida_squirtle<0:
        vida_squirtle=0

    barra_vida_pikachu=int(vida_pikachu * 10/ VIDA_INICIAL_PIKACHU)
    print("Pikachu: [{}{}] ({}/{})".format("*"*barra_vida_pikachu, " "*(TAMAÑO_BARRA_VIDA - barra_vida_pikachu),vida_pikachu,VIDA_INICIAL_PIKACHU))
    barra_vida_squirtle=int(vida_squirtle * 10/ VIDA_INICIAL_SQUIRTLE)
    print("Squirtle: [{}{}] ({}/{})".format("*"*barra_vida_squirtle, " "*(TAMAÑO_BARRA_VIDA - barra_vida_squirtle),vida_squirtle,VIDA_INICIAL_SQUIRTLE))
    input("Enter para continuar...\n\n")
    os.system ("cls") 

    print("Turno Squirtle")
    ataque_squirtle = input("¿Que ataque desea realizar? -> [P]lacaje , [A]gua , [B]urbuja , [N]ingun Ataque ")
    while ataque_squirtle!='P' and ataque_squirtle!='A' and ataque_squirtle!='B' and ataque_squirtle!='N':
        ataque_squirtle = input("¿Que ataque desea realizar? -> [P]lacaje , [A]gua , [B]urbuja ")
    if ataque_squirtle=='P':
        vida_pikachu-=10
    elif ataque_squirtle=='A':
        vida_pikachu-=12
    elif ataque_squirtle=='B':
        vida_pikachu-=9
    elif ataque_squirtle=='N':
        print("Squirtle no hace nada...")
