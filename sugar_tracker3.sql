-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : ven. 24 mai 2024 à 07:44
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
  `nom` varchar(30) DEFAULT NULL
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
  `qtsucre` float(30) DEFAULT NULL,
  `idCategorie` int(11) DEFAULT NULL,
  `idUtilisateur` int(11) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `produit`
--

INSERT INTO `produit` (`idProduit`, `nom`, `marque`, `qtsucre`, `idCategorie`, `idUtilisateur`, `image`) VALUES
(1, 'nutella', 'ferrero', '56.3', 1, 1, 'nutella.jpg'),
(2, 'prince', 'lu', '32', 1, 1, 'prince_lu.webp'),
(3, 'coca-cola', 'coca-cola', '10.6', 6, 1, 'coca.jpg'),
(4, 'skyr', 'yoplait', '3.6', 2, 1, 'skyr.jpeg'),
(5, 'pain_de_mie_complet', 'pasquier', '4.9', 7, 1, 'pain_de_mie.jpeg'),
(6, 'napolitain', 'lu', '33', 1, 1, 'napolitain.jpg'),
(7, 'mayonnaise', 'amora', '1', 3, 1, 'mayonnaise.jpg'),
(8, 'ketchup', 'amora', '22.8', 3, 1, 'ketchup.jpg'),
(9, 'vache_qui_rit', 'vache_qui_rit', '6', 2, 1, 'vache_qui_rit.png'),
(10, 'beurre_doux', 'president', '1', 2, 1, 'beurre_doux.jpeg'),
(11, 'spaghetti', 'barilla', '3.5', 7, 1, 'spaghetti.jpg'),
(12, 'sauce_tomate_basilic', 'barilla', '5.9', 3, 1, 'sauce_tomate_basilic.jpeg'),
(13, 'riz', 'taureau_aile', '0.2', 7, 1, 'riz.jpg'),
(14, 'semoule', 'tipiak', '1.6', 7, 1, 'semoule.jpg'),
(15, 'jambon', 'herta', '0.5', 5, 1, 'jambon_herta.jpg'),
(16, 'steak_hache', 'charal', '0', 5, 1, 'steak_hache_charal.jpg'),
(17, 'knacki', 'herta', '1.9', 5, 1, 'knacki.png'),
(18, 'poulet', 'herta', '0.5', 5, 1, 'poulet_herta.jpg'),
(19, 'dinde', 'herta', '0.5', 5, 1, 'dinde_herta.jpg'),
(20, 'nuggets', 'le_gaulois', '0.9', 5, 1, 'nuggets.jpg'),
(21, 'frites', 'mc_cain', '0.5', 7, 1, 'frites_mc_cain.png'),
(22, 'maïs', 'bonduelle', '5.2', 4, 1, 'mais_bonduelle.jpg'),
(23, 'haricots_verts', 'bonduelle', '0.5', 4, 1, 'haricots_verts.jpg'),
(24, 'madeleine', 'st_michel', '23', 1, 4, 'madeleine_st_michel.jpeg'),
(25, 'compote_pomme', 'andros', '12', 1, 1, 'compote_pomme.jpg'),
(26, 'compote_poire', 'andros', '20', 1, 1, 'compote_poire.jpg'),
(27, 'compote_fraise', 'andros', '11', 1, 1, 'compote_fraise.jpg'),
(28, 'chocapic', 'nestle', '22.4', 7, 1, 'chocapic.jpg'),
(29, 'belvita', 'lu', '27', 1, 1, 'belvita_lu.jpg'),
(30, 'chocolat_lait', 'milka', '55', 1, 1, 'chocolat_lait_milka.jpg'),
(31, 'chocolat_noir', 'nestle', '7', 1, 1, 'chocolat_noir_nestle.jpg'),
(32, 'lait', 'candia', '0', 6, 1, 'lait_candia.jpeg'),
(33, 'saumon_fume', 'petit_navire', '0.6', 5, 1, 'saumon_fume.jpg'),
(34, 'thon', 'petit_navire', '0', 5, 1, 'thon_petit_navire.jpg'),
(35, 'oasis_tropical', 'oasis', '7.8', 6, 1, 'oasis_tropical.jpg'),
(36, 'ice_tea', 'lipton', '3', 6, 1, 'ice_tea.jpeg'),
(37, 'kinder_bueno', 'kinder', '41.2', 1, 1, 'kinder_bueno.png'),
(38, 'chips', 'pringles', '1.4', 1, 1, 'pringles_original.jpg'),
(39, 'belin', 'monaco', '5.6', 1, 1, 'belin_monaco.jpg'),
(40, 'biere_tequila', 'desperados', '2.2', 6, 1, 'biere_tequila.jpg'),
(41, 'jus_dorange', 'joker', '8.6', 6, 1, 'jus_orange.jpeg'),
(42, 'jus_multifruit', 'joker', '8.2', 6, 1, 'jus_multifruit.jpeg'),
(43, 'veloute_de_legumes', 'liebig', '1.32', 4, 1, 'veloute_de_legumes.jpg'),
(44, 'schoko_bons', 'kinder', '52.2', 1, 1, 'schoko_bons.jpg'),
(45, 'glace_vanille', 'carte_dor', '9', 1, 1, 'glace_vanille.jpg'),
(47, 'Pain au lait', 'Pasquier', '11', 1, 5, 'prod_pal_x10_2022.jpg'),
(48, 'Sauce algérienne', 'Samia', '8.9', 3, 5, 'sauce-alger.webp');

-- --------------------------------------------------------

--
-- Structure de la table `repas`
--

CREATE TABLE `repas` (
  `idProduit` int(11) NOT NULL,
  `idUtilisateur` int(11) NOT NULL,
  `plats` enum('petit-dej','dejeuner','gouter','diner') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `repas`
--

INSERT INTO `repas` (`idProduit`, `idUtilisateur`, `plats`) VALUES
(1, 1, 'petit-dej'),
(2, 1, 'petit-dej');

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

CREATE TABLE `utilisateur` (
  `idUtilisateur` int(11) NOT NULL,
  `login` varchar(30) DEFAULT NULL,
  `nom` varchar(30) DEFAULT NULL,
  `prenom` varchar(30) DEFAULT NULL,
  `age` float(30) DEFAULT NULL,
  `mail` varchar(50) DEFAULT NULL,
  `motPasse` char(64) DEFAULT NULL,
  `qtmax` float(10) DEFAULT NULL,
  `statut` varchar(10) DEFAULT NULL,
  `avatar` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `utilisateur`
--

INSERT INTO `utilisateur` (`idUtilisateur`, `login`, `nom`, `prenom`,`age`, `mail`, `motPasse`,`qtmax`, `statut`, `avatar`) VALUES
(3, 'Léa', 'Terrin', 'Léa','20', 'leaterrin@gmail.com', '2f9b41cb15524d25550b14708d0f706fc01365135102d6e7f16756223f698a2c','100', 'gestionnaire', 'avatar6'),
(5, 'sisalama', 'SI SALAH', 'Majdi', 'sisalahmajdi@gmail.com', 'f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9','100', 'admin', 'avatar5'),
(6, 'Julie', 'Lombardi', 'Julie', 'c@c.c', '9f13e2b013a7c621dd1be1cf1caa05d2f785507fd7fb2ba70729aca6d650f2e7','100' ,'admin', 1, 'avatar4'),
(7, 'margotte', 'Deveil Villelga', 'Margot', 'margot.deveil@gmail.com', '4d8213eb7377dfefbdca96ab6f4f5e9f1837e1a233abf5680db2eb0865dfd2e6','100', 'gestionnaire', 'avatar8'),
(8, 'Lea-T', 'Terrin', 'Léa', 'c@c.c', '2f9b41cb15524d25550b14708d0f706fc01365135102d6e7f16756223f698a2c','100', 'admin', 'avatar4');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `categorie`
--
ALTER TABLE `categorie`
  ADD PRIMARY KEY (`idCategorie`);

--
-- Index pour la table `produit`
--
ALTER TABLE `produit`
  ADD PRIMARY KEY (`idProduit`),
  ADD KEY `idCategorie` (`idCategorie`),
  ADD KEY `idUtilisateur` (`idUtilisateur`);

--
-- Index pour la table `repas`
--
ALTER TABLE `repas`
  ADD PRIMARY KEY (`idProduit`,`idUtilisateur`),
  ADD KEY `idUtilisateur` (`idUtilisateur`);

--
-- Index pour la table `utilisateur`
--
ALTER TABLE `utilisateur`
  ADD PRIMARY KEY (`idUtilisateur`);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `produit`
--
ALTER TABLE `produit`
  ADD CONSTRAINT `produit_ibfk_1` FOREIGN KEY (`idCategorie`) REFERENCES `categorie` (`idCategorie`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
