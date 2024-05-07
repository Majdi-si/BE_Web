# import sys
# sys.path.insert(0, 'c:/Users/majdi/OneDrive/Bureau/ENAC/S6/Application web/BE Web/sujet_groupeE')
import mysql.connector 
from flask import session 
# from .. import config
import sujet_groupeE.model.bddGen as bddGen
import hashlib

###################################################################################

#retourne les données de la table sugar_tracker
def get_membresData(login=None):
    cnx=bddGen.connexion()
    if cnx is None:
        return None
    try:
        cursor=cnx.cursor(dictionary=True)
        if login is not None:
            sql="SELECT * FROM utilisateur WHERE login = %s"
            param = (login,)
            cursor.execute(sql, param)
            user = cursor.fetchall()  # Utilisez fetchall() pour récupérer tous les résultats
        else:
            sql="SELECT * FROM sugar_tracker"
            cursor.execute(sql)
            user = cursor.fetchall()
        session['successDB']="OK get_membresData"
    except mysql.connector.Error as err:
        user=None
        session['errorDB']="Failed get membres data:{}".format(err)
    finally:
        cursor.close()
        cnx.close()
    return user
def add_userData(nom, prenom, mail, login, motPasse, statut, admin):
    mdp = hashlib.sha256(motPasse.encode()).hexdigest()
    cnx = bddGen.connexion()
    if cnx is None:
        return None

    cursor = cnx.cursor()
    cursor.execute("SELECT MAX(idUtilisateur) FROM utilisateur")
    max_id = cursor.fetchone()[0]
    new_id = max_id + 1 if max_id is not None else 1

    sql = "INSERT INTO utilisateur(idUtilisateur, login, nom, prenom, mail, motPasse, statut, admin) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    param = (new_id, login, nom, prenom, mail, mdp, statut, admin)  
    msg = {
        "success": "addMembreOK",
        "error": "Failed add membres data"
    }
    lastId = bddGen.addData(cnx, sql, param, msg)
    cnx.close()
    # dernier id créé = id du nouvel utilisateur
    return lastId

def update_userData(champ,newValue,idUser):
    cnx=bddGen.connexion()
    if cnx is None :
        return None
    sql="UPDATE identification SET "+champ+"=%s WHERE idUser=%s;"
    param=(newValue,idUser)
    msg={"success":"updateMembreOK",
         "error":"Failed update membres data"}
    bddGen.updateData(cnx,sql,param,msg)
    cnx.close()
    return 1

def verifAuthData(login, mdp):
    mdp = hashlib.sha256(mdp.encode()).hexdigest()
    cnx = bddGen.connexion()
    if cnx is None: 
        return None
    else :
        sql = "SELECT * FROM utilisateur WHERE login=%s and motPasse=%s"
        param=(login, mdp)
        msg = {
            "success":"authOK",
            "error" : "Failed get Auth data"
        }
        # requête par fetchone
        user = bddGen.selectOneData(cnx,sql,param,msg)
        cnx.close()
    return user