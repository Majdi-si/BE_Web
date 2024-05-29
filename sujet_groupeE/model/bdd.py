# import sys
# sys.path.insert(0, 'c:/Users/majdi/OneDrive/Bureau/ENAC/S6/Application web/BE Web/sujet_groupeE')
import mysql.connector 
from flask import session 
# from .. import config
import sujet_groupeE.model.bddGen as bddGen
import hashlib

###################################################################################

#retourne les données de la table sugar_tracker
# def get_membresData(login=None):
#     cnx=bddGen.connexion()
#     if cnx is None:
#         return None
#     try:
#         cursor=cnx.cursor(dictionary=True)
#         if login is not None:
#             sql="SELECT * FROM utilisateur WHERE login = %s"
#             param = (login,)
#             cursor.execute(sql, param)
#             user = cursor.fetchall()  # Utilisez fetchall() pour récupérer tous les résultats
#         else:
#             sql="SELECT * FROM sugar_tracker"
#             cursor.execute(sql)
#             user = cursor.fetchall()
#         session['successDB']="OK get_membresData"
#     except mysql.connector.Error as err:
#         user=None
#         session['errorDB']="Failed get membres data:{}".format(err)
#     finally:
#         cursor.close()
#         cnx.close()
#     return user

def get_membresData():
    cnx = bddGen.connexion() 
    if cnx is None: 
        return None
    try:
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM utilisateur"
        cursor.execute(sql)
        listeMembres = cursor.fetchall()
        cursor.close()
        cnx.close()

        #session['successDB'] = "OK get_membresData"
    except mysql.connector.Error as err:
        listeMembres = None
        session['errorDB'] = "Failed get membres data : {}".format(err)
    return listeMembres

def add_userData(nom, prenom, mail, login, motPasse, statut, avatar, age, qtmax):
    mdp = hashlib.sha256(motPasse.encode()).hexdigest()
    cnx = bddGen.connexion()
    if cnx is None:
        return None

    cursor = cnx.cursor()
    cursor.execute("SELECT MAX(idUtilisateur) FROM utilisateur")
    max_id = cursor.fetchone()[0]
    new_id = max_id + 1 if max_id is not None else 1

    sql = "INSERT INTO utilisateur(idUtilisateur, login, nom, prenom, age, mail, motPasse, qtmax, statut, avatar) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param = (new_id, login, nom, prenom, age, mail, mdp, qtmax, statut, avatar)  
    msg = {
        "success": "addMembreOK",
        "error": "Failed add membres data"
    }
    lastId = bddGen.addData(cnx, sql, param, msg)
    cnx.close()
    # dernier id créé = id du nouvel utilisateur
    return lastId

import hashlib

def update_userData(champ, newValue, idUser):
    cnx = bddGen.connexion()
    if cnx is None:
        return None

    # Si le champ à mettre à jour est le mot de passe, chiffrer la nouvelle valeur
    if champ == 'motPasse':
        newValue = hashlib.sha256(newValue.encode()).hexdigest()
    sql = "UPDATE utilisateur SET " + champ + "=%s WHERE idUtilisateur=%s;"
    param = (newValue, idUser)
    msg = {
        "success": "updateMembreOK",
        "error": "Failed update membres data"
    }
    bddGen.updateData(cnx, sql, param, msg)
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

def verifAuthData2(idUtilisateur, oldPassword, newPassword, confirmPassword):
    # Hasher l'ancien mot de passe
    hashed_oldPassword = hashlib.sha256(oldPassword.encode()).hexdigest()

    cnx = bddGen.connexion()
    if cnx is None: 
        return False
    else :
        # Vérifier si l'ancien mot de passe est correct
        sql = "SELECT * FROM utilisateur WHERE idUtilisateur=%s and motPasse=%s"
        param=(idUtilisateur, hashed_oldPassword)
        msg = {
            "success":"authOK",
            "error" : "Failed get Auth data"
        }
        user = bddGen.selectOneData(cnx,sql,param,msg)
        cnx.close()

        # Si l'ancien mot de passe est incorrect, renvoyer False
        if user is None:
            return False

        # Vérifier si le nouveau mot de passe et le mot de passe confirmé sont les mêmes
        if newPassword != confirmPassword:
            print("Les mots de passe ne correspondent pas")
            return False

    # Si toutes les vérifications sont réussies, renvoyer True
    return True

def delete_userData(idUser):
    cnx = bddGen.connexion()
    if cnx is None:
        return None
    else:
        sql = "DELETE FROM utilisateur WHERE idUtilisateur=%s"
        param = (idUser,)
        msg = {
            "success": "deleteMembreOK",
            "error": "Failed delete membres data"
        }
        bddGen.deleteData(cnx, sql, param, msg)
        cnx.close()
    return 1

#enregistrement des données provenant du fichier excel
def saveDataFromFile(data):
    truncateTable("identification")
    cnx = bddGen.connexion()
    if cnx is None: return None
    # insertion des nouvelles données avec executemany
    sql ="INSERT INTO identification (nom, prenom, mail,login, motPasse, statut, avatar) VALUES (%s,%s,%s,%s,%s,%s,%s);"
    param = []
    for d in data:
        newData = (d['nom'],d['prenom'],d['mail'],d['login'],d['motPasse'],d['statut'],d['avatar'])
        param.append(newData)
    msg = {
        "success":"OK saveDataFromFile",
        "error" : "Failed saveDataFromFile data"
    } 
    lastId = bddGen.addManyData(cnx, sql, param, msg)
    cnx.close()
    return lastId

#supprime les données d'une table
def truncateTable(nomTable):
    cnx = bddGen.connexion()
    if cnx is None: return None
    sql = "TRUNCATE TABLE %s;"
    param = [nomTable]
    msg = {
        "succes":"truncateTableOK",
        "error" :"Failed truncate data"
    }
    return bddGen.deleteData(cnx, sql, param, msg)

def get_produitData_per_15(page, per_page=15):
    cnx = bddGen.connexion()
    if cnx is None: return None
    sql = "SELECT * FROM produit ORDER BY idProduit LIMIT %s OFFSET %s"
    param = (per_page, (page - 1) * per_page)
    msg = {
        "success":"ok",
        "error" : "Ce produit n'existe pas"
    }
    listeProduit = bddGen.selectData(cnx, sql, param, msg)
    cnx.close()
    return listeProduit

def add_produit(nom_produit, marque, qtsucre, idCategorie, idUtilisateur, image):
    cnx = bddGen.connexion()
    if cnx is None: return None
    cursor = cnx.cursor()
    cursor.execute("SELECT MAX(idProduit) FROM produit")
    max_id = cursor.fetchone()[0]
    new_id = max_id + 1 if max_id is not None else 1

    sql = "INSERT INTO produit(idProduit, nom, marque, qtsucre, idCategorie, idUtilisateur, image) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    param = (new_id, nom_produit, marque, qtsucre, idCategorie, idUtilisateur, image)
    msg = {
        "success": "addProduitOK",
        "error": "Failed add produit data"
    }
    lastId = bddGen.addData(cnx, sql, param, msg)
    cnx.close()
    return lastId

def get_imageData():
    cnx = bddGen.connexion()
    if cnx is None: return None
    sql = " SELECT image FROM produit"
    param = None
    msg = {
        "success":"ok",
        "error" : "Ce produit n'existe pas"
    }
    listeimage = bddGen.selectData(cnx, sql, param, msg)
    cnx.close()
    return listeimage

def get_qtsurcreData():
    cnx = bddGen.connexion()
    if cnx is None: return None
    sql = " SELECT qtsucre FROM produit"
    param = None
    msg = {
        "success":"ok",
        "error" : "Ce produit n'existe pas"
    }
    listeqtsucre = bddGen.selectData(cnx, sql, param, msg)
    cnx.close()
    return listeqtsucre

def get_produitData():
    cnx = bddGen.connexion()
    if cnx is None: return None
    sql = "SELECT * FROM produit"
    param = None
    msg = {
        "success":"ok",
        "error" : "Ce produit n'existe pas"
    }
    listeProduit = bddGen.selectData(cnx, sql, param, msg)
    cnx.close()
    return listeProduit

def get_total_produit() :   # Cette fonction doit retourner le nombre total de produits
    cnx = bddGen.connexion()
    if cnx is None: return None
    sql = "SELECT COUNT(*) FROM produit"
    param = None
    msg = {
        "success":"ok",
        "error" : "Ce produit n'existe pas"
    }
    dico_total = bddGen.selectData(cnx, sql, param, msg)
    total = dico_total[0]['COUNT(*)']
    cnx.close()
    return total

def get_total_produit_per_categorie():
    cnx = bddGen.connexion()
    if cnx is None: 
        return None
    
    sql = "SELECT idCategorie, COUNT(*) as total FROM produit GROUP BY idCategorie"
    param = None
    msg = {
        "success":"ok",
        "error" : "Ce produit n'existe pas"
    }
    result = bddGen.selectData(cnx, sql, param, msg)
    cnx.close()
    
    # Convert the result into a dictionary
    total_per_categorie = {item['idCategorie']: item['total'] for item in result}
    
    return total_per_categorie

def get_produitData_per_categorie(idCategorie):
    cnx = bddGen.connexion()
    if cnx is None: return None
    sql = "SELECT * FROM produit WHERE idCategorie = %s"
    param = (idCategorie,)
    msg = {
        "success":"ok",
        "error" : "Ce produit n'existe pas"
    }
    listeProduit = bddGen.selectData(cnx, sql, param, msg)
    cnx.close()
    return listeProduit

def get_produit_by_id(idProduit):
    cnx = bddGen.connexion()
    if cnx is None: return None
    sql = "SELECT * FROM produit WHERE idProduit = %s"
    param = (idProduit,)
    msg = {
        "success":"ok",
        "error" : "Ce produit n'existe pas"
    }
    produit = bddGen.selectOneData(cnx, sql, param, msg)
    cnx.close()
    return produit

def get_latest_products():
    cnx = bddGen.connexion()
    if cnx is None:
        return None
    sql = "SELECT * FROM produit ORDER BY idProduit DESC LIMIT 8"
    param = None
    msg = {
        "success": "ok",
        "error": "Failed to get latest products"
    }
    latest_products = bddGen.selectData(cnx, sql, param, msg)
    cnx.close() 
    return latest_products

def update_produitData(champ, newValue, idProduit):
    cnx = bddGen.connexion()
    if cnx is None:
        return None
    sql = "UPDATE produit SET " + champ + "=%s WHERE idProduit=%s;"
    param = (newValue, idProduit)
    msg = {
        "success": "updateProduitOK",
        "error": "Failed update produit data"
    }
    bddGen.updateData(cnx, sql, param, msg)
    cnx.close()
    return 1

def delete_produitData(idProduit):
    cnx = bddGen.connexion()
    if cnx is None:
        return None
    else:
        sql = "DELETE FROM produit WHERE idProduit=%s"
        param = (idProduit,)
        msg = {
            "success": "deleteProduitOK",
            "error": "Failed delete produit data"
        }
        bddGen.deleteData(cnx, sql, param, msg)
        cnx.close()
    return 1


def add_new_categorie(nomCategorie):
    cnx = bddGen.connexion()
    if cnx is None:
        return None
    cursor = cnx.cursor()
    cursor.execute("SELECT MAX(idCategorie) FROM categorie")
    max_id = cursor.fetchone()[0]
    new_id = max_id + 1 if max_id is not None else 1

    sql = "INSERT INTO categorie(idCategorie, nom) VALUES(%s,%s)"
    param = (new_id, nomCategorie)
    msg = {
        "success": "addCategorieOK",
        "error": "Failed add categorie data"
    }
    lastId = bddGen.addData(cnx, sql, param, msg)
    cnx.close()
    return lastId

def get_categorieData():
    cnx = bddGen.connexion()
    if cnx is None:
        return None
    sql = "SELECT * FROM categorie"
    param = None
    msg = {
        "success": "ok",
        "error": "Failed get categorie data"
    }
    listeCategorie = bddGen.selectData(cnx, sql, param, msg)
    cnx.close()
    return listeCategorie

def delete_categorieData(category_id):
    cnx = bddGen.connexion()
    if cnx is None:
        return None
    else:
        sql = "DELETE FROM categorie WHERE idCategorie=%s"
        param = (category_id,)
        msg = {
            "success": "deleteCategorieOK",
            "error": "Failed delete categorie data"
        }
        bddGen.deleteData(cnx, sql, param, msg)
        cnx.close()
    return 1