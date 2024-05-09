-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : jeu. 09 mai 2024 à 11:49
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
  `idUtilisateur` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `produit`
--

INSERT INTO `produit` (`idProduit`, `nom`, `marque`, `qtsucre`, `idCategorie`, `idUtilisateur`) VALUES
(1, 'nutella', 'ferrero', '8.44', 1, 1),
(2, 'prince', 'lu', '6.8', 1, 1),
(3, 'coca-cola', 'coca-cola', '35', 6, 1),
(4, 'skyr', 'yoplait', '3.6', 2, 1),
(5, 'pain_de_mie_complet', 'pasquier', '4.21', 7, 1),
(6, 'napolitain', 'lu', '9.8', 1, 1),
(7, 'mayonnaise', 'amora', '0.225', 3, 1),
(8, 'ketchup', 'amora', '3.15', 3, 1),
(9, 'vache_qui_rit', 'vache_qui_rit', '0.96', 2, 1),
(10, 'beurre_doux', 'president', '0.8', 2, 1),
(11, 'spaghetti', 'barilla', '2.98', 7, 1),
(12, 'sauce_tomate_basilic', 'barilla', '5.9', 3, 1),
(13, 'riz', 'taureau_aile', '0.2', 7, 1),
(14, 'semoule', 'tipiak', '1.6', 7, 1),
(15, 'jambon', 'herta', '0.5', 5, 1),
(16, 'steak_hache', 'charal', '0', 5, 1),
(17, 'knacki', 'herta', '1.9', 5, 1),
(18, 'poulet', 'herta', '0.5', 5, 1),
(19, 'dinde', 'herta', '0.5', 5, 1),
(20, 'nuggets', 'le_gaulois', '0.9', 5, 1),
(21, 'frites', 'mc_cain', '0.5', 7, 1),
(22, 'maïs', 'bonduelle', '7.28', 4, 1),
(23, 'haricots_verts', 'bonduelle', '1.3', 4, 1),
(24, 'madeleine', 'st_michel', '3.91', 1, 4),
(25, 'compote_pomme', 'andros', '17', 1, 1),
(26, 'compote_poire', 'andros', '15', 1, 1),
(27, 'compote_fraise', 'andros', '15', 1, 1),
(28, 'chocapic', 'nestle', '3.9', 7, 1),
(29, 'belvita', 'lu', '3.38', 1, 1),
(30, 'chocolat_lait', 'milka', '9.19', 1, 1),
(31, 'chocolat_noir', 'nestle', '11.6', 1, 1),
(32, 'lait', 'candia', '12', 6, 1),
(33, 'saumon_fume', 'petit_navire', '0.5', 5, 1),
(34, 'thon', 'petit_navire', '0', 5, 1),
(35, 'oasis_tropical', 'oasis', '15.6', 6, 1),
(36, 'ice_tea', 'lipton', '7.5', 6, 1),
(37, 'kinder_bueno', 'kinder', '8.86', 1, 1),
(38, 'chips', 'pringles', '0.42', 1, 1),
(39, 'belin', 'monaco', '1.4', 1, 1),
(40, 'biere_tequila', 'desperados', '7.26', 6, 1),
(41, 'jus_dorange', 'joker', '12.9', 6, 1),
(42, 'jus_multifruit', 'joker', '10', 6, 1),
(43, 'veloute_de_legumes', 'liebig', '1.4', 4, 1),
(44, 'schoko_bons', 'kinder', '3.03', 1, 1),
(45, 'glace_vanille', 'carte_dor', '9', 1, 1);

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
(1, 'admin', 'admin', 'admin', 'julielombardi@outlook.fr', 'admin', 'connecte', 1, '');

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
