import mysql.connector
from flask import session
from  config import DB_SERVER, COLOR

#connexion au serveur de la base de données
def connexion():
    try:
        cnx=mysql.connector.connect(**DB_SERVER)
        #affichage dans le terminal
        print(color['green']+'connexion BDD OK'+COLOR['end'])
        return cnx
    except mysql.connector.Error as err : #le problème
        session['errorDB']=format(err)

        #affichage dans le terminal
        print(COLOR['red']+session['errorDB']+color['end'])
        return None

#retourne les données de la table sugar_tracker
def get_membresData():
    cnx=connexion()
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

def add_userData(nom,prenom,mail,login,motPasse,statut,avatar):
    cnx=bdd.connexion()
    if cnx is None:
        return None
    sql="INSERT INTO sugar_tracker(nom,prenom,mail,login,motPasse,statut,avatar)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    param=(nom,prenom,mail,login,motPasse,statut,avatar)
    msg={
        "success":"addMembreOK",
        "error":"Failed add membres data"
    }
    lastId=bdd.addData(cnx,sql,param,msg)
    cnx.close()
    #dernier id créé=id du nouvel utilisateur
    return lastId

def update_userData(champ,newValue,idUser):
    cnx=bdd.connexion()
    if cnx is None :
        return None
    sql="UPDATE identification SET "+champ+"=%s WHERE idUser=%s;"
    param=(newValue,idUser)
    msg={"success":"updateMembreOK",
         "error":"Failed update membres data"}
    bdd.updateData(cnx,sql,param,msg)
    cnx.close()
    return 1
