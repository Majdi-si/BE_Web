# import sys
# sys.path.insert(0, 'c:/Users/majdi/OneDrive/Bureau/ENAC/S6/Application web/BE Web/sujet_groupeE')
import mysql.connector 
from flask import session 
# from .. import config
import sujet_groupeE.model.bddGen as bddGen

###################################################################################

#retourne les données de la table sugar_tracker
def get_membresData():
    cnx=bddGen.connexion()
    if cnx is None:
        return None
    try:
        cursor=cnx.cursor(dictionary=True)
        sql="SELECT * FROM sugar_tracker"
        cursor.execute(sql)
        listeMembres=cursor.fetchall()
        close_bd(cursor,cnx)
        session['successDB']="OK get_membresData"
    except mysql.connector.Error as err:
        listeMembres=None
        session['errorDB']="Failed get membres data:{}".format(err)
    return(listeMembres)

def add_userData(nom,prenom,mail,login,motPasse,statut, taux):
    cnx=bddGen.connexion()
    if cnx is None:
        return None
    sql="INSERT INTO utilisateur(nom, prenom, mail, login, motPasse, statut, taux) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    param=(nom,prenom,mail,login,motPasse,statut,taux)
    msg={
        "success":"addMembreOK",
        "error":"Failed add membres data"
    }
    lastId=bddGen.addData(cnx,sql,param,msg)
    cnx.close()
    #dernier id créé=id du nouvel utilisateur
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
    cnx = bddGen.connexion()
    if cnx is None: return None
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