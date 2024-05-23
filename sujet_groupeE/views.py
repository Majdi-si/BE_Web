from flask import Flask, render_template, request, session, redirect, flash, url_for
import hashlib
from sujet_groupeE.controller import function as f
import sujet_groupeE.model.bdd as bdd
from werkzeug.utils import secure_filename
import pandas, os
import json
from math import ceil
from werkzeug.utils import secure_filename
from flask import jsonify

app = Flask(__name__)
app.template_folder = "template"
app.static_folder = "static"
app.config.from_object('sujet_groupeE.config')
@app.route("/")
def index():
    categories = {
        1: "Goûter/Dessert",
        2: "Produits Laitiers",
        3: "Sauce",
        4: "Fruits/Légumes",
        5: "Viande/Poisson",
        6: "Boisson",
        7: "Féculents/Céréales"
    }
    last_products = bdd.get_latest_products()
    print("last_produit", last_products)
    params = f.messageInfo() # récupération des messages d'info
    return render_template("index.html", **params, last_products=last_products, categories=categories)

#page home
@app.route("/menu")
def menu():
    produits_menu = session.get('meal', [])  # Récupère les produits du repas
    return render_template("menu.html", produits_menu=produits_menu)

@app.route("/CV_Majdi")
def CV_Majdi():
    return render_template("CV_Majdi.html")

@app.route("/CV_Julie")
def CV_Julie():
    return render_template("CV_Julie.html")

@app.route("/CV_Margot")
def CV_Margot():
    return render_template("CV_Margot.html")

@app.route("/CV_Lea")
def CV_Lea():
    return render_template("CV_Lea.html")

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

@app.route("/recherche")
def recherche():
    return render_template("recherche.html")

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

@app.route("/update_status", methods=['post'])
def update_status():
    idUtilisateur = request.form.get('id_membre') 
    statut = request.form.get('nouveau_statut')
    if statut == "Administrateur":
        statut = "admin"
        admin = 1
    else:
        statut = "gestionnaire"
        admin = 0
    bdd.update_userData('statut', statut, idUtilisateur)
    bdd.update_userData('admin', admin, idUtilisateur)
    return redirect(url_for('admin'))



def ecrire_code_html(nom_fichier,nom_produit,image,qtsucre):
    # Code HTML du produit
    code_html = f"""
                <div class="col-md-6 col-lg-6 col-xl-4">
                    <div class="rounded shadow-sm position-relative fruite-item border border-primary">
                        <div class="fruite-img">
                            <img src="static/img/{image}" class="img-fluid w-100 rounded-top" alt="">
                        </div>
                        <div class="p-4 border border-primary border-top-0 rounded-bottom">
                            <h4 class="text-primary">{nom_produit}</h4>
                            <div class="d-flex justify-content-between align-items-center">
                                <p class="text-dark fs-5 fw-bold mb-0"> {qtsucre} g / portion</p>
                                <button type="button" class="btn btn-primary rounded-pill px-3">Ajouter au panier</button>
                            </div>
                        </div>
                    </div>
                </div>
        """
    print(code_html)
    # Ouvrir le fichier en mode écriture
    with open(nom_fichier, "a") as fichier:
        # Écrire le code HTML dans le fichier
        fichier.write(code_html)
        fichier.close()

def suppression_code_html(nom_fichier):
    # Ouvrir le fichier en mode écriture
    with open(nom_fichier, "w") as fichier:
        # Écrire le code HTML dans le fichier
        fichier.write("")
        fichier.close()


@app.route("/votre_page_de_resultats", methods=['post'])
def votre_page_de_resultats():
    suppression_code_html("sujet_groupeE\\template\\recherche.html")
    mot = request.form.get('keyword').lower()  # Convertir le mot de recherche en minuscules
    produit = bdd.get_produitData()
    images = bdd.get_imageData()
    qtsucre = bdd.get_qtsurcreData()
    print(qtsucre)
    for i in range(len(produit)):
        if mot[:3] == produit[i]['nom'].lower()[:3]: 
            ecrire_code_html("sujet_groupeE\\template\\recherche.html", produit[i]['nom'],images[i]['image'],qtsucre[i]['qtsucre'])
    return redirect(url_for('recherche'))



@app.route("/ajout_produit", methods=['POST'])
def ajout_produit():
    photo_produit = request.files['photo_produit']
    filename = secure_filename(photo_produit.filename) 
    photo_produit.save(os.path.join('sujet_groupeE\static\img', filename))
    nom_produit = request.form.get('nom_produit')
    marque = request.form.get('marque')
    quantite_sucre = request.form.get('quantite_sucre')
    categorie = request.form.get('categorie')
    idUtilisateur = session['idUtilisateur']
    bdd.add_produit(nom_produit, marque, quantite_sucre, categorie, idUtilisateur, filename)  
    return redirect(url_for('compte'))



@app.route('/produits')
@app.route('/produits/<int:page>')
@app.route('/produits/categorie/<int:category_id>')
@app.route('/produits/categorie/<int:category_id>/<int:page>')
def produits(page=1, category_id=None):
    categories = {
        1: "Goûter/Dessert",
        2: "Produits Laitiers",
        3: "Sauce",
        4: "Fruits/Légumes",
        5: "Viande/Poisson",
        6: "Boisson",
        7: "Féculents/Céréales"
    }
    per_page = 15
    if category_id:
        produits = bdd.get_produitData_per_categorie(category_id)
    else:
        produits = bdd.get_produitData_per_15(page, per_page)
    total = bdd.get_total_produit()  # Cette fonction doit retourner le nombre total de produits
    total_pages = ceil(total / per_page)  # Ajoutez cette ligne pour calculer le nombre total de pages
    total_produits_par_categorie = bdd.get_total_produit_per_categorie()

    next_url = url_for('produits', page=page + 1) if total > page * per_page else None
    prev_url = url_for('produits', page=page - 1) if page > 1 else None

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render_template('produits_partiel.html', produits=produits, next_url=next_url, prev_url=prev_url, total_pages=total_pages, current_page=page, categories=categories, total_produits_par_categorie=total_produits_par_categorie)
    else:
        return render_template('produits.html', produits=produits, next_url=next_url, prev_url=prev_url, total_pages=total_pages, current_page=page, categories=categories, total_produits_par_categorie=total_produits_par_categorie)
    
@app.route('/add_to_meal', methods=['POST'])
def add_to_meal():
    data = request.get_json()
    print("data",data)  # Ajoutez cette ligne pour afficher les données reçues 
    produit_nom = data.get('nom_produit')
    produit_cat = data.get('idCategorie')
    produit_qtsucre = data.get('qtsucre')
    produit_image = data.get('image')
    produit_id = data.get('idProduit')

    meal = session.get('meal', [])
    meal.append({'nom_produit': produit_nom, 'idCategorie': produit_cat, 'qtsucre': produit_qtsucre, 'image': produit_image, 'idProduit': produit_id})
    session['meal'] = meal
    session.modified = True
    print(session['meal'])
    return jsonify({'productCount': len(meal)})
    

@app.route('/delete_product', methods=['POST'])
def delete_product():
    data = request.get_json()
    print("data",data)  # Ajoutez cette ligne pour afficher les données reçues
    product_id = data.get('id')  # Utilisez la clé 'id' pour obtenir l'ID du produit
    meal = session.get('meal', [])
    meal = [product for product in meal if product['idProduit'] != product_id]
    session['meal'] = meal
    print(session['meal'])
    print("len(meal): ", len(meal))
    return jsonify({'productCount': len(meal)})