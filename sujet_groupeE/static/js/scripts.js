fetch('compte.html')
    .then(response => response.text())
    .then(data => {
        // Ici, vous pouvez analyser les données et extraire les informations sur les produits
        // Ensuite, vous pouvez les ajouter à votre page "produits.html"
    });