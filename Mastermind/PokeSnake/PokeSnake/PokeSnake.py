import readchar 
import os
import random
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

#Map and Character initial values
POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
NUM_OF_MAP_OBJECTS = 5

my_position = [random.randint(0, MAP_WIDTH),random.randint(0, MAP_HEIGHT)]
end_game = False
map_objects = []
while len(map_objects) < NUM_OF_MAP_OBJECTS:
    new_position = [random.randint(0, MAP_WIDTH-1),random.randint(0, MAP_HEIGHT-1)]
    if new_position not in map_objects and new_position != my_position:
        map_objects.append(new_position)
my_position[POS_X]
my_position[POS_Y]
my_name=input("Inserta tu nombre de usuario: ")

#Pokemon Initial Values
VIDA_INICIAL_PIKACHU = 100
VIDA_INICIAL_SQUIRTLE = 100
TAMAÑO_BARRA_VIDA = 10
vida_squirtle=VIDA_INICIAL_SQUIRTLE
vida_pikachu=VIDA_INICIAL_PIKACHU

#Main Loop
while not end_game:
    #Draw map
    print("+" + "-" * (MAP_WIDTH*3) + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            
            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw=Back.BLUE + Fore.BLUE + "*"
                    object_in_cell = map_object

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw=Back.WHITE + "@"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    vida_pikachu=VIDA_INICIAL_PIKACHU
                    vida_squirtle=VIDA_INICIAL_SQUIRTLE
                    while vida_pikachu>0 and vida_squirtle>0:
                        #Se devuelven los numeros
                        print("Turno de Squirtle")
                        ataque_squirtle = random.randint(1,2)
                        if ataque_squirtle==1:
                            #Placaje
                            print("Squirtle ataca con Placaje.")
                            vida_pikachu-=10
                        else:
                            #Agua
                            print("Squirtle ataca con Agua.")
                            vida_pikachu-=10

                        if vida_pikachu<0:
                            vida_pikachu=0
                        if vida_squirtle<0:
                            vida_squirtle=0

                        barra_vida_pikachu=int(vida_pikachu * 10/ VIDA_INICIAL_PIKACHU)
                        print("Pikachu: [{}{}] ({}/{})".format("*"*barra_vida_pikachu, " "*(TAMAÑO_BARRA_VIDA - barra_vida_pikachu),vida_pikachu,VIDA_INICIAL_PIKACHU))
                        barra_vida_squirtle=int(vida_squirtle * 10/ VIDA_INICIAL_SQUIRTLE)
                        print("Squirtle: [{}{}] ({}/{})".format("*"*barra_vida_squirtle, " "*(TAMAÑO_BARRA_VIDA - barra_vida_squirtle),vida_squirtle,VIDA_INICIAL_SQUIRTLE))
                        input("Enter para continuar...\n\n")
                        os.system ("clear") 

                        print("Turno Pikachu")
                        ataque_pikachu = input("¿Que ataque desea realizar? -> [L]atigo , [I]mpactrueno , [B]ola Voltio , [N]ingun Ataque ")
                        while ataque_pikachu!='L' and ataque_pikachu!='I' and ataque_pikachu != 'B' and ataque_pikachu != 'N' and ataque_pikachu != 'º' :
                            ataque_pikachu = input("¿Que ataque desea realizar? -> [L]atigo , [I]mpactrueno , [B]ola Voltio , [N]ingun Ataque ")
                        if ataque_pikachu == 'L':
                            #Placaje
                            vida_squirtle -= 10
                        elif ataque_pikachu == 'I':
                            #Agua
                            vida_squirtle -= 12
                        elif ataque_pikachu =='B':
                            #Burbuja
                            vida_squirtle -= 9
                        elif ataque_pikachu =='N':
                            #Nada
                            print("Pikachu no hace nada...")
                        elif ataque_pikachu == 'º':
                            #Secret Cheat
                            vida_squirtle = 0
                        if vida_pikachu<=0:
                            #End_game
                            print( Style.BRIGHT + Fore.RED + my_name + " Game Over.")
                            end_game = True
                    if len(map_objects) == 0:
                        print( Style.BRIGHT + Fore.GREEN + my_name + " you Win :)")
                        end_game = True
                        
            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * (MAP_WIDTH*3) + "+")

    #Ask user where he wants to move.
    direction= readchar.readchar()

    if direction == 'w':
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == 's':
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == 'a':
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == 'd':
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == 'q':
        end_game = True
                
    os.system("clear")
