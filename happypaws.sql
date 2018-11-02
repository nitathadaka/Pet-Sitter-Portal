-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: happypaws
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `aname` varchar(20) DEFAULT NULL,
  `apass` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('lenix','lenix');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logins`
--

DROP TABLE IF EXISTS `logins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `logins` (
  `uid` int(5) NOT NULL AUTO_INCREMENT,
  `umail` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logins`
--

LOCK TABLES `logins` WRITE;
/*!40000 ALTER TABLE `logins` DISABLE KEYS */;
INSERT INTO `logins` VALUES (3,'suyog ','suyog'),(9,'pratik','qweqwe'),(10,'testing@gmail.com','yup'),(11,'bhimam@gmail.com','bhima'),(12,'nitikas@gmail.com','nikita'),(13,'pramodd@gmail.com','pramod'),(14,'amitabhs@gmail.com','amitabh'),(15,'testee','testt'),(16,'mayur@gmail.com','mayur'),(17,'testing@test','test'),(18,'lenix@gmail.com','lenix'),(19,'protonics69','qweqwe'),(20,'test','test'),(21,'sdfghjk','sdfghjkl'),(22,'test555','test'),(23,'test8484','test'),(24,'tanmay@test','tanmay'),(25,'lelelelele','2f'),(26,'te33','qwe'),(27,'test@gmail.com','test'),(28,'suyog@test.com','suyog'),(29,'test123@gmail.com','12345'),(32,'nita@gmail.com','nita'),(33,'tanmay@gmail.com','tanmay'),(34,'test55@test.com','test'),(35,'test@test','test'),(36,'testing@again','test'),(37,'zahirbose@gmail.com','xahir'),(38,'suyog@suyog.com','suyog'),(39,'nita@nita.com','nita');
/*!40000 ALTER TABLE `logins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pets`
--

DROP TABLE IF EXISTS `pets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pets` (
  `pid` int(5) NOT NULL AUTO_INCREMENT,
  `pname` varchar(20) DEFAULT NULL,
  `category` varchar(10) DEFAULT NULL,
  `breed` varchar(20) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `descrip` varchar(45) DEFAULT NULL,
  `image` varchar(20) DEFAULT NULL,
  `uid` int(5) DEFAULT NULL,
  PRIMARY KEY (`pid`),
  KEY `uid` (`uid`),
  CONSTRAINT `pets_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `logins` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pets`
--

LOCK TABLES `pets` WRITE;
/*!40000 ALTER TABLE `pets` DISABLE KEYS */;
INSERT INTO `pets` VALUES (4,'testinging','Dog','Bruno',4,'qweqweqwe','test.jpg',9),(5,'chchu','Dog','chch',6,'this is epic!','test.jpg',3),(6,'test','asdfg','zxcvbn',5,'asdfghj','test.png',10),(7,'Molly','Cat','Abyssinian',2,'Molly loves to play.','1.png',11),(8,'Max','Dog','Ausralian',4,'Max is well mannered','2.png',11),(9,'Charlie','Dog','Beagle',1,'Charlie is very epic','3.png',12),(10,'Cooper','Dog','Border Collie',5,'Cooper loves to play','4.png',13),(11,'Tigger','Cat','american shortband',3,'Tigger is Royal','3.png',14),(12,'Test','test','test',4,'test','22.png',18),(13,'testagain','Dog','Husky',4,'epic','test.jpg',19),(14,'bruno','Dog','Pug',12,'Cool','21.png',29),(15,'Breezy','Cat','Test',123,'Epic','22.png',29),(16,'Snoopy','Dog','Labrador',5,'Fun','17.png',29),(17,'Luna','Dog','spitz',15,'short and sweet','15.png',37),(18,'Chewy','Dog','Poodle',3,'Small and Naughty','20.png',37),(19,'Tanmay','Dog','Pug',3,'Naughty and Loud','21.png',38),(20,'NIno','Cat','xyz',4,'Hello World','20.png',38),(21,'lilo','Cat','abc',2,'Sweet','11.png',38);
/*!40000 ALTER TABLE `pets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sitters`
--

DROP TABLE IF EXISTS `sitters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sitters` (
  `sid` int(5) NOT NULL AUTO_INCREMENT,
  `sname` varchar(20) DEFAULT NULL,
  `Location` varchar(10) DEFAULT NULL,
  `Addr` varchar(30) DEFAULT NULL,
  `phno` varchar(11) DEFAULT NULL,
  `image` varchar(10) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `smail` varchar(20) DEFAULT NULL,
  `uid` int(5) DEFAULT NULL,
  `available` varchar(1) DEFAULT 'Y',
  `prof` varchar(10) DEFAULT 'Owner',
  `charges` int(5) DEFAULT NULL,
  PRIMARY KEY (`sid`),
  KEY `uid` (`uid`),
  CONSTRAINT `sitters_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `logins` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sitters`
--

LOCK TABLES `sitters` WRITE;
/*!40000 ALTER TABLE `sitters` DISABLE KEYS */;
INSERT INTO `sitters` VALUES (17,'Bhima','Delhi','near','7894561235','20.png','I love dogs','bhimam@gmail.com',11,'N','Sitter',NULL),(19,'Nitika','Delhi','Camp','123456789','33.png','Dogs are my friend','nitikas@gmail.com',12,'N','Owner',NULL),(21,'testtse','testsete','steststse','rersreste','23.png','tsetser','testing@test',17,'Y','Owner',NULL),(22,'pratik','Kolhapur','JMRoad','789456123','29.png','infinite','pratik',9,'Y','Owner',NULL),(23,'lenix','Pune','Kalyani Nagar','123456789','22.png','Test','lenix@gmail.com',18,'Y','Sitter',240),(24,'t','t','testee','123','23.png','t','protonics69',19,'N','Sitter',NULL),(25,'qwe','qwe','qwe','qwe','16.png','qwe','te33',26,'Y','Owner',NULL),(26,'tet','Pune','Fatima','7894561235','23.png','Go Go ','suyog@test.com',28,'Y','Sitter',NULL),(34,'suyog','Pune','Fatima Nagar,Pune','1234567891','21.png','Cats','test123@gmail.com',29,'Y','Owner',NULL),(35,'Nita','Delhi','abcdefgh','9876543212','32.png','Dogs','nita@gmail.com',32,'Y','Sitter',NULL),(36,'Tanmay','Delhi','43,BharatGunj','234556456','14.png','Testing images ','tanmay@gmail.com',33,'Y','Sitter',NULL),(37,'testcharges','Pune','Near','123123','21.png','Cats','test@test',35,'Y','Sitter',600),(38,'testee','Pune','asdadsadasdasdad','asd','21.png','asd','testing@again',36,'Y','Sitter',600),(39,'Pramod Devarukhar','Nagpur','42,Subhash Chowk','9955664455','3.jpg','Animals bring peace to the society','pramodd@gmail.com',13,'Y','Sitter',600),(40,'Zahir Bose','Kolkata','RehmanGarh','7766552244','11.png','I love animals as Family','zahirbose@gmail.com',37,'Y','Owner',580),(41,'Suyog','Kolkata','Near GrandPool','7531594682','35.jpg','I like pets','suyog@suyog.com',38,'Y','Owner',250);
/*!40000 ALTER TABLE `sitters` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test` (
  `starttime` varchar(20) DEFAULT NULL,
  `endtime` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test`
--

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
INSERT INTO `test` VALUES ('10/09/2018','10/09/2018'),('0','5210'),('0','5210');
/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transaction` (
  `ownerid` int(5) DEFAULT NULL,
  `sitterid` int(5) DEFAULT NULL,
  `petid` int(5) DEFAULT NULL,
  `status` varchar(10) DEFAULT 'Pending',
  `tid` int(5) NOT NULL AUTO_INCREMENT,
  `startdate` varchar(10) DEFAULT NULL,
  `enddate` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`tid`),
  KEY `ownerid` (`ownerid`),
  KEY `sitterid` (`sitterid`),
  KEY `petid` (`petid`),
  CONSTRAINT `transaction_ibfk_1` FOREIGN KEY (`ownerid`) REFERENCES `logins` (`uid`),
  CONSTRAINT `transaction_ibfk_2` FOREIGN KEY (`ownerid`) REFERENCES `sitters` (`sid`),
  CONSTRAINT `transaction_ibfk_3` FOREIGN KEY (`ownerid`) REFERENCES `pets` (`pid`),
  CONSTRAINT `transaction_ibfk_4` FOREIGN KEY (`ownerid`) REFERENCES `logins` (`uid`),
  CONSTRAINT `transaction_ibfk_5` FOREIGN KEY (`sitterid`) REFERENCES `sitters` (`sid`),
  CONSTRAINT `transaction_ibfk_6` FOREIGN KEY (`petid`) REFERENCES `pets` (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction`
--

LOCK TABLES `transaction` WRITE;
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transactions` (
  `ownerid` int(5) DEFAULT NULL,
  `sitterid` int(5) DEFAULT NULL,
  `petid` int(5) DEFAULT NULL,
  `status` varchar(10) DEFAULT 'unknown',
  `tid` int(5) NOT NULL AUTO_INCREMENT,
  `startdate` varchar(12) DEFAULT NULL,
  `enddate` varchar(12) DEFAULT NULL,
  `totaldue` int(5) DEFAULT NULL,
  PRIMARY KEY (`tid`),
  KEY `ownerid` (`ownerid`),
  KEY `sitterid` (`sitterid`),
  KEY `petid` (`petid`),
  CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`ownerid`) REFERENCES `logins` (`uid`),
  CONSTRAINT `transactions_ibfk_2` FOREIGN KEY (`sitterid`) REFERENCES `sitters` (`sid`),
  CONSTRAINT `transactions_ibfk_3` FOREIGN KEY (`petid`) REFERENCES `pets` (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
INSERT INTO `transactions` VALUES (37,39,17,'Cancelled',65,'10/16/2018','10/23/2018',4200),(37,23,17,'Cancelled',66,'10/16/2018','10/24/2018',1920),(37,39,17,'Paid',67,'10/16/2018','10/18/2018',1200),(37,23,18,'Accepted',68,'10/16/2018','10/18/2018',480),(38,23,20,'Cancelled',69,'10/17/2018','10/22/2018',1200),(38,38,20,'Cancelled',70,'10/17/2018','10/22/2018',3000),(38,23,21,'Paid',71,'10/17/2018','10/17/2018',0),(38,23,21,'Cancelled',72,'10/17/2018','10/17/2018',0),(38,23,19,'Cancelled',73,'10/17/2018','10/24/2018',1680),(38,23,20,'Cancelled',74,'10/17/2018','10/23/2018',1440),(38,23,19,'Paid',75,'10/17/2018','10/24/2018',1680),(38,39,20,'Paid',76,'10/17/2018','10/17/2018',0),(38,23,20,'Cancelled',77,'10/17/2018','10/22/2018',1200),(38,38,20,'request',78,'10/17/2018','10/20/2018',1800);
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-17 12:37:45
