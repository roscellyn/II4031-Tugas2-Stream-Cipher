-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: sistar_studiin
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `informasi_tutor`
--

DROP TABLE IF EXISTS `informasi_tutor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `informasi_tutor` (
  `id` int NOT NULL,
  `email` varchar(30) DEFAULT NULL,
  `nama` varchar(50) DEFAULT NULL,
  `no_telp` varchar(20) DEFAULT NULL,
  `jenis_kelamin` enum('Laki-laki','Perempuan') DEFAULT NULL,
  `status` enum('Verified','Not Verified') DEFAULT 'Not Verified',
  `tempat_lahir` varchar(20) DEFAULT NULL,
  `tanggal_lahir` date DEFAULT NULL,
  `pendidikan` varchar(10) DEFAULT NULL,
  `jurusan` varchar(20) DEFAULT NULL,
  `nama_univ` varchar(50) DEFAULT NULL,
  `GPA` float(3,2) DEFAULT NULL,
  `pengalaman_posisi` varchar(30) DEFAULT NULL,
  `pengalaman_tempat` varchar(30) DEFAULT NULL,
  `pengalaman_file` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_ID_EMAIL` (`id`,`email`),
  CONSTRAINT `informasi_tutor_ibfk_1` FOREIGN KEY (`id`, `email`) REFERENCES `user` (`id`, `email`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `informasi_tutor`
--

LOCK TABLES `informasi_tutor` WRITE;
/*!40000 ALTER TABLE `informasi_tutor` DISABLE KEYS */;
INSERT INTO `informasi_tutor` VALUES (6,'faisalkeren@gmail.com',NULL,NULL,NULL,'Not Verified',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `informasi_tutor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(30) NOT NULL,
  `password` varchar(20) DEFAULT NULL,
  `role` enum('admin','tutor') DEFAULT 'tutor',
  PRIMARY KEY (`id`,`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin@studiin.com','admin','admin'),(6,'faisalkeren@gmail.com','sikeren','tutor');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = cp850 */ ;
/*!50003 SET character_set_results = cp850 */ ;
/*!50003 SET collation_connection  = cp850_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `insert_id_email` AFTER INSERT ON `user` FOR EACH ROW INSERT INTO informasi_tutor(id,email)
SELECT id, email
FROM user
WHERE user.email = NEW.email */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-30 23:01:06
