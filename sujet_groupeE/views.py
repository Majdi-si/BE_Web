from flask import Flask, render_template, request, session, redirect
import hashlib


import sujet_groupeE.model.bdd as bdd

app = Flask(__name__)
app.template_folder = "template"
app.static_folder = "static"
app.config.from_object('sujet_groupeE.config')
@app.route("/")
def index():
    return render_template("index.html")

#page home
@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/404")
def error():
    return render_template("404.html")

@app.route("/chackout")
def chackout():
    return render_template("chackout.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/shop-detail")
def shop_detail():
    return render_template("shop-detail.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/testimonial")
def testimonial():
    return render_template("testimonial.html")
    
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/ajout", methods=["POST"])
def ajout():
    nom_connexion = request.form['nom']
    prenom_connexion = request.form['prenom']
    mail_connexion = request.form['mail']
    login_connexion = request.form['login']
    mdp_connexion = request.form['mdp']
    statut_connexion = request.form['monSelect']
    # avatar_connexion = request.files['avatar']
    lastId = bdd.add_userData(nom_connexion, login_connexion, prenom_connexion, mail_connexion, mdp_connexion, statut_connexion)
    # print(lastId) # dernier id créé par le serveur de BDD
    # if "errorDB" not in session: 
    #     session["infoVert"]="Nouveau membre inséré"
    # else:
    #     session["infoRouge"]="Problème ajout utilisateur"
    # return redirect("/sgbd")
    return "Les données reçues sont : " + nom_connexion + " " + prenom_connexion + " " + mail_connexion + " " + login_connexion + " " + mdp_connexion + " " + statut_connexion
    
#mdp = hashlib.sha256(mdp.encode())
#mdpC = mdp.hexdigest() #mdpC=mot de passe chiffré


#reception donnees du compte
@app.route("/compte")
def compte():
    return render_template("compte.html")

@app.route("/ajouter", methods=["POST"])
def ajouter():
    return request.form['prenom']
    #return "Formulaire POST reçu"

#mdp = hashlib.sha256(mdp.encode())
#mdpC = mdp.hexdigest() #mdpC=mot de passe chiffré

# ajout d'un membre
@app.route("/addMembre", methods=['POST'])
def addMembre():
 # réception des données du formulaire
    nom = request.form['nom']
    prenom = request.form['prenom']
    mail = request.form['mail']
    login = request.form['login']
    motPasse = request.form['mdp']
    statut = request.form['statut']
    avatar = request.form['avatar']
    lastId = bdd.add_userData(nom, prenom, mail, login, motPasse, statut, avatar)
    print(lastId) # dernier id créé par le serveur de BDD
    if "errorDB" not in session: 
        session["infoVert"]="Nouveau membre inséré"
    else:
        session["infoRouge"]="Problème ajout utilisateur"
    return redirect("/sgbd")

@app.route("/login", methods=["POST"])
def connect():
    login = request.form['login']
    mdp = request.form['mdp']
    user = bdd.verifAuthData(login, mdp)
    print(user)
    try:
        # Authentification réussie
        session["idUser"] = user["idUser"]
        session["nom"] = user["nom"]
        session["prenom"] = user["prenom"]
        session["mail"] = user["mail"]
        session["statut"] = user["statut"]
        session["avatar"] = user["avatar"]
        session["infoVert"]="Authentification réussie"
        return redirect("/")
    except TypeError as err:
        # Authentification refusée
        session["infoRouge"]="Authentification refusée"
    return redirect("/login")