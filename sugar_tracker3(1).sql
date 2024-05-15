-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mer. 15 mai 2024 à 17:32
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
CREATE DATABASE IF NOT EXISTS `sugar_tracker3` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `sugar_tracker3`;

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
  `qtsucre` varchar(30) DEFAULT NULL,
  `idCategorie` int(11) DEFAULT NULL,
  `idUtilisateur` int(11) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `produit`
--

INSERT INTO `produit` (`idProduit`, `nom`, `marque`, `qtsucre`, `idCategorie`, `idUtilisateur`, `image`) VALUES
(1, 'nutella', 'ferrero', '8.44', 1, 1, NULL),
(2, 'prince', 'lu', '6.8', 1, 1, NULL),
(3, 'coca-cola', 'coca-cola', '35', 6, 1, NULL),
(4, 'skyr', 'yoplait', '3.6', 2, 1, NULL),
(5, 'pain_de_mie_complet', 'pasquier', '4.21', 7, 1, NULL),
(6, 'napolitain', 'lu', '9.8', 1, 1, NULL),
(7, 'mayonnaise', 'amora', '0.225', 3, 1, NULL),
(8, 'ketchup', 'amora', '3.15', 3, 1, NULL),
(9, 'vache_qui_rit', 'vache_qui_rit', '0.96', 2, 1, NULL),
(10, 'beurre_doux', 'president', '0.8', 2, 1, NULL),
(11, 'spaghetti', 'barilla', '2.98', 7, 1, NULL),
(12, 'sauce_tomate_basilic', 'barilla', '5.9', 3, 1, NULL),
(13, 'riz', 'taureau_aile', '0.2', 7, 1, NULL),
(14, 'semoule', 'tipiak', '1.6', 7, 1, NULL),
(15, 'jambon', 'herta', '0.5', 5, 1, NULL),
(16, 'steak_hache', 'charal', '0', 5, 1, NULL),
(17, 'knacki', 'herta', '1.9', 5, 1, NULL),
(18, 'poulet', 'herta', '0.5', 5, 1, NULL),
(19, 'dinde', 'herta', '0.5', 5, 1, NULL),
(20, 'nuggets', 'le_gaulois', '0.9', 5, 1, NULL),
(21, 'frites', 'mc_cain', '0.5', 7, 1, NULL),
(22, 'maïs', 'bonduelle', '7.28', 4, 1, NULL),
(23, 'haricots_verts', 'bonduelle', '1.3', 4, 1, NULL),
(24, 'madeleine', 'st_michel', '3.91', 1, 4, NULL),
(25, 'compote_pomme', 'andros', '17', 1, 1, NULL),
(26, 'compote_poire', 'andros', '15', 1, 1, NULL),
(27, 'compote_fraise', 'andros', '15', 1, 1, NULL),
(28, 'chocapic', 'nestle', '3.9', 7, 1, NULL),
(29, 'belvita', 'lu', '3.38', 1, 1, NULL),
(30, 'chocolat_lait', 'milka', '9.19', 1, 1, NULL),
(31, 'chocolat_noir', 'nestle', '11.6', 1, 1, NULL),
(32, 'lait', 'candia', '12', 6, 1, NULL),
(33, 'saumon_fume', 'petit_navire', '0.5', 5, 1, NULL),
(34, 'thon', 'petit_navire', '0', 5, 1, NULL),
(35, 'oasis_tropical', 'oasis', '15.6', 6, 1, NULL),
(36, 'ice_tea', 'lipton', '7.5', 6, 1, NULL),
(37, 'kinder_bueno', 'kinder', '8.86', 1, 1, NULL),
(38, 'chips', 'pringles', '0.42', 1, 1, NULL),
(39, 'belin', 'monaco', '1.4', 1, 1, NULL),
(40, 'biere_tequila', 'desperados', '7.26', 6, 1, NULL),
(41, 'jus_dorange', 'joker', '12.9', 6, 1, NULL),
(42, 'jus_multifruit', 'joker', '10', 6, 1, NULL),
(43, 'veloute_de_legumes', 'liebig', '1.4', 4, 1, NULL),
(44, 'schoko_bons', 'kinder', '3.03', 1, 1, NULL),
(45, 'glace_vanille', 'carte_dor', '9', 1, 1, NULL);

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
  `mail` varchar(50) DEFAULT NULL,
  `motPasse` char(64) DEFAULT NULL,
  `statut` varchar(20) DEFAULT NULL,
  `admin` tinyint(1) DEFAULT NULL,
  `avatar` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `utilisateur`
--

INSERT INTO `utilisateur` (`idUtilisateur`, `login`, `nom`, `prenom`, `mail`, `motPasse`, `statut`, `admin`, `avatar`) VALUES
(2, 'admin', 'Terrin', 'Lea', 'leaterrin@gmail.com', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 'gestionnaire', 0, 'avatar6'),
(3, 'Léa', 'Terrin', 'Léa', 'leaterrin@gmail.com', '2f9b41cb15524d25550b14708d0f706fc01365135102d6e7f16756223f698a2c', 'gestionnaire', 0, 'avatar6'),
(5, 'sisalama', 'SI SALAH', 'Majdi', 'sisalahmajdi@gmail.com', 'f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9', 'admin', 1, 'avatar5'),
(6, 'Julie', 'Lombardi', 'Julie', 'c@c.c', '9f13e2b013a7c621dd1be1cf1caa05d2f785507fd7fb2ba70729aca6d650f2e7', 'admin', 1, 'avatar4'),
(7, 'margotte', 'Deveil Villelga', 'Margot', 'margot.deveil@gmail.com', '4d8213eb7377dfefbdca96ab6f4f5e9f1837e1a233abf5680db2eb0865dfd2e6', 'gestionnaire', 0, 'avatar8');

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
