from flask import Flask, render_template, request
import hashlib
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

@app.route("/ajout", methods=["GET"])
def ajout():
    return "Formulaire POST reçu"
    
#reception donnees du compte
@app.route("/compte")
def compte():
    return render_template("compte.html")

@app.route("/ajouter", methods=["POST"])
def ajouter():
    #return request.form['prenom']
    return "Formulaire POST reçu"

# mdp = hashlib.sha256(mdp.encode())
# mdpC = mdp.hexdigest() #mdpC=mot de pass chiffré

