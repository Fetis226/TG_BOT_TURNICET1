-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: gaga
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log` (
  `idlog` int NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `entry_id` int NOT NULL DEFAULT '0',
  `Status` tinyint DEFAULT '0' COMMENT '1 - В учебном заведении, 0 - не в учебном заведении',
  PRIMARY KEY (`idlog`)
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--

LOCK TABLES `log` WRITE;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
INSERT INTO `log` VALUES (10,'2024-05-14 16:52:42',1,1),(14,'2024-05-14 16:54:27',1,0),(15,'2024-05-14 16:54:34',1,0),(16,'2024-05-14 17:00:38',1,0),(17,'2024-05-14 17:05:13',1,1),(18,'2024-05-14 17:05:20',1,1),(19,'2024-05-14 17:12:18',1,0),(20,'2024-05-14 17:12:29',1,0),(21,'2024-05-14 17:17:55',1,0),(22,'2024-05-14 17:21:22',1,0),(23,'2024-05-14 17:26:48',1,1),(24,'2024-05-14 17:26:58',1,0),(25,'2024-05-14 17:27:20',1,1),(26,'2024-05-14 17:28:14',3,1),(27,'2024-05-14 17:28:25',3,0),(28,'2024-05-14 17:28:36',3,1),(29,'2024-05-14 17:28:53',3,0),(30,'2024-05-14 17:29:13',1,0),(31,'2024-05-14 19:06:14',1,1),(32,'2024-05-14 19:06:26',1,0),(33,'2024-05-15 17:10:29',3,1),(34,'2024-05-15 17:10:57',6,1),(35,'2024-05-15 17:11:19',4,1),(36,'2024-05-15 17:11:44',1,1),(37,'2024-05-15 18:29:45',7,1),(38,'2024-05-15 19:12:57',3,0),(39,'2024-05-15 20:31:25',1,0),(40,'2024-05-15 20:31:59',1,1),(41,'2024-05-15 20:32:01',1,0),(42,'2024-05-15 20:34:24',3,1),(43,'2024-05-15 20:34:24',1,1),(44,'2024-05-15 20:41:10',1,0),(45,'2024-05-16 00:39:06',3,0),(46,'2024-05-16 00:56:31',3,1),(47,'2024-05-16 00:56:42',3,0),(48,'2024-05-16 01:05:05',3,1),(49,'2024-05-16 01:05:19',3,0),(50,'2024-05-16 14:24:48',1,1),(51,'2024-05-16 14:24:50',7,0),(52,'2024-05-16 14:24:51',6,0),(53,'2024-05-16 14:24:52',4,0),(54,'2024-05-16 14:24:53',3,1),(55,'2024-05-16 14:24:56',1,0),(56,'2024-05-16 14:29:55',1,1),(57,'2024-05-16 14:30:05',1,0),(58,'2024-05-16 14:30:06',3,0),(59,'2024-05-16 14:30:08',1,1),(60,'2024-05-16 14:30:10',1,0),(61,'2024-05-16 14:30:11',1,1),(62,'2024-05-16 14:31:12',1,0),(63,'2024-05-16 14:31:12',1,1),(64,'2024-05-16 14:31:13',1,0),(65,'2024-05-16 14:31:15',1,1),(66,'2024-05-16 14:31:15',1,0),(67,'2024-05-16 14:44:43',1,1),(68,'2024-05-16 14:44:43',1,0),(69,'2024-05-16 14:44:45',1,1),(70,'2024-05-16 14:44:46',1,0),(71,'2024-05-16 14:46:54',1,1),(72,'2024-05-16 14:47:01',1,0),(73,'2024-05-16 14:47:07',1,1),(74,'2024-05-16 14:47:09',1,0),(75,'2024-05-16 14:48:51',1,1),(76,'2024-05-16 14:48:52',1,0),(77,'2024-05-16 15:02:28',1,1),(78,'2024-05-16 15:02:29',1,0),(79,'2024-05-16 15:02:30',1,1),(80,'2024-05-16 15:07:02',1,0),(81,'2024-05-16 15:07:03',3,1),(82,'2024-05-16 15:07:04',1,1),(83,'2024-05-16 15:07:05',3,0),(84,'2024-05-16 15:08:33',1,0),(85,'2024-05-16 15:10:46',3,1),(86,'2024-05-16 15:10:47',3,0),(87,'2024-05-16 15:10:48',1,1),(88,'2024-05-16 15:10:48',1,0),(89,'2024-05-16 15:10:49',1,1),(90,'2024-05-16 15:10:50',3,1),(91,'2024-05-16 15:16:12',1,0),(92,'2024-05-16 15:17:13',3,0),(93,'2024-05-16 18:15:09',1,1),(94,'2024-05-16 19:18:46',1,0),(95,'2024-05-16 20:11:09',1,1),(96,'2024-05-16 20:11:10',1,0),(97,'2024-05-16 20:15:39',3,1),(98,'2024-05-16 20:35:38',1,1),(99,'2024-05-16 20:46:27',1,0),(100,'2024-05-16 20:47:25',3,0),(101,'2024-05-16 22:22:14',1,1),(102,'2024-05-16 22:22:41',1,0),(103,'2024-05-16 10:00:00',1,1),(104,'2024-05-16 10:02:00',1,0),(105,'2024-05-16 10:02:00',1,1),(106,'2024-05-16 10:02:00',1,0),(107,'2024-05-16 10:00:00',1,1),(108,'2024-05-16 10:02:00',1,0),(109,'2024-05-16 10:02:00',1,1),(110,'2024-05-16 10:02:00',1,0);
/*!40000 ALTER TABLE `log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `raspisanie_1`
--

DROP TABLE IF EXISTS `raspisanie_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `raspisanie_1` (
  `idrasp` int NOT NULL AUTO_INCREMENT,
  `Pon` int DEFAULT '0',
  `Vto` int DEFAULT '0',
  `Sre` int DEFAULT '0',
  `Che` int DEFAULT '0',
  `Pt` int DEFAULT '0',
  `sub` int DEFAULT '0',
  `group` int DEFAULT '0',
  UNIQUE KEY `idrasp_UNIQUE` (`idrasp`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `raspisanie_1`
--

LOCK TABLES `raspisanie_1` WRITE;
/*!40000 ALTER TABLE `raspisanie_1` DISABLE KEYS */;
INSERT INTO `raspisanie_1` VALUES (1,13451835,13451835,0,0,8201655,11401655,1),(2,13451515,10001515,0,0,8201310,8201655,2),(3,10001515,11401515,0,10001515,10001515,8201310,3);
/*!40000 ALTER TABLE `raspisanie_1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stud-par`
--

DROP TABLE IF EXISTS `stud-par`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stud-par` (
  `id` int NOT NULL AUTO_INCREMENT,
  `student_name` varchar(45) DEFAULT '0',
  `parent_id` int DEFAULT '0',
  `parent_name` varchar(45) DEFAULT '0',
  `code` varchar(45) DEFAULT '0',
  `Group` varchar(45) DEFAULT '0' COMMENT 'Группа',
  `group_id` int DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `code_UNIQUE` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stud-par`
--

LOCK TABLES `stud-par` WRITE;
/*!40000 ALTER TABLE `stud-par` DISABLE KEYS */;
INSERT INTO `stud-par` VALUES (1,'Ддвдв Дыдыд Тты',508777810,'Жвхкх Итрв Ьылвш','JKAS2','ИД 23.1/Б1-19',3),(3,'Жжыь Лу7шв Лвллв',794211640,'с с с','KAK1','ИД 23.2/Б1-19',2),(4,'Дыщщы Ьыьвь Щда',900264433,'KAJFA!','KAJFA!','ИД 23.1/Б2-19',3),(5,'Имбрагим Малимжон',0,'0','NEFOR!SD','0',0),(6,'Андрю Буаденос',860830119,'Бубес Дрэйк Хреновищ','askd!12d','ИД 23.1/Б2-19',3),(7,'Димчик',1289944129,'Ирпакот Клапат Нокич','ASKF!e34','ИД 23.1/Б1-19',1);
/*!40000 ALTER TABLE `stud-par` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-17  0:01:15
