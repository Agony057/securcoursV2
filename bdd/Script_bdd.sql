-- ---------------------------------------------------------------------------------------------------------------------------
-- -------------------------------------------- || SAE PARTIE 2 SQL || -------------------------------------------------------
-- ---------------------------------------------------------------------------------------------------------------------------
-- -------------------------------------- || Projet 1 : Gestion des Salles || ------------------------------------------------
-- ---------------------------------------------------------------------------------------------------------------------------
-- 
-- ---------------------------------------------------------------------------------------------------------------------------
-- -------------------------------------------- || Suppression TABLE || ------------------------------------------------------
-- ---------------------------------------------------------------------------------------------------------------------------
-- 
DROP TABLE IF EXISTS Identite CASCADE;
DROP TABLE IF EXISTS Casier CASCADE;
DROP TABLE IF EXISTS Classe CASCADE;
-- 
-- ---------------------------------------------------------------------------------------------------------------------------
-- ----------------------------------------------- || Création TABLE || ------------------------------------------------------
-- ---------------------------------------------------------------------------------------------------------------------------
-- 
CREATE TABLE Classe(
	id VARCHAR(10) NOT NULL CHECK(id IN('Vert', 'Bleu', 'Jaune', 'Rouge', 'Orange', 'Or')),
    Libelle VARCHAR(25) NOT NULL,
    PRIMARY KEY (id)
);
-- 
CREATE TABLE Casier(
	id INT NOT NULL CHECK(id > 0 && id <=2),
	Ouvert BOOLEAN NOT NULL DEFAULT FALSE,
	Libre BOOLEAN NOT NULL DEFAULT TRUE,
	Classe_id VARCHAR(15) NOT NULL,
	PRIMARY KEY (id),
    FOREIGN KEY (Classe_id) REFERENCES Classe(id)

);
-- 
CREATE TABLE Identite(
	NoCarte VARCHAR(15) DEFAULT NULL,
    id VARCHAR(20),
    Nom VARCHAR(50) NOT NULL,
    Prenom VARCHAR (50) NOT NULL,
    Classe_id VARCHAR(15) NOT NULL,
	Statut VARCHAR(20) DEFAULT NULL CHECK(Statut IN('ADMIN', NULL)),
	Casier_id INT DEFAULT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (Classe_id) REFERENCES Classe(id),
	FOREIGN KEY (Casier_id) REFERENCES Casier(id)
);
--
-- ---------------------------------------------------------------------------------------------------------------------------
-- -------------------------------------------- || Insertion données || ------------------------------------------------------
-- ---------------------------------------------------------------------------------------------------------------------------
--
INSERT INTO Classe VALUES ('Bleu', 'Seconde Bac Pro TMA'),
						('Vert', 'Première Bac Pro TMA'),
                        ('Rouge', 'Terminale Bac Pro TMA'),
						('Jaune', 'Première CAP MF'),
                        ('Orange', 'Terminale CAP MF'),
						('Or', 'Professeur');
--
INSERT INTO Identite(NoCarte, Nom, Prenom, Classe_id, Statut, id) VALUES
							('12.153.12.2', 'BEAUDOUIN', 'Corentin', 'Or', 'ADMIN', 'BEAUDOUIN1'),
							('170.1.62.61', 'MENNINGER', 'Jason', 'Jaune', NULL, 'MENNINGER1'),
							('64.105.61.61', 'ZELL', 'Renaud', 'Vert', NULL, 'ZELL1'),
							('4.232.61.61', 'TIJOU', 'Allan', 'Jaune', NULL, 'TIJOU1'),
							('15.55.62.61', 'VIARDOT', 'Thibault', 'Vert', NULL, 'VIARDOT1'),
							('142.62.61.61', 'AGOZZINO', 'Anthony', 'Bleu', NULL, 'AGOZZINO1');
-- 
INSERT INTO Casier(id, Classe_id) VALUES (1, 'Vert'), (2, 'Bleu'),
                                         (3, 'Rouge'), (4, 'Jaune'),
                                         (5, 'Orange');
--
-- -------------------------------------- || 2 select pour verifier les données des 2 tables || ------------------------------
-- 
SELECT * FROM Classe ORDER BY Libelle;
SELECT * FROM Identite ORDER BY Nom;
SELECT * FROM Casier ORDER BY id;
--
-- ---------------------------------------------------------------------------------------------------------------------------
-- -------------------------------------------------- || FIN DES Création || -------------------------------------------------
-- ---------------------------------------------------------------------------------------------------------------------------