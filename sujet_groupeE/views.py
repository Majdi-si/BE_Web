from flask import Flask, render_template, request, session, redirect, flash, url_for
import hashlib
from sujet_groupeE.controller import function as f


import sujet_groupeE.model.bdd as bdd

app = Flask(__name__)
app.template_folder = "template"
app.static_folder = "static"
app.config.from_object('sujet_groupeE.config')
@app.route("/")
def index():
    params = f.messageInfo() # récupération des messages d'info
    return render_template("index.html", **params)

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
    
@app.route("/new_account")
def new_account():
    return render_template("new_account.html")

@app.route("/ajout", methods=["POST"])
def ajout():
    admin = 0
    nom_connexion = request.form['nom']
    prenom_connexion = request.form['prenom']
    mail_connexion = request.form['mail']
    login_connexion = request.form['login']
    mdp_connexion = request.form['mdp']
    statut_connexion = request.form['monSelect']
    if statut_connexion == "admin":
        admin = 1
    else:
        admin = 0
    avatar_connexion = None
    if 'avatar' in request.form:
        avatar_connexion = request.form['avatar']
    else:
        # Gérer le cas où 'avatar' n'est pas présent
        print("Le fichier 'avatar' n'est pas présent dans la requête.")
    lastId = bdd.add_userData(nom_connexion, prenom_connexion, mail_connexion, login_connexion, mdp_connexion, statut_connexion, admin, avatar_connexion)
    if lastId == 0:  # Si l'insertion a échoué
        lastId = bdd.get_membresData(login_connexion)  # Récupère l'ID de l'utilisateur à partir du login
    # print(lastId) # dernier id créé par le serveur de BDD
    # if "errorDB" not in session: 
    #     session["infoVert"]="Nouveau membre inséré"
    # else:
    #     session["infoRouge"]="Problème ajout utilisateur"

    # Stocke les informations de l'utilisateur dans la session
    session['idUtilisateur'] = lastId
    session['login'] = login_connexion
    session['admin'] = admin
    session['nom'] = nom_connexion
    session['prenom'] = prenom_connexion
    session['mail'] = mail_connexion
    session['avatar'] = avatar_connexion
    session['statut'] = statut_connexion
    return redirect(url_for('compte'))  # Redirige vers la page de compte
    
#mdp = hashlib.sha256(mdp.encode())
#mdpC = mdp.hexdigest() #mdpC=mot de passe chiffré

@app.route("/login")
def login():
    params = f.messageInfo() # récupération des messages d'info
    return render_template("login.html", **params)


@app.route("/login", methods=["POST"])
def connect():
    login = request.form['login']
    mdp = request.form['mdp']
    user = bdd.verifAuthData(login, mdp)
    try:
        # Authentification réussie
        session["idUtilisateur"] = user["idUtilisateur"]
        session["nom"] = user["nom"]
        session["prenom"] = user["prenom"]
        session["mail"] = user["mail"]
        session["statut"] = user["statut"]
        session["admin"] = user["admin"]
        session["avatar"] = user["avatar"]
        session["login"] = user["login"]
        # session["avatar"] = user["avatar"]
        flash("Authentification réussie", "success")
        session["infoVert"]="Authentification réussie"
        return redirect("/")
    except TypeError as err:
        # Authentification refusée
        session["infoRouge"]="Authentification refusée : Login ou Mot de passe incorrect"
        flash("Authentification refusée : Login ou Mot de passe incorrect", "error")
        return redirect("/login")

@app.route('/logout')
def logout():
    # Supprime 'login' de la session
    session.clear() 
    # Redirige l'utilisateur vers la page de connexion
    return redirect(url_for('login'))

@app.route("/compte")
def compte():
    return render_template("compte.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route('/update-info', methods=['POST'])
def update_info():
    # Récupérer les nouvelles informations du formulaire
    prenom = request.form.get('prenom')
    print(prenom)
    nom = request.form.get('nom')
    login = request.form.get('login')
    mail = request.form.get('mail')
    statut = request.form.get('statut')

    # Valider les nouvelles informations ici...

    # Mettre à jour les informations de l'utilisateur dans la base de données
    bdd.update_userData('prenom', prenom, session['idUtilisateur'])
    bdd.update_userData('nom', nom, session['idUtilisateur'])
    bdd.update_userData('login', login, session['idUtilisateur'])
    bdd.update_userData('mail', mail, session['idUtilisateur'])
    bdd.update_userData('statut', statut, session['idUtilisateur'])

    # Mettre à jour les informations de la session
    session['prenom'] = prenom
    session['nom'] = nom
    session['login'] = login
    session['mail'] = mail
    session['statut'] = statut

    # Rediriger l'utilisateur vers la page du compte ou afficher un message de succès
    return redirect(url_for('compte'))