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
    categories = bdd.get_categorieData()
    last_products = bdd.get_latest_products()
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
    age_connexion = request.form['age']

    ## Gestion du fichier avatar
    # avatar_connexion = None
    # avatar_extension = None
    # if 'avatar' in request.files:
    #     avatar_file = request.files['avatar']
    #     if avatar_file.filename != '':
    #         avatar_extension = os.path.splitext(avatar_file.filename)[1][1:]  # get file extension
    #         avatar_connexion = secure_filename(avatar_file.filename)
    #         avatar_file.save(os.path.join(app.config['UPLOAD_FOLDER'], avatar_connexion))

    avatar_connexion = None
    if 'avatar' in request.form:
        avatar_connexion = request.form['avatar']
    else:
        # Gérer le cas où 'avatar' n'est pas présent
        print("Le fichier 'avatar' n'est pas présent dans la requête.")

    if int(age_connexion) >= 18:
        qtmax = 25 #quantité de sucre max par jour pour un adulte
    else:
        qtmax = 15 #quantité de sucre max par jour

    lastId = bdd.add_userData(nom_connexion, prenom_connexion, mail_connexion, login_connexion, mdp_connexion, statut_connexion, avatar_connexion, age_connexion, qtmax) #ajouter avatar_extension
    if lastId == 0:  # Si l'insertion a échoué
        data = bdd.get_membresData()
        lastId = data[-1]['idUtilisateur']
    # print(lastId) # dernier id créé par le serveur de BDD
    # if "errorDB" not in session: 
    #     session["infoVert"]="Nouveau membre inséré"
    # else:
    #     session["infoRouge"]="Problème ajout utilisateur"

    # Stocke les informations de l'utilisateur dans la session
    session['idUtilisateur'] = lastId
    session['login'] = login_connexion
    session['nom'] = nom_connexion
    session['prenom'] = prenom_connexion
    session['mail'] = mail_connexion
    session['avatar'] = avatar_connexion
    session['statut'] = statut_connexion
    session['mdp'] = mdp_connexion
    session['age'] = age_connexion
    session['qtmax'] = qtmax
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
        session["age"]=user["age"]
        session["avatar"] = user["avatar"]
        session["login"] = user["login"]
        session["mdp"] = mdp
        session["qtmax"] = user["qtmax"]
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
    categories = bdd.get_categorieData()
    return render_template("compte.html", categories=categories)

@app.route("/recherche")
def recherche():
    return render_template("recherche.html")

@app.route("/rien")
def rien():
    return render_template("rien.html")

@app.route("/admin")
def admin():
    membres = bdd.get_membresData()
    return render_template("admin.html", membres=membres)

@app.route("/delete_member", methods=['POST'])
def delete_membre():
    id_membre = request.form.get('id_membre')
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
    age = request.form.get('age')
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
        bdd.update_userData('age', age, session['idUtilisateur'])

        # Mettre à jour les informations de la session
        session['prenom'] = prenom
        session['nom'] = nom
        session['login'] = login
        session['mail'] = mail
        session['statut'] = statut
        session['age'] = age
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



def ecrire_code_html(nom_fichier, nom_produit, image, qtsucre):
    # Générer le HTML à partir du template
    code_html = f'''div class="col-md-6 col-lg-6 col-xl-4">
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
                </div>'''
    # Ouvrir le fichier en mode écriture
    with open(nom_fichier, 'a', encoding='utf-8') as fichier:
        new_text = fichier[263:]
        new_text.write(code_html)
        new_text.close()


# def ecrire_rien(fichier):
#     with open(fichier, "a", encoding='utf-8') as fichier:
#         fichier.write(f'Aucun produit ne correspond à votre recherche')
#         fichier.close()


def suppression_code_html(nom_fichier,n):
    # Ouvrir le fichier en mode écriture
    with open(nom_fichier[263:n*15+263], "w",encoding='utf-8') as fichier:
        # Écrire le code HTML dans le fichier
        fichier.write("")
        fichier.close()


@app.route("/votre_page_de_resultats", methods=['post'])
def votre_page_de_resultats():
    n=0
    #suppression_code_html("sujet_groupeE\\template\\recherche.html",n)
    mot = request.form.get('keyword').lower()  # Convertir le mot de recherche en minuscules
    print("Mot de recherche: ", mot)
    produit = bdd.get_produitData()
    images = bdd.get_imageData()
    qtsucre = bdd.get_qtsurcreData()
    for i in range(len(produit)):
        if mot[:3] == produit[i]['nom'].lower()[:3]: 
            print("Produit trouvé: ", produit[i]['nom'])
            n=n+1
            ecrire_code_html("BE_Web\sujet_groupeE\\template\\recherche.html", produit[i]['nom'],images[i]['image'],qtsucre[i]['qtsucre'])
    if n==0 :
        return redirect(url_for('rien'))
    return redirect(url_for('recherche'))



@app.route("/ajout_produit", methods=['POST'])
def ajout_produit():
    photo_produit = request.files['photo_produit']
    filename = secure_filename(photo_produit.filename) 
    photo_produit.save(os.path.join('sujet_groupeE\static\img', filename))
    nom_produit = request.form.get('nom_produit')
    nom_produit = ''.join(nom_produit)
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
    categories = bdd.get_categorieData()
    per_page = 15
    if category_id:
        produits = bdd.get_produitData_per_categorie(category_id)
    else:
        produits = bdd.get_produitData_per_15(page, per_page)
    total = bdd.get_total_produit()  # Cette fonction doit retourner le nombre total de produits
    total_pages = ceil(total / per_page)  # Ajoutez cette ligne pour calculer le nombre total de pages
    total_produits_par_categorie = bdd.get_total_produit_per_categorie()
    print("total_produits_par_categorie", total_produits_par_categorie)

    next_url = url_for('produits', page=page + 1) if total > page * per_page else None
    prev_url = url_for('produits', page=page - 1) if page > 1 else None

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render_template('produits_partiel.html', produits=produits, next_url=next_url, prev_url=prev_url, total_pages=total_pages, current_page=page, categories=categories, total_produits_par_categorie=total_produits_par_categorie)
    else:
        return render_template('produits.html', produits=produits, next_url=next_url, prev_url=prev_url, total_pages=total_pages, current_page=page, categories=categories, total_produits_par_categorie=total_produits_par_categorie)
    
@app.route('/add_to_meal', methods=['POST'])
def add_to_meal():
    data = request.get_json()
    produit_nom = data.get('nom_produit')
    produit_cat = data.get('idCategorie')
    produit_qtsucre = data.get('qtsucre')
    produit_image = data.get('image')
    produit_id = data.get('idProduit')

    meal = session.get('meal', [])
    meal.append({'nom_produit': produit_nom, 'idCategorie': produit_cat, 'qtsucre': produit_qtsucre, 'image': produit_image, 'idProduit': produit_id})
    session['meal'] = meal
    session.modified = True
    return jsonify({'productCount': len(meal)})
    

@app.route('/delete_product', methods=['POST'])
def delete_product():
    data = request.get_json()
    product_id = data.get('id')  # Utilisez la clé 'id' pour obtenir l'ID du produit
    meal = session.get('meal', [])
    meal = [product for product in meal if product['idProduit'] != product_id]
    session['meal'] = meal
    return jsonify({'productCount': len(meal)})

@app.route('/update_product', methods=['POST'])
def update_product():
    data = request.get_json()
    if not data:  # Si l'objet est vide, retournez une réponse sans effectuer aucune action
        return jsonify({'message': 'No data received'})

    idProduit = data.get('update_idProduit')
    nomProduit = data.get('update_nomProduit')
    marque = data.get('update_marque')
    qtsucre = data.get('update_qtsucre')
    idCategorie = data.get('update_idCategorie')
    bdd.update_produitData('nom', nomProduit, idProduit)
    bdd.update_produitData('marque', marque, idProduit)
    bdd.update_produitData('qtsucre', qtsucre, idProduit)
    bdd.update_produitData('idCategorie', idCategorie, idProduit)

    return jsonify({'message': 'Product updated successfully'})

@app.route('/delete_produit/<int:idProduit>', methods=['DELETE'])
def delete_produit(idProduit):
    bdd.delete_produitData(idProduit)
    return redirect(url_for('produits'))

@app.route('/add_category', methods=['POST'])
def add_categorie():
    data = request.get_json()
    print("data", data)
    if data == {'category': ['']}:
        return jsonify({'message': 'No data received'})
    else:  
        categories = data.get('category')

        print("categories", categories)
        for categorie in categories: 
            if categorie == '':
                continue   
            print("catégorie :", categorie)
            # def add_new_categorie(nomCategorie)
            bdd.add_new_categorie(categorie)

    return jsonify({'message': 'Category added successfully'})

@app.route('/delete_category', methods=['POST'])
def delete_categorie():
    data = request.get_json()
    print("data", data )
    category_id = data['category_to_delete']
    print("category_id", category_id)
    bdd.delete_categorieData(category_id)
    return jsonify({'message': 'Category deleted successfully'})

@app.route('/save_products', methods=['POST'])
def save_products():
    # Récupérer les données du corps de la requête
    data = request.get_json()
    print("data", data)

    for product_data in data['products']:
        idProduit = product_data['id']
        quantite = product_data['quantity']
        idUtilisateur = session['idUtilisateur']
        dico_nom_produit = bdd.get_nom_produit(idProduit)
        nom_produit = dico_nom_produit['nom']
        bdd.ajout_repas(idProduit, idUtilisateur, nom_produit, quantite)

    # Retourner une réponse de succès
    return jsonify({'message': 'Les produits ont été enregistrés avec succès.'})

@app.route('/repas')
def repas():
    idUtilisateur = session['idUtilisateur']
    repas = bdd.get_repasData(idUtilisateur)
    total_sucre = 0
    repas = [list(i) for i in repas]  # Convertir chaque tuple en liste
    for i in repas:
        i[4] = round(i[4] * i[3] / 100, 2)
        total_sucre += round(i[4],2)
    return render_template('repas.html', repas=repas, total_sucre=total_sucre)


@app.route('/delete_product_meal', methods=['POST'])
def delete_product_meal():
    id_produit = request.form.get('id_produit')
    bdd.delete_product_meal(id_produit)
    if "errorDB" not in session:
        session["infoVert"] = "Produit supprimé"
    else:
        session["infoRouge"] = "Problème suppression produit"

    return redirect(url_for('repas'))

@app.route('/clear_messages', methods=['POST'])
def clear_messages():
    if "infoVert" in session:
        del session["infoVert"]
    if "infoRouge" in session:
        del session["infoRouge"]
    return jsonify({'message': 'Messages cleared'})