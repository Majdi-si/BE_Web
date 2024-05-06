import mysql.connector
from flask import session
from ..config import DB_SERVER, COLOR


###################################################################################
# connexion au serveur de la base de données

def connexion():
    try:
        cnx = mysql.connector.connect(**DB_SERVER)
        return cnx
    except mysql.connector.Error as err:
        session['errorDB'] = format(err)+" <br /> Veuillez vérifier les paramètres dans config.py"
        #affichage dans terminal
        print(COLOR['red'] + session['errorDB'] + COLOR['end'])  
        return None
    
