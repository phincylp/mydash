-- MySQL dump 10.13  Distrib 5.5.46, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: mysql_dashboard
-- ------------------------------------------------------
-- Server version	5.5.46-0+deb7u1

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
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inventory` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `dbhost` varchar(255) NOT NULL,
  `cluster_name` varchar(255) NOT NULL,
  `master_host` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT '1',
  `cluster_status` int(11) DEFAULT '1',
  `userpath` varchar(255) DEFAULT 'YES',
  `orderpath` varchar(255) DEFAULT 'NO',
  UNIQUE KEY `ID` (`ID`),
  UNIQUE KEY `dbhost` (`dbhost`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES (4,'flo-warehouse-b2b-db-2.nm.domain.com','flo-warehouse','None',1,1,'NO','YES'),(5,'flo-warehouse-b2b-db-10.nm.domain.com','flo-warehouse','flo-warehouse-b2b-db-2.nm.domain.com',1,1,'NO','YES'),(6,'flo-warehouse-b2b-db-12.nm.domain.com','flo-warehouse','flo-warehouse-b2b-db-2.nm.domain.com',1,1,'NO','YES'),(7,'flo-oms-db-5.nm.domain.com','flo-oms','None',1,1,'NO','YES'),(8,'flo-oms-db-24.nm.domain.com','flo-oms','flo-oms-db-5.nm.domain.com',1,1,'NO','YES'),(9,'10.32.113.185','none','None',1,1,'YES','NO'),(10,'10.32.165.80','fk-mp-pricing-console-mysql','None',1,1,'YES','NO'),(11,'10.84.184.70','sp-fa','None',1,1,'NO','YES'),(12,'flo-proc-db-1.nm.domain.com','g','None',1,1,'NO','YES'),(13,'scm-crm-db-1.nm.domain.com','CS Common Cluster','None',1,1,'NO','YES'),(14,'flo-acct-b2c-db1.nm.domain.com','flo-acct-b2c-db.nm.domain.com','None',1,1,'NO','YES'),(15,'10.32.157.15','fk-dfp-mysql-cluster','None',1,1,'YES','NO'),(16,'cs-titans-infra-db-master.nm.domain.com','cs-titans-infra-db','None',1,1,'NO','YES'),(17,'nlp-socialcs-mysql-master.nm.domain.com','nlp','None',1,1,'NO','YES'),(18,'mp-asl-next-db1.nm.domain.com','mp-asl-next-db1.nm.domain.com','None',1,1,'YES','NO'),(19,'spsrm-db-buzz-0001.nm.domain.com','spsrm-db-buzz-0001.nm.domain.com','None',1,1,'NO','YES'),(20,'10.33.89.8','qa-fdpanalytics-mysql-d','None',1,1,'YES','NO'),(21,'10.32.133.45','qa-fdpanalytics-badger-mysql-d','None',1,1,'YES','NO'),(22,'mp-asl-ui-db1.nm.domain.com','mp-asl-ui-db','None',1,1,'NO','YES'),(23,'scm-crm-db-master.nm.domain.com','scm-crm-db-cluster','None',1,1,'NO','YES'),(24,'10.33.101.98','prod-orchestrator-mysql-a-0001','None',1,1,'NO','YES'),(25,'10.32.145.169','prod-wallet','None',1,1,'YES','NO'),(26,'10.32.78.121','prod-wallet','10.32.145.169',1,1,'YES','NO'),(27,'cs-platform-mysql.nm.domain.com','cs-platform-mysql.nm.domain.com','None',1,1,'YES','NO'),(28,'retail-cpl-db1.nm.domain.com','retail-cpl','None',1,1,'YES','NO'),(29,'retail-cpl-db-1.nm.domain.com','retail-cpl','retail-cpl-db1.nm.domain.com',1,1,'YES','NO'),(30,'retail-cpl-db-2.nm.domain.com','retail-cpl','retail-cpl-db-1.nm.domain.com',1,1,'YES','NO'),(31,'retail-cpl-db-5.nm.domain.com','retail-cpl','retail-cpl-db-1.nm.domain.com',1,1,'YES','NO'),(32,'flo-warehouse-b2b-db-1.nm.domain.com','flo-warehouse','flo-warehouse-b2b-db-2.nm.domain.com',1,1,'YES','NO'),(33,'flo-warehouse-b2b-db-4.nm.domain.com','flo-warehouse','flo-warehouse-b2b-db-2.nm.domain.com',1,1,'YES','NO'),(34,'flo-warehouse-b2b-db-5.nm.domain.com','flo-warehouse','flo-warehouse-b2b-db-2.nm.domain.com',1,1,'YES','NO'),(35,'flo-warehouse-b2b-db-6.nm.domain.com','flo-warehouse','flo-warehouse-b2b-db-2.nm.domain.com',1,1,'YES','NO'),(36,'flo-warehouse-b2b-db-11.nm.domain.com','flo-warehouse','flo-warehouse-b2b-db-2.nm.domain.com',1,1,'YES','NO'),(37,'flo-warehouse-b2b-db-13.nm.domain.com','flo-warehouse','flo-warehouse-b2b-db-2.nm.domain.com',1,1,'YES','NO'),(38,'flo-warehouse-b2b-db-8.nm.domain.com','flo-warehouse','flo-warehouse-b2b-db-2.nm.domain.com',1,1,'YES','NO'),(39,'retail-cpl-db-4.nm.domain.com','retail-cpl','retail-cpl-db-1.nm.domain.com',1,1,'YES','NO'),(40,'retail-cpl-db-3.nm.domain.com','retail-cpl','retail-cpl-db-1.nm.domain.com',1,1,'YES','NO');
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-12-15 16:02:34
