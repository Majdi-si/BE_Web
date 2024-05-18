// Sélectionner les éléments du DOM
const categorySelect = document.getElementById('categorie');
const sugarRange = document.getElementById('rangeInput');
const productContainer = document.querySelector('.row.g-4.justify-content-center');

// Fonction pour afficher les produits
function displayProducts(products) {
    productContainer.innerHTML = ''; // Effacer les produits actuels
    for (let product of products) {
        // Créer un nouvel élément de produit et l'ajouter au conteneur de produits
        // Vous devrez adapter ce code pour correspondre à la structure de vos produits
        let productElement = document.createElement('div');
        productElement.innerHTML = `
            <div class="rounded position-relative fruite-item">
                <div class="fruite-img">
                    <img src="${product.photo_produit}" class="img-fluid w-100 rounded-top" alt="${product.nom_produit}">
                </div>
                <div class="text-white bg-secondary px-3 py-1 rounded position-absolute" style="top: 10px; left: 10px;">${product.categorie}</div>
                <div class="p-4 border border-secondary border-top-0 rounded-bottom">
                    <h4>${product.nom_produit}</h4>
                    <div class="d-flex justify-content-between flex-lg-wrap">
                        <p class="text-dark fs-5 fw-bold mb-0">${product.quantite_sucre}g/portion</p>
                        <a href="#" class="btn border border-secondary rounded-pill px-3 text-primary"><i class="fas fa-utensils me-2 text-primary"></i> Ajouter au repas</a>
                    </div>
                </div>
            </div>
        `;
        productContainer.appendChild(productElement);
    }
}

// Fonction pour filtrer les produits
function filterProducts() {
    // Récupérer les produits depuis le serveur ou une API
    fetchProducts().then(products => {
        // Filtrer les produits en fonction de la catégorie et de la quantité de sucre
        let filteredProducts = products.filter(product =>
            product.categorie === categorySelect.value &&
            product.quantite_sucre <= sugarRange.value
        );
        // Afficher les produits filtrés
        displayProducts(filteredProducts);
    });
}

// Ajouter des écouteurs d'événements pour filtrer les produits lorsque la catégorie ou la quantité de sucre change
categorySelect.addEventListener('change', filterProducts);
sugarRange.addEventListener('input', filterProducts);

// Filtrer les produits initialement
filterProducts();

const ajoutProduitForm = document.getElementById('ajoutProduitForm');

ajoutProduitForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Empêcher le rechargement de la page

    // Récupérer les valeurs du formulaire
    const nomProduit = document.getElementById('nomProduit').value;
    const categorieProduit = document.getElementById('categorieProduit').value;
    const quantiteSucre = document.getElementById('quantiteSucre').value;

    // Créer l'objet produit
    const produit = {
        nom: nomProduit,
        categorie: categorieProduit,
        sucre: quantiteSucre
    };

    // Envoyer une requête au serveur pour créer le produit
    // Vous devrez remplacer 'URL_DU_SERVEUR' par l'URL de votre serveur
    fetch('URL_DU_SERVEUR', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(produit)
    }).then(response => {
        if (response.ok) {
            alert('Produit ajouté avec succès !');
        } else {
            alert('Erreur lors de l\'ajout du produit.');
        }
    });
});

// Sélectionner les éléments du DOM
const categorySelect = document.getElementById('categorie');
const sugarRange = document.getElementById('rangeInput');
const productContainer = document.querySelector('.row.g-4.justify-content-center');

// Fonction pour afficher les produits
function displayProducts(products) {
    productContainer.innerHTML = ''; // Effacer les produits actuels
    for (let product of products) {
        // Créer un nouvel élément de produit et l'ajouter au conteneur de produits
        // Vous devrez adapter ce code pour correspondre à la structure de vos produits
        let productElement = document.createElement('div');
        productElement.innerHTML = `
            <div class="rounded position-relative fruite-item">
                <div class="fruite-img">
                    <img src="${product.photo_produit}" class="img-fluid w-100 rounded-top" alt="${product.nom_produit}">
                </div>
                <div class="text-white bg-secondary px-3 py-1 rounded position-absolute" style="top: 10px; left: 10px;">${product.categorie}</div>
                <div class="p-4 border border-secondary border-top-0 rounded-bottom">
                    <h4>${product.nom_produit}</h4>
                    <div class="d-flex justify-content-between flex-lg-wrap">
                        <p class="text-dark fs-5 fw-bold mb-0">${product.quantite_sucre}g/portion</p>
                        <a href="#" class="btn border border-secondary rounded-pill px-3 text-primary"><i class="fas fa-utensils me-2 text-primary"></i> Ajouter au repas</a>
                    </div>
                </div>
            </div>
        `;
        productContainer.appendChild(productElement);
    }
}

// Fonction pour filtrer les produits
function filterProducts() {
    // Récupérer les produits depuis le serveur ou une API
    fetchProducts().then(products => {
        // Filtrer les produits en fonction de la catégorie et de la quantité de sucre
        let filteredProducts = products.filter(product =>
            product.categorie === categorySelect.value &&
            product.quantite_sucre <= sugarRange.value
        );
        // Afficher les produits filtrés
        displayProducts(filteredProducts);
    });
}

// Ajouter des écouteurs d'événements pour filtrer les produits lorsque la catégorie ou la quantité de sucre change
categorySelect.addEventListener('change', filterProducts);
sugarRange.addEventListener('input', filterProducts);

// Filtrer les produits initialement
filterProducts();

const ajoutProduitForm = document.getElementById('ajoutProduitForm');

ajoutProduitForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Empêcher le rechargement de la page

    // Récupérer les valeurs du formulaire
    const nomProduit = document.getElementById('nomProduit').value;
    const categorieProduit = document.getElementById('categorieProduit').value;
    const quantiteSucre = document.getElementById('quantiteSucre').value;

    // Créer l'objet produit
    const produit = {
        nom: nomProduit,
        categorie: categorieProduit,
        sucre: quantiteSucre
    };

    // Envoyer une requête au serveur pour créer le produit
    // Vous devrez remplacer 'URL_DU_SERVEUR' par l'URL de votre serveur
    fetch('URL_DU_SERVEUR', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(produit)
    }).then(response => {
        if (response.ok) {
            alert('Produit ajouté avec succès !');
        } else {
            alert('Erreur lors de l\'ajout du produit.');
        }
    });
});

// Définir la fonction pour basculer le mode nuit
function toggleNightMode() {
    document.body.classList.toggle('night-mode');
    // Enregistrer le choix de mode nuit dans le localStorage
    localStorage.setItem('night-mode', document.body.classList.contains('night-mode'));
}

// Ajouter un écouteur d'événement sur le bouton "Mode nuit"
document.getElementById('night-mode-toggle').addEventListener('click', toggleNightMode);

// Vérifier le localStorage au chargement de la page pour déterminer si le mode nuit doit être activé
window.addEventListener('DOMContentLoaded', (event) => {
    if (localStorage.getItem('night-mode') === 'true') {
        document.body.classList.add('night-mode');
    }
});
