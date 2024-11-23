-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: tablas
-- ------------------------------------------------------
-- Server version	9.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `perros`
--

DROP TABLE IF EXISTS `perros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `perros` (
  `idperros` int NOT NULL AUTO_INCREMENT,
  `Nombre_Perro` varchar(45) NOT NULL,
  `Raza_Perro` varchar(45) NOT NULL,
  `Edad` int NOT NULL,
  `Peso` float DEFAULT NULL,
  `Id_Guarderia` int NOT NULL,
  `Id_Cuidador` int NOT NULL,
  PRIMARY KEY (`idperros`),
  KEY `Id_Guarderia_idx` (`Id_Guarderia`),
  KEY `Id_Cuidador_idx` (`Id_Cuidador`),
  CONSTRAINT `Id_Cuidador` FOREIGN KEY (`Id_Cuidador`) REFERENCES `cuidadores` (`idcuidador`),
  CONSTRAINT `Id_Guarderia` FOREIGN KEY (`Id_Guarderia`) REFERENCES `guarderias` (`idGuarderia`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perros`
--

LOCK TABLES `perros` WRITE;
/*!40000 ALTER TABLE `perros` DISABLE KEYS */;
INSERT INTO `perros` VALUES (1,'Max','Labrador',5,2.8,4,4),(2,'Bella','Beagle',3,12.5,4,1),(3,'Rocky','Bulldog',4,2,4,4),(4,'Luna','Poodle',2,8.2,4,4),(5,'Duke','Boxer',6,23.6,4,4),(6,'lassie lopez','Chihuahua',1,4.1,3,1),(7,'Simba','Golden',3,30.8,1,2),(8,'Nala','Pug',4,7.4,2,4),(9,'lassie el magnifico','Husky',5,2.5,3,4),(10,'Sasha','Schnauzer',4,2,2,4);
/*!40000 ALTER TABLE `perros` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-07 23:37:22
