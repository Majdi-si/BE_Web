-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : dim. 09 juin 2024 à 19:09
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `sugar_tracker3`
--

-- --------------------------------------------------------

--
-- Structure de la table `categorie`
--

CREATE TABLE `categorie` (
  `idCategorie` int(11) NOT NULL,
  `nom` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`idCategorie`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;


--
-- Déchargement des données de la table `categorie`
--

INSERT INTO `categorie` (`idCategorie`, `nom`) VALUES
(1, 'gouter_dessert'),
(2, 'produits_laitiers'),
(3, 'sauce'),
(4, 'fruits_légumes'),
(5, 'viande_poisson'),
(6, 'boisson'),
(7, 'feculents_cereales');

-- --------------------------------------------------------

--
-- Structure de la table `produit`
--

CREATE TABLE `produit` (
  `idProduit` int(11) NOT NULL,
  `nom` varchar(30) DEFAULT NULL,
  `marque` varchar(30) DEFAULT NULL,
  `qtsucre` double DEFAULT NULL,
  `idCategorie` int(11) DEFAULT NULL,
  `idUtilisateur` int(11) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`idProduit`),
  FOREIGN KEY (`idCategorie`) REFERENCES `categorie`(`idCategorie`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;


--
-- Déchargement des données de la table `produit`
--

INSERT INTO `produit` (`idProduit`, `nom`, `marque`, `qtsucre`, `idCategorie`, `idUtilisateur`, `image`) VALUES
(1, 'nutella', 'ferrero', 56.3, 1, 1, 'nutella.jpg'),
(2, 'prince', 'lu', 32, 1, 1, 'prince_lu.webp'),
(3, 'coca-cola', 'coca-cola', 10.6, 6, 1, 'coca.jpg'),
(4, 'skyr', 'yoplait', 3.6, 2, 1, 'skyr.jpeg'),
(5, 'pain_de_mie_complet', 'pasquier', 4.9, 7, 1, 'pain_de_mie.jpeg'),
(6, 'napolitain', 'lu', 33, 1, 1, 'napolitain.jpg'),
(7, 'mayonnaise', 'amora', 1, 3, 1, 'mayonnaise.jpg'),
(8, 'ketchup', 'amora', 22.8, 3, 1, 'ketchup.jpg'),
(9, 'vache_qui_rit', 'vache_qui_rit', 6, 2, 1, 'vache_qui_rit.png'),
(10, 'beurre_doux', 'president', 1, 2, 1, 'beurre_doux.jpeg'),
(11, 'spaghetti', 'barilla', 3.5, 7, 1, 'spaghetti.jpg'),
(12, 'sauce_tomate_basilic', 'barilla', 5.9, 3, 1, 'sauce_tomate_basilic.jpeg'),
(13, 'riz', 'taureau_aile', 0.2, 7, 1, 'riz.jpg'),
(14, 'semoule', 'tipiak', 1.6, 7, 1, 'semoule.jpg'),
(15, 'jambon', 'herta', 0.5, 5, 1, 'jambon_herta.jpg'),
(16, 'steak_hache', 'charal', 0, 5, 1, 'steak_hache_charal.jpg'),
(17, 'knacki', 'herta', 1.9, 5, 1, 'knacki.png'),
(18, 'poulet', 'herta', 0.5, 5, 1, 'poulet_herta.jpg'),
(19, 'dinde', 'herta', 0.5, 5, 1, 'dinde_herta.jpg'),
(20, 'nuggets', 'le_gaulois', 0.9, 5, 1, 'nuggets.jpg'),
(21, 'frites', 'mc_cain', 0.5, 7, 1, 'frites_mc_cain.png'),
(22, 'maïs', 'bonduelle', 5.2, 4, 1, 'mais_bonduelle.jpg'),
(23, 'haricots_verts', 'bonduelle', 0.5, 4, 1, 'haricots_verts.jpg'),
(24, 'madeleine', 'st_michel', 23, 1, 4, 'madeleine_st_michel.jpeg'),
(25, 'compote_pomme', 'andros', 12, 1, 1, 'compote_pomme.jpg'),
(26, 'compote_poire', 'andros', 20, 1, 1, 'compote_poire.jpg'),
(27, 'compote_fraise', 'andros', 11, 1, 1, 'compote_fraise.jpg'),
(28, 'chocapic', 'nestle', 22.4, 7, 1, 'chocapic.jpg'),
(29, 'belvita', 'lu', 27, 1, 1, 'belvita_lu.jpg'),
(30, 'chocolat_lait', 'milka', 55, 1, 1, 'chocolat_lait_milka.jpg'),
(31, 'chocolat_noir', 'nestle', 7, 1, 1, 'chocolat_noir_nestle.jpg'),
(32, 'lait', 'candia', 0, 6, 1, 'lait_candia.jpeg'),
(33, 'saumon_fume', 'petit_navire', 0.6, 5, 1, 'saumon_fume.jpg'),
(34, 'thon', 'petit_navire', 0, 5, 1, 'thon_petit_navire.jpg'),
(35, 'oasis_tropical', 'oasis', 7.8, 6, 1, 'oasis_tropical.jpg'),
(36, 'ice_tea', 'lipton', 3, 6, 1, 'ice_tea.jpeg'),
(37, 'kinder_bueno', 'kinder', 41.2, 1, 1, 'kinder_bueno.png'),
(38, 'chips', 'pringles', 1.4, 1, 1, 'pringles_original.jpg'),
(39, 'belin', 'monaco', 5.6, 1, 1, 'belin_monaco.jpg'),
(40, 'biere_tequila', 'desperados', 2.2, 6, 1, 'biere_tequila.jpg'),
(41, 'jus_dorange', 'joker', 8.6, 6, 1, 'jus_orange.jpeg'),
(42, 'jus_multifruit', 'joker', 8.2, 6, 1, 'jus_multifruit.jpeg'),
(43, 'veloute_de_legumes', 'liebig', 1.32, 4, 1, 'veloute_de_legumes.jpg'),
(44, 'schoko_bons', 'kinder', 52.2, 1, 1, 'schoko_bons.jpg'),
(45, 'glace_vanille', 'carte_dor', 9, 1, 1, 'glace_vanille.jpg'),
(47, 'Pain au lait', 'Pasquier', 11, 1, 5, 'prod_pal_x10_2022.jpg'),
(48, 'Sauce algérienne', 'Samia', 8.9, 3, 5, 'sauce-alger.webp'),
(49, 'banane', 'Carrefour', 12, 4, 3, 'banane.jpg'),
(50, 'fraise', 'Carrefour', 4.9, 4, 3, 'fraise.webp'),
(51, 'courgette', 'carrefour', 1.67, 4, 3, 'courgette.jpg'),
(52, 'pomme', 'carrefour', 10, 4, 3, 'pomme.png'),
(53, 'Yaourt nature', 'Danone', 5.7, 2, 3, 'veloute.jpg'),
(54, 'Emmental rapé', 'Président', 1, 2, 3, 'rape.jpg'),
(55, 'tomates', 'carrefour', 1.7, 4, 3, 'tomate.jpg'),
(56, 'concombre', 'carrefour', 1.67, 4, 3, 'concombre.jpg'),
(57, 'avocat', 'carrefour', 0.9, 4, 3, 'avocat.webp'),
(58, 'asperge', 'carrefour', 1.88, 4, 3, 'asperge.webp'),
(59, 'poivron', 'carrefour', 4.2, 4, 3, 'poivron.jpg'),
(60, 'Tortillas', 'Old el paso', 2.1, 7, 3, 'tortilla.webp'),
(61, 'crème fraiche', 'bridélice', 3.9, 2, 3, 'creme.avif'),
(62, 'poulet', 'Le Gaulois', 0.5, 5, 3, 'poulet.jpg'),
(63, 'lardons', 'Herta', 7, 5, 3, 'lardon.jpg'),
(64, 'Kinder Délice', 'Kinder', 58.8, 1, 4, 'telechargement.jpeg');

-- --------------------------------------------------------

--
-- Structure de la table `repas`
--

CREATE TABLE `repas` (
  `idProduit` int(11) NOT NULL,
  `idUtilisateur` int(11) NOT NULL,
  `nom_produit` varchar(50) NOT NULL,
  `quantité` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `repas`
--

INSERT INTO `repas` (`idProduit`, `idUtilisateur`, `nom_produit`, `quantité`) VALUES
(1, 1, 'nutella', 102),
(2, 1, 'prince', 10),
(5, 3, 'pain_de_mie_complet', 1),
(1, 3, 'nutella', 11),
(9, 4, 'vache_qui_rit', 50),
(12, 4, 'sauce_tomate_basilic', 40),
(30, 4, 'chocolat_lait', 40),
(29, 4, 'belvita', 45),
(44, 5, 'schoko_bons', 100),
(48, 5, 'Sauce algérienne', 100),
(56, 5, 'concombre', 100),
(32, 5, 'lait', 50),
(28, 5, 'chocapic', 50),
(42, 5, 'jus_multifruit', 30);

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

CREATE TABLE `utilisateur` (
  `idUtilisateur` int(11) NOT NULL,
  `login` varchar(30) DEFAULT NULL,
  `nom` varchar(30) DEFAULT NULL,
  `prenom` varchar(30) DEFAULT NULL,
  `age` double DEFAULT NULL,
  `mail` varchar(50) DEFAULT NULL,
  `motPasse` char(64) DEFAULT NULL,
  `qtmax` float DEFAULT NULL,
  `statut` varchar(20) DEFAULT NULL,
  `avatar` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `utilisateur`
--

INSERT INTO `utilisateur` (`idUtilisateur`, `login`, `nom`, `prenom`, `age`, `mail`, `motPasse`, `qtmax`, `statut`, `avatar`) VALUES
(1, 'admin', 'admin', 'admin', 99, 'admin@admin.com', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 25, 'admin', 'avatar6'),
(3, 'margotte', 'Deveil', 'Margot', 20, 'margot@gmail.com', '4d8213eb7377dfefbdca96ab6f4f5e9f1837e1a233abf5680db2eb0865dfd2e6', 15, 'gestionnaire', 'avatar2'),
(4, 'Lea-T', 'Terrin', 'Léa', 20, 'leaterrin@gmail.com', 'f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9', 100, 'admin', 'avatar4'),
(5, 'lombarju', 'LOMBARDI', 'Julie', 21, 'julielombardi@outlook.fr', 'd948c51c0ddbb19828ee99d80ad3cae2301fefb37571ca8f8eb4e9619273db99', 100, 'gestionnaire', 'avatar2');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
