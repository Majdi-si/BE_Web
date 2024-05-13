from flask import Flask, render_template, request, session, redirect, flash, url_for
import hashlib
from sujet_groupeE.controller import function as f
import sujet_groupeE.model.bdd as bdd
from werkzeug.utils import secure_filename
import pandas, os

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

@app.route("/webmaster")
def contact():
    return render_template("webmaster.html")

@app.route("/recettes")
def shop_detail():
    return render_template("recettes.html")

@app.route("/produits")
def shop():
    return render_template("produits.html")

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

    ## Gestion du fichier avatar
    # avatar_connexion = None
    # avatar_extension = None
    # if 'avatar' in request.files:
    #     avatar_file = request.files['avatar']
    #     if avatar_file.filename != '':
    #         avatar_extension = os.path.splitext(avatar_file.filename)[1][1:]  # get file extension
    #         avatar_connexion = secure_filename(avatar_file.filename)
    #         avatar_file.save(os.path.join(app.config['UPLOAD_FOLDER'], avatar_connexion))

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
    lastId = bdd.add_userData(nom_connexion, prenom_connexion, mail_connexion, login_connexion, mdp_connexion, statut_connexion, admin, avatar_connexion) #ajouter avatar_extension
    if lastId == 0:  # Si l'insertion a échoué
        lastId = bdd.get_membresData()  # Récupère l'ID de l'utilisateur à partir du login
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
    session['mdp'] = mdp_connexion
    return redirect(url_for('compte'))  # Redirige vers la page de compte
    
#mdp = hashlib.sha256(mdp.encode())
#mdpC = mdp.hexdigest() #mdpC=mot de passe chiffré

@app.route("/login")
def login():
    #params = f.messageInfo() # récupération des messages d'info
    return render_template("login.html")


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
        session["mdp"] = mdp
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
    membres = bdd.get_membresData()
    return render_template("admin.html", membres=membres)

@app.route("/delete_member", methods=['POST'])
def delete_membre():
    id_membre = request.form.get('id_membre')
    print("member id to delete: ", id_membre)
    bdd.delete_userData(id_membre)
    if "errorDB" not in session:
        session["infoVert"] = "Membre supprimé"
    else:
        session["infoRouge"] = "Problème suppression utilisateur"
    return redirect(url_for('admin'))


@app.route('/update-info', methods=['POST'])
def update_info():
    # Récupérer les nouvelles informations du formulaire
    prenom = request.form.get('prenom')
    nom = request.form.get('nom')
    login = request.form.get('login')
    mail = request.form.get('mail')
    statut = request.form.get('statut')
    newPassword = request.form.get('newPassword')
    confirmPassword = request.form.get('confirmPassword')
    oldPassword = request.form.get('oldPassword')

    # Vérifier si l'utilisateur a entré un nouveau mot de passe
    if newPassword:
        try:
            # Vérifier si l'ancien mot de passe est correct et si le nouveau mot de passe et le mot de passe confirmé sont les mêmes
            if bdd.verifAuthData2(session['idUtilisateur'], oldPassword, newPassword, confirmPassword):
                # Mettre à jour le mot de passe de l'utilisateur dans la base de données
                bdd.update_userData('motPasse', newPassword, session['idUtilisateur'])
                session['mdp'] = newPassword
                flash('Votre mot de passe a été mis à jour avec succès.', 'success')
            else:
                flash('L\'ancien mot de passe n\'est pas correct ou le nouveau mot de passe et le mot de passe confirmé ne correspondent pas.', 'error')
        except Exception as e:
            flash('Une erreur est survenue lors de la vérification du mot de passe.', 'error')

    try:
        # Mettre à jour les autres informations de l'utilisateur dans la base de données
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
    except Exception as e:
        flash('Une erreur est survenue lors de la mise à jour de vos informations.', 'error')

    # Rediriger l'utilisateur vers la page du compte
    return redirect(url_for('compte'))

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))+'/file/'

@app.route("/fichierUpload", methods=['POST'])
def fichiersUpload():
    if "testFile" in request.files:
        file=request.files['testFile']

        #enregistrement du fichier dans le répertoire files
        filename = secure_filename(file.filename)
        print(os.path.join(UPLOAD_FOLDER, filename))
        file.save(os.path.join(UPLOAD_FOLDER, filename))

        #Conversion du fichier xls en dictionnaire
        xls = pandas.read_excel(UPLOAD_FOLDER+file.name)
        data = xls.to_dict('records')
        print([file.filename, data])

        #Enregistrement des données en BDD
        bdd.saveDataFromFile(data)
        if "errorDB" not in session:
            session["infoVert"] = "Données sauvegardées en BDD"
            return redirect("/sgbd")
        else:
            session["infoRouge"]="Problème enregistrement des données"
            return redirect("/fichiers")