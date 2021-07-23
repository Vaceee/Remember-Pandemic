CREATE DATABASE  IF NOT EXISTS `bbsdb` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bbsdb`;
-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: bbsdb
-- ------------------------------------------------------
-- Server version	8.0.17

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
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `usr_id` int(11) NOT NULL,
  `cls_id` int(11) NOT NULL,
  `adm_level` int(11) NOT NULL,
  PRIMARY KEY (`usr_id`,`cls_id`),
  KEY `fk_usr_class_classes_idx` (`cls_id`),
  KEY `fk_class_usr_users_idx` (`usr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base`
--

DROP TABLE IF EXISTS `base`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bas_name` varchar(60) NOT NULL,
  `bas_comment` varchar(150) DEFAULT NULL,
  `bas_forbidden` enum('Y','N') CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'N',
  `bas_postsCnt` int(11) NOT NULL,
  `bas_star` int(11) NOT NULL,
  `bas_clsec` enum('C','S') CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'C',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base`
--

LOCK TABLES `base` WRITE;
/*!40000 ALTER TABLE `base` DISABLE KEYS */;
INSERT INTO `base` VALUES (1,'疫情通告','通报和讨论有关疫情的最新消息','N',10,0,'S'),(2,'疫情日记','记录有关疫情的观察、反思和一切','N',3,0,'S'),(3,'抗疫行动','为疫情的抗击发出每个个体的声音','N',3,0,'S'),(4,'线上学习',NULL,'N',2,0,'C'),(5,'时间管理',NULL,'N',1,0,'C'),(6,'校园生活',NULL,'N',2,0,'C'),(7,'畅所欲言',NULL,'N',2,0,'C'),(8,'兴趣交流',NULL,'N',2,0,'C');
/*!40000 ALTER TABLE `base` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classes`
--

DROP TABLE IF EXISTS `classes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `classes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cls_name` varchar(20) NOT NULL,
  `cls_no` char(8) NOT NULL,
  `cls_grade` char(4) NOT NULL,
  `cls_term` char(11) NOT NULL,
  `cls_forbiden` enum('Y','N') CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'N',
  PRIMARY KEY (`id`),
  KEY `NO` (`cls_no`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classes`
--

LOCK TABLES `classes` WRITE;
/*!40000 ALTER TABLE `classes` DISABLE KEYS */;
INSERT INTO `classes` VALUES (1,'Prolang-C++','100384','2018','2018/2019/1','N'),(2,'DiscreteMath','100388','2019','2019/2020/1','N');
/*!40000 ALTER TABLE `classes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forbidip`
--

DROP TABLE IF EXISTS `forbidip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `forbidip` (
  `forbid_ip` varchar(15) NOT NULL,
  `forbid_loginCnt` int(11) NOT NULL,
  `forbid_time` int(11) NOT NULL,
  PRIMARY KEY (`forbid_ip`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forbidip`
--

LOCK TABLES `forbidip` WRITE;
/*!40000 ALTER TABLE `forbidip` DISABLE KEYS */;
INSERT INTO `forbidip` VALUES ('127.0.0.1',6,1592769978);
/*!40000 ALTER TABLE `forbidip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `images`
--

DROP TABLE IF EXISTS `images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `images` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `post_id` int(11) DEFAULT NULL,
  `rep_id` int(11) DEFAULT NULL,
  `img_path` text NOT NULL,
  `img_title` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_imgPath_post1_idx` (`post_id`),
  KEY `fk_imgPath_reply1_idx` (`rep_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `images`
--

LOCK TABLES `images` WRITE;
/*!40000 ALTER TABLE `images` DISABLE KEYS */;
/*!40000 ALTER TABLE `images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likes`
--

DROP TABLE IF EXISTS `likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `likes` (
  `rep_id` int(11) NOT NULL,
  `usr_id` int(11) NOT NULL,
  PRIMARY KEY (`rep_id`,`usr_id`),
  KEY `fk_like_reply1_idx` (`rep_id`),
  KEY `fk_like_users1_idx` (`usr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes`
--

LOCK TABLES `likes` WRITE;
/*!40000 ALTER TABLE `likes` DISABLE KEYS */;
INSERT INTO `likes` VALUES (12,8),(13,8);
/*!40000 ALTER TABLE `likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loginlogs`
--

DROP TABLE IF EXISTS `loginlogs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loginlogs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usr_id` int(11) NOT NULL,
  `login_ip` varchar(15) NOT NULL,
  `login_time` datetime NOT NULL,
  `login_site` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_table2_users1_idx` (`usr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loginlogs`
--

LOCK TABLES `loginlogs` WRITE;
/*!40000 ALTER TABLE `loginlogs` DISABLE KEYS */;
INSERT INTO `loginlogs` VALUES (1,1,'127.0.0.1','2020-02-20 04:31:00','SJBBS'),(2,1,'127.0.0.1','2020-02-20 04:31:11','SJBBS'),(3,1,'127.0.0.1','2020-02-20 04:46:24','SJBBS'),(4,1,'127.0.0.1','2020-02-20 04:47:52','SJBBS'),(5,1,'127.0.0.1','2020-02-20 04:50:55','SJBBS'),(6,1,'127.0.0.1','2020-02-20 04:54:05','SJBBS'),(7,1,'127.0.0.1','2020-02-20 04:58:13','SJBBS'),(8,1,'127.0.0.1','2020-02-23 15:05:21','SJBBS'),(9,1,'127.0.0.1','2020-02-23 15:08:17','SJBBS'),(10,1,'127.0.0.1','2020-02-24 01:24:08','SJBBS'),(11,1,'127.0.0.1','2020-02-24 02:15:51','SJBBS'),(12,1,'127.0.0.1','2020-02-24 02:22:29','SJBBS'),(13,1,'127.0.0.1','2020-02-24 02:24:43','SJBBS'),(14,1,'127.0.0.1','2020-02-24 02:25:35','SJBBS'),(15,1,'127.0.0.1','2020-02-24 02:26:10','SJBBS'),(16,1,'127.0.0.1','2020-02-24 02:29:27','SJBBS'),(17,1,'127.0.0.1','2020-02-24 02:32:02','SJBBS'),(18,1,'127.0.0.1','2020-02-24 02:34:16','SJBBS'),(19,1,'127.0.0.1','2020-02-25 14:37:12','SJBBS'),(20,1,'127.0.0.1','2020-02-25 14:41:54','SJBBS'),(21,1,'127.0.0.1','2020-02-25 14:42:19','SJBBS'),(22,1,'127.0.0.1','2020-02-25 14:43:38','SJBBS'),(23,1,'127.0.0.1','2020-02-25 14:50:35','SJBBS'),(24,1,'127.0.0.1','2020-02-25 14:59:47','SJBBS'),(25,1,'127.0.0.1','2020-02-25 15:00:10','SJBBS'),(26,1,'127.0.0.1','2020-02-25 15:00:14','SJBBS'),(27,1,'127.0.0.1','2020-02-25 15:01:06','SJBBS'),(28,1,'127.0.0.1','2020-02-25 15:01:13','SJBBS'),(29,1,'127.0.0.1','2020-02-25 15:01:19','SJBBS'),(30,1,'127.0.0.1','2020-02-25 15:01:38','SJBBS'),(31,1,'127.0.0.1','2020-02-25 15:02:07','SJBBS'),(32,1,'127.0.0.1','2020-02-25 15:02:17','SJBBS'),(33,1,'127.0.0.1','2020-02-25 15:02:27','SJBBS'),(34,1,'127.0.0.1','2020-02-25 15:02:32','SJBBS'),(35,1,'127.0.0.1','2020-02-25 15:08:44','SJBBS'),(36,1,'127.0.0.1','2020-02-25 15:10:23','SJBBS'),(37,1,'127.0.0.1','2020-02-25 15:45:10','SJBBS'),(38,1,'127.0.0.1','2020-02-25 15:45:15','SJBBS'),(39,1,'127.0.0.1','2020-02-25 15:56:58','SJBBS'),(40,1,'127.0.0.1','2020-02-25 15:57:04','SJBBS'),(41,1,'127.0.0.1','2020-02-25 15:57:10','SJBBS'),(42,1,'127.0.0.1','2020-02-25 15:57:29','SJBBS'),(43,1,'127.0.0.1','2020-02-25 15:57:59','SJBBS'),(44,1,'127.0.0.1','2020-02-25 15:58:09','SJBBS'),(45,1,'127.0.0.1','2020-02-25 15:58:19','SJBBS'),(46,1,'127.0.0.1','2020-02-25 15:58:24','SJBBS'),(47,1,'127.0.0.1','2020-02-26 04:12:03','SJBBS'),(48,1,'127.0.0.1','2020-02-26 22:02:04','SJBBS'),(49,1,'127.0.0.1','2020-02-26 22:05:33','SJBBS'),(50,1,'127.0.0.1','2020-02-26 22:18:28','SJBBS'),(51,1,'127.0.0.1','2020-02-26 22:33:14','SJBBS'),(52,1,'127.0.0.1','2020-02-26 22:52:13','SJBBS'),(53,1,'127.0.0.1','2020-02-26 23:24:19','SJBBS'),(54,1,'127.0.0.1','2020-06-22 00:40:09','SJBBS'),(55,1,'127.0.0.1','2020-06-22 00:49:59','SJBBS'),(56,1,'127.0.0.1','2020-06-22 00:50:08','SJBBS'),(57,1,'127.0.0.1','2020-06-22 00:50:12','SJBBS'),(58,1,'127.0.0.1','2020-06-22 00:59:53','SJBBS'),(59,1,'127.0.0.1','2020-06-22 01:25:26','SJBBS'),(60,1,'127.0.0.1','2020-06-22 01:32:48','SJBBS'),(61,1,'127.0.0.1','2020-06-22 04:08:59','SJBBS'),(62,1,'127.0.0.1','2020-06-23 01:20:53','SJBBS'),(63,1,'127.0.0.1','2020-06-25 22:28:03','SJBBS'),(64,3,'127.0.0.1','2020-06-26 00:28:46','SJBBS'),(65,5,'127.0.0.1','2020-06-26 00:59:24','SJBBS'),(66,5,'127.0.0.1','2020-06-26 02:00:15','SJBBS'),(67,3,'127.0.0.1','2020-06-26 03:39:21','SJBBS'),(68,5,'127.0.0.1','2020-06-26 03:39:47','SJBBS'),(69,5,'127.0.0.1','2020-06-26 03:43:20','SJBBS'),(70,3,'127.0.0.1','2020-06-26 03:51:53','SJBBS'),(71,5,'127.0.0.1','2020-06-26 05:02:15','SJBBS'),(72,5,'127.0.0.1','2020-06-26 05:02:43','SJBBS'),(73,5,'127.0.0.1','2020-06-26 05:02:54','SJBBS'),(74,5,'127.0.0.1','2020-06-26 05:11:22','SJBBS'),(75,7,'127.0.0.1','2020-06-26 07:17:26','SJBBS'),(76,8,'127.0.0.1','2020-06-26 07:31:24','SJBBS'),(77,8,'127.0.0.1','2020-06-26 07:31:44','SJBBS'),(78,8,'127.0.0.1','2020-06-26 07:31:45','SJBBS'),(79,8,'127.0.0.1','2020-06-26 07:31:45','SJBBS'),(80,8,'127.0.0.1','2020-06-26 07:31:45','SJBBS'),(81,9,'127.0.0.1','2020-06-26 07:37:51','SJBBS'),(82,1,'127.0.0.1','2020-06-26 08:25:34','SJBBS'),(83,12,'127.0.0.1','2020-06-26 08:33:22','SJBBS'),(84,11,'127.0.0.1','2020-06-26 21:36:28','SJBBS'),(85,8,'127.0.0.1','2020-06-26 22:25:13','SJBBS');
/*!40000 ALTER TABLE `loginlogs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usr_from` int(11) NOT NULL,
  `usr_to` int(11) NOT NULL,
  `msg_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `msg_content` text,
  PRIMARY KEY (`id`),
  KEY `fk_message_users1_idx` (`usr_from`),
  KEY `fk_message_users2_idx` (`usr_to`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,1,2,'2020-02-25 15:58:01','sjnb!');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notices`
--

DROP TABLE IF EXISTS `notices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bas_id` int(11) NOT NULL,
  `usr_from` int(11) NOT NULL,
  `ntc_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `ntc_content` text,
  `ntc_deleted` enum('Y','N') NOT NULL DEFAULT 'N',
  PRIMARY KEY (`id`),
  KEY `fk_notices_users_idx` (`usr_from`),
  KEY `fk_notices_base_idx` (`bas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notices`
--

LOCK TABLES `notices` WRITE;
/*!40000 ALTER TABLE `notices` DISABLE KEYS */;
/*!40000 ALTER TABLE `notices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post_tag`
--

DROP TABLE IF EXISTS `post_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post_tag` (
  `post_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`post_id`,`tag_id`),
  KEY `fk_post_tag_tags1_idx` (`tag_id`),
  KEY `fk_post_tag_posts1_idx` (`post_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post_tag`
--

LOCK TABLES `post_tag` WRITE;
/*!40000 ALTER TABLE `post_tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `post_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usr_id` int(11) NOT NULL,
  `post_title` varchar(255) NOT NULL,
  `post_content` text,
  `post_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `post_quoteFrom` int(11) DEFAULT NULL,
  `bas_id` int(11) NOT NULL,
  `post_mergedTo` int(11) DEFAULT NULL,
  `post_deleted` enum('Y','N') NOT NULL DEFAULT 'N',
  `post_onTop` enum('Y','N') NOT NULL DEFAULT 'N',
  `post_repCnt` int(11) NOT NULL DEFAULT '0',
  `post_clickCnt` int(11) NOT NULL DEFAULT '0',
  `post_lastRepTime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_posts_users1_idx` (`usr_id`),
  KEY `fk_post_column1_idx` (`bas_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES (1,1,'ljgnb!','lphnblphnbljgnb!','2020-02-25 15:01:25',NULL,2,NULL,'Y','N',-2,23,'2020-02-25 15:57:31'),(2,1,'lphnb!','lphnblphnblphnb!','2020-02-25 15:57:16',NULL,2,NULL,'Y','N',2,7,'2020-06-26 03:53:46'),(3,5,'我用OfCourse发的第一个帖子','我用OfCourse发的第一个帖子','2020-06-26 02:51:37',NULL,1,NULL,'Y','N',1,4,'2020-06-26 03:49:58'),(4,5,'我在记疫发的第一个帖子','我在*记疫*发的第`1`个<sub>帖子</sub>','2020-04-26 02:53:04',NULL,1,NULL,'N','N',2,21,'2020-04-26 03:26:54'),(5,6,'美国确诊人数已突破200万','抗议','2020-06-12 15:32:00',NULL,1,NULL,'N','N',8,133,'2020-06-26 22:34:28'),(6,7,'未来记载新冠病毒的配图','## 你会选择哪张照片？\r \r ![COVID-19](https://pic1.zhimg.com/80/v2-791df17df337110c52301a37f32e0b47_720w.jpg)\r ','2020-05-20 07:21:15',NULL,2,NULL,'N','N',12,96,'2020-06-26 22:18:05'),(7,8,'北京疫情复发！我们能做些什么','**面对疫情 做好日常预防**\n\n ◆ 勤洗手来多消毒，才能远离坏病毒；\n\n ◆ 出门就把口罩戴，利己利人大家好；\n\n ◆ 发热症状及早看，确保自己身体好；\n\n ◆ 多开窗多通风，保持室内空气好；\n\n ◆ 少出门少聚会，减少传染的机会。\n\n ◆ 出门就把口罩戴，利己利人大家好；\n','2020-06-13 13:35:32',NULL,3,NULL,'N','N',0,5,'2020-06-13 13:35:32'),(8,9,'欢迎加入Wuhan2020开源社区！','## Wuhan2020是什么？\r - - -\r 我们希望通过共同构建一个开源信息共享项目，帮助武汉自组织救援工作更有效、更准确地开展。我们当前在做的事是：建立一个医院、工厂、采购等信息实时同步的数据服务，同时召集所有希望对这次抗击病毒战役进行贡献的人，让每个具有相关技能的人都可以参与相关主题的开发工作，用开源的社区文化，以自组织协作的方式完成。\r \r ## 我可以做什么？\r - - -\r \r \r ### 提供资源及信息 \r 如果您希望提供有关医院、物流、酒店、生产、捐赠、义诊等援助信息，请移步项目线上web入口：[新型冠状病毒防疫信息平台](https://wh.opensource-service.cn/)\r \r ### 提供开发、翻译、新闻等技术支持\r 欢迎你加入Wuhan2020开发者的团队\r  1. 请先移步至[快速开始](https://wuhan2020.github.io/zh-cn/docs/dev/quickstart.html)查看基本协作流程、项目列表以及其他指南\r 2. 根据您的技能与兴趣加入我们的 [Slack 交流群组](https://join.slack.com/t/wuhan2020/shared_invite/enQtOTQxMTU4MzgyNTYwLWIxMTMyNWI4NWE2YTk3NGRjZGJhMjUzNmJhMjg1MDQ3OTEzNDE5NGY4MWFhMjRlYWU4MmE3ZGQyOGU4N2YwMzY)\r 3. 找到适合你的项目开始入手','2020-02-29 09:45:44',NULL,3,NULL,'Y','N',0,4,'2020-02-29 09:45:44'),(9,9,'欢迎加入Wuhan2020开源社区！','## Wuhan2020是什么？\n - - -\n 我们希望通过共同构建一个开源信息共享项目，帮助武汉自组织救援工作更有效、更准确地开展。我们当前在做的事是：建立一个医院、工厂、采购等信息实时同步的数据服务，同时召集所有希望对这次抗击病毒战役进行贡献的人，让每个具有相关技能的人都可以参与相关主题的开发工作，用开源的社区文化，以自组织协作的方式完成。\n\n## 我可以做什么？\n - - -\n\n### 提供资源及信息 \n 如果您希望提供有关医院、物流、酒店、生产、捐赠、义诊等援助信息，请移步项目线上web入口：[新型冠状病毒防疫信息平台](https://wh.opensource-service.cn/)\n \n### 提供开发、翻译、新闻等技术支持\n欢迎你加入Wuhan2020开发者的团队\n 1. 请先移步至[快速开始](https://wuhan2020.github.io/zh-cn/docs/dev/quickstart.html)查看基本协作流程、项目列表以及其他指南\n 2. 根据您的技能与兴趣加入我们的 [Slack 交流群组](https://join.slack.com/t/wuhan2020/shared_invite/enQtOTQxMTU4MzgyNTYwLWIxMTMyNWI4NWE2YTk3NGRjZGJhMjUzNmJhMjg1MDQ3OTEzNDE5NGY4MWFhMjRlYWU4MmE3ZGQyOGU4N2YwMzY)\n 3. 找到适合你的项目开始入手','2020-02-29 09:45:44',NULL,3,NULL,'N','N',0,1,'2020-02-29 09:45:44'),(10,8,'有对数据挖掘感兴趣的同学吗','我觉得`数据挖掘`是一门很实用的课程','2020-06-24 08:59:11',NULL,8,NULL,'N','N',2,4,'2020-06-26 22:02:26'),(11,12,'【世卫组织】全球新冠肺炎确诊病例超过941万例','根据世卫组织最新实时统计数据，截至欧洲中部夏令时间6月26日8时01分（北京时间6月26日14时01分），全球累计新冠肺炎确诊病例9413289例，累计死亡病例482730例。\n\n![图片1](http://p1.img.cctvpic.com/cportal/cnews-yz/img/2020/06/26/1593163654720_936_565x286.png)\n![图片2](http://p1.img.cctvpic.com/cportal/cnews-yz/img/2020/06/26/1593163662379_247_569x288.png)','2020-06-26 18:24:02',NULL,1,NULL,'N','N',0,1,'2020-06-26 18:24:02'),(12,12,'对于线上网课，你有哪些技巧分享？','线上学习给同学们带来便捷的同时，也有着不一而足的难处：**难以保持专注、形式感不强、内容相对零散**，你有哪些应对线上学习的好方法呢？','2020-06-26 21:28:25',NULL,4,NULL,'N','N',0,0,'2020-06-26 21:28:25'),(13,10,'期末的论文和大作业太多了吧','虽然很多课取消了考试，但都以大型作业和论文的形式代替，每天生产上万字的论文\n##真的头都要大了','2020-06-16 21:30:33',NULL,4,NULL,'N','N',3,14,'2020-06-26 21:30:33'),(14,11,'截至6月20日24时新型冠状病毒肺炎疫情最新情况','6月20日0—24时，31个省（自治区、直辖市）和新疆生产建设兵团报告新增确诊病例26例，其中境外输入病例1例（在福建），本土病例25例（北京22例，河北3例）；无新增死亡病例；新增疑似病例3例，均为本土病例（均在北京）。','2020-06-21 08:36:51',NULL,1,NULL,'N','N',0,0,'2020-06-21 08:36:51'),(15,11,'截至6月21日24时新型冠状病毒肺炎疫情最新情况','6月21日0—24时，31个省（自治区、直辖市）和新疆生产建设兵团报告新增确诊病例18例，其中境外输入病例7例（上海3例，陕西2例，天津1例，辽宁1例），本土病例11例（北京9例，河北2例）；无新增死亡病例；新增疑似病例2例，均为本土病例（均在北京）。\n\n当日无新增治愈出院病例，解除医学观察的密切接触者144人，重症病例与前一日相比减少3例。\n\n境外输入现有确诊病例89例（其中重症病例1例），无现有疑似病例。累计确诊病例1876例，累计治愈出院病例1787例，无死亡病例。','2020-06-22 08:36:51',NULL,1,NULL,'N','N',0,0,'2020-06-22 08:36:51'),(16,11,'截至6月22日24时新型冠状病毒肺炎疫情最新情况','6月22日0—24时，31个省（自治区、直辖市）和新疆生产建设兵团报告新增确诊病例22例，其中境外输入病例9例（甘肃7例，江苏1例，陕西1例），本土病例13例，均在北京；无新增死亡病例；新增疑似病例2例，均为本土病例（均在北京）。\n\n当日新增治愈出院病例12例，解除医学观察的密切接触者328人，重症病例与前一日相比增加1例。\n\n境外输入现有确诊病例87例（其中重症病例1例），无现有疑似病例。累计确诊病例1885例，累计治愈出院病例1798例，无死亡病例。','2020-06-23 08:36:51',NULL,1,NULL,'N','N',0,0,'2020-06-23 08:36:51'),(17,11,'截至6月23日24时新型冠状病毒肺炎疫情最新情况','6月23日0—24时，31个省（自治区、直辖市）和新疆生产建设兵团报告新增确诊病例12例，其中境外输入病例3例（上海2例，陕西1例），本土病例9例（北京7例，河北2例）；无新增死亡病例；新增疑似病例4例，均为本土病例（均在北京）。\n\n当日新增治愈出院病例3例，解除医学观察的密切接触者584人，重症病例与前一日相比减少1例。\n\n境外输入现有确诊病例87例（其中重症病例1例），无现有疑似病例。累计确诊病例1888例，累计治愈出院病例1801例，无死亡病例。','2020-06-24 08:36:51',NULL,1,NULL,'N','N',0,0,'2020-06-24 08:36:51'),(18,11,'截至6月24日24时新型冠状病毒肺炎疫情最新情况','6月24日0—24时，31个省（自治区、直辖市）和新疆生产建设兵团报告新增确诊病例19例，其中境外输入病例5例（甘肃3例，广东1例，陕西1例），本土病例14例（北京13例，河北1例）；无新增死亡病例；无新增疑似病例。\n\n当日新增治愈出院病例5例，解除医学观察的密切接触者415人，重症病例与前一日相比增加3例。\n\n境外输入现有确诊病例88例（其中重症病例1例），无现有疑似病例。累计确诊病例1893例，累计治愈出院病例1805例，无死亡病例。','2020-06-25 08:36:51',NULL,1,NULL,'N','N',0,0,'2020-06-25 08:36:51'),(19,11,'截至6月25日24时新型冠状病毒肺炎疫情最新情况','6月25日0—24时，31个省（自治区、直辖市）和新疆生产建设兵团报告新增确诊病例13例，其中境外输入病例2例（均在上海），本土病例11例（均在北京）；无新增死亡病例；新增疑似病例3例，均为本土病例（均在北京）。\n\n当日新增治愈出院病例6例，解除医学观察的密切接触者625人，重症病例与前一日相比减少7例。\n\n境外输入现有确诊病例84例（其中重症病例1例），无现有疑似病例。累计确诊病例1895例，累计治愈出院病例1811例，无死亡病例。','2020-06-26 08:36:51',NULL,1,NULL,'N','N',0,0,'2020-06-26 08:36:51'),(20,6,'想念西苑大排档的烤鱼了','深夜流口水','2020-04-26 23:44:44',NULL,6,NULL,'N','N',1,3,'2020-04-26 23:44:44'),(21,14,'还来不及和老师同学认真告别，就匆匆毕业了','“我的青春结束了。”','2020-06-06 21:05:39',NULL,6,NULL,'N','N',0,1,'2020-06-06 21:05:39'),(22,10,'大家在家都如何保持自主性呢','一个人学习真的好难\n\n![计算机组成原理](https://img-ph-mirror.nosdn.127.net/OIg_5Lpiuhv6EtrYRLuwNA==/6630887445793811434.png)','2020-04-01 13:51:49',NULL,5,NULL,'N','N',0,1,'2020-04-01 13:51:49'),(23,13,'疫情期间，你还会跟室友经常交流吗？','感觉大家彼此之间的 *联系* 都因为疫情而减弱了\n\n对应的是学习压力真的好大','2020-03-26 21:24:02',NULL,7,NULL,'N','N',0,2,'2020-03-26 21:24:02'),(24,17,'异地恋的同学是怎样度过疫情的？','好奇，想听你们分享故事八卦一下hhh','2020-04-10 15:55:54',NULL,7,NULL,'N','N',0,3,'2020-04-10 15:55:54'),(25,13,'分享我在疫情期间的新爱好','每天<sub>在家无聊</sub>之余，我参加了很多抗疫志愿组织和开源社区，感觉把自己的能力用在抗击疫情之中，既能贡献自己的力量，又能提高自己的技能，是一件很**有意义**的事~','2020-03-15 18:01:00',NULL,8,NULL,'N','N',0,1,'2020-03-15 18:01:00');
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `replies`
--

DROP TABLE IF EXISTS `replies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `replies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usr_id` int(11) NOT NULL,
  `post_id` int(11) NOT NULL,
  `rep_to` int(11) NOT NULL DEFAULT '-1',
  `rep_content` text NOT NULL,
  `rep_time` datetime NOT NULL,
  `rep_likeCnt` int(11) NOT NULL DEFAULT '0',
  `rep_repCnt` int(11) NOT NULL DEFAULT '0',
  `rep_deleted` enum('Y','N') NOT NULL DEFAULT 'N',
  PRIMARY KEY (`id`),
  KEY `fk_replies_users1_idx` (`usr_id`),
  KEY `fk_replies_posts1_idx` (`post_id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `replies`
--

LOCK TABLES `replies` WRITE;
/*!40000 ALTER TABLE `replies` DISABLE KEYS */;
INSERT INTO `replies` VALUES (1,1,1,-1,'yigeilo!','2020-02-25 15:57:49',2,2,'N'),(2,1,1,1,'您就是冬泳怪鸽？','2020-02-25 15:57:33',0,0,'N'),(3,1,1,-1,'eat mihotel','2020-02-25 15:57:35',0,0,'N'),(4,1,1,-1,'meizhierzhier','2020-02-25 15:57:37',0,0,'N'),(5,1,2,-1,'社会主义好','2020-02-25 15:57:40',0,0,'N'),(6,2,1,1,'爷‍又回来了','2020-06-22 15:57:40',0,0,'N'),(7,5,4,-1,'你好','2020-06-26 03:23:32',0,0,'N'),(8,5,4,-1,'我好','2020-06-26 03:26:54',0,0,'N'),(9,5,3,-1,'**好久不见呀**','2020-06-26 03:49:58',0,0,'N'),(10,3,2,-1,'**李培昊牛逼！** 回复也支持<sup>mark</sup><sub>down</sub>了\n> 不过需要手写','2020-06-26 03:53:46',0,0,'N'),(11,16,13,-1,'谁不是呢，抓紧时间吧，对我们文科生而言，起码比考试背书强一些','2020-06-26 21:31:16',0,0,'N'),(12,12,13,-1,'唉，其实也怪自己早些时候没有抓紧时间，都拖到最后才做','2020-06-26 21:31:43',2,0,'N'),(13,13,13,-1,'是啊，疫情期间真的好难','2020-06-26 21:32:04',1,0,'N'),(14,8,20,-1,'**我也是啊！！！** 还有学苑的蛋包饭','2020-06-26 21:47:08',0,0,'N'),(15,15,10,-1,'我觉得听起来很有意思！今年选这门课的人`好多`','2020-06-25 18:50:11',0,0,'N'),(16,8,10,-1,'好不容易才选到这门课233','2020-06-26 22:02:26',0,0,'N'),(17,1,6,-1,'感谢每一个平凡的中国人\n\n![1](https://pic2.zhimg.com/80/v2-019c2501350b006b4fd56911442862c2_720w.jpg)','2020-06-26 22:05:45',0,0,'N'),(18,2,6,-1,'国士无双\n\n![2](https://pic1.zhimg.com/80/v2-0179ba3aacad9ca05ac1f1b70f77ae84_720w.jpg)','2020-06-26 22:07:00',0,0,'N'),(19,3,6,-1,'封城之初的武汉\n\n![3](https://pic1.zhimg.com/80/v2-4fb5155b8243383225d18ddbc3bb2825_720w.jpg)','2020-06-26 22:07:25',0,0,'N'),(20,5,6,-1,'全民抗疫\n\n![4](https://pic4.zhimg.com/80/v2-8c40ba3ab838d4fe70b570c785d0d8c4_720w.jpg)','2020-06-26 22:08:05',0,0,'N'),(21,6,6,-1,'伟大的英雄\n\n![5](https://pic2.zhimg.com/80/v2-bd9a2cc313ace63075239bcab808e0e6_720w.jpg)','2020-06-26 22:08:45',0,0,'N'),(22,15,6,-1,'火神山建设的中国速度。我最喜欢的一张照片，也是`记疫`的注册界面背景\n\n![6](https://pic4.zhimg.com/80/v2-ab543d0e0a182de01e12b6be2efb935c_720w.jpg)','2020-06-26 22:10:31',0,0,'N'),(23,8,6,-1,'伟大的劳动人民\n\n![7](https://pic4.zhimg.com/80/v2-60b493d2c7b497f447f67435617ecc58_720w.jpg)','2020-06-26 22:14:42',0,0,'N'),(24,9,6,-1,'从来就没有什么救世主，也不靠神仙皇帝！\n要创造人类的幸福，全靠我们自己！\n\n![8](https://pic3.zhimg.com/80/v2-2340721b54ea5e4c4ed5d1246c9f23d5_720w.jpg)','2020-06-26 22:15:19',0,0,'N'),(25,10,6,-1,'3月初，在武汉战“疫”最艰难的时刻，一张落日余晖下，90后医生陪病床上八旬新冠肺炎患者王欣一起看夕阳。\n\n![9](https://pic2.zhimg.com/80/v2-dfea4a4ea3f22b64059c4ff9c6620887_720w.jpg)','2020-06-26 22:16:26',0,0,'N'),(26,14,6,-1,'![10](https://pic4.zhimg.com/80/v2-4858aa45238bb2704e68eae6407c57b1_720w.jpg)','2020-06-26 22:17:07',0,0,'N'),(27,12,6,-1,'![](https://pic1.zhimg.com/80/v2-4285c0597409bdab171672b66fa81500_720w.jpg)','2020-06-26 22:17:37',0,0,'N'),(28,7,6,-1,'来一些轻松的吧\n\n![](https://pic1.zhimg.com/80/v2-c5e5029bbfeae31e4fe3351b43f22ae3_720w.jpg)','2020-06-26 22:18:05',0,0,'N'),(29,8,5,-1,'**抗议**与**抗疫**齐飞 : )','2020-06-12 22:28:39',0,0,'N'),(30,9,5,-1,'美国政府的消极抗议政策真是祸及全国乃至全球','2020-06-13 08:29:36',0,0,'N'),(31,10,5,-1,'美国专家估测实际感染人数可能已超过2000万~','2020-06-13 12:31:08',0,0,'N'),(32,13,5,-1,'中国：疫情在我国已经不算热点话题了。\n\n美国：俺也一样！\n\n中国：我们很少关心疫情走向了。\n\n美国：俺也一样！\n\n中国：我国街上人声鼎沸。\n\n美国：俺也一样！','2020-06-14 22:32:04',0,0,'N'),(33,15,5,-1,'![](https://pic4.zhimg.com/80/v2-3e6c05ffaab1f7e93fcb75cec0430fca_720w.jpg)','2020-06-16 22:32:23',0,0,'N'),(34,17,5,-1,'美国CDC主任不是已经承认了早期不建议人们戴口罩是怕口罩不够用吗','2020-06-18 22:33:16',0,0,'N'),(35,14,5,-1,'美国检测出200万感染者，比第二到第六名的总和都多，巴西、俄罗斯、西班牙、英国、印度五个国家加起来，都没拼过一个美国。','2020-06-20 22:33:33',0,0,'N'),(36,2,5,-1,'2020年，真乃魔幻现实之年','2020-06-24 22:34:28',0,0,'N');
/*!40000 ALTER TABLE `replies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sessions`
--

DROP TABLE IF EXISTS `sessions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sessions` (
  `SJBBSID` char(32) NOT NULL,
  `usr_id` int(11) NOT NULL,
  `ss_expireTime` int(11) NOT NULL,
  PRIMARY KEY (`usr_id`),
  UNIQUE KEY `SJBBSID_UNIQUE` (`SJBBSID`),
  KEY `fk_cookies_users1_idx` (`usr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sessions`
--

LOCK TABLES `sessions` WRITE;
/*!40000 ALTER TABLE `sessions` DISABLE KEYS */;
/*!40000 ALTER TABLE `sessions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stu_class`
--

DROP TABLE IF EXISTS `stu_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stu_class` (
  `stu_id` int(11) NOT NULL,
  `cls_id` int(11) NOT NULL,
  PRIMARY KEY (`stu_id`,`cls_id`),
  KEY `fk_stu_class_classes1_idx` (`cls_id`),
  KEY `fk_class_stu_students1_idx` (`stu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stu_class`
--

LOCK TABLES `stu_class` WRITE;
/*!40000 ALTER TABLE `stu_class` DISABLE KEYS */;
INSERT INTO `stu_class` VALUES (1,1),(2,1),(1,2);
/*!40000 ALTER TABLE `stu_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tags`
--

DROP TABLE IF EXISTS `tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag_name` varchar(10) NOT NULL,
  `tag_cnt` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tag_name_UNIQUE` (`tag_name`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tags`
--

LOCK TABLES `tags` WRITE;
/*!40000 ALTER TABLE `tags` DISABLE KEYS */;
/*!40000 ALTER TABLE `tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usr_no` varchar(7) NOT NULL,
  `usr_password` varchar(64) NOT NULL,
  `usr_name` varchar(32) NOT NULL,
  `usr_grade` char(4) DEFAULT NULL,
  `usr_userlevel` int(11) NOT NULL DEFAULT '0',
  `usr_enabled` enum('Y','N') CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'Y',
  `usr_gender` enum('F','M') CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'M',
  PRIMARY KEY (`id`),
  KEY `NO` (`usr_no`),
  KEY `PASSWD` (`usr_password`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'1859999','5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8','test_user','2018',0,'Y','M'),(2,'1859998','5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8','god','2018',0,'Y','F'),(3,'1651579','47e81409bf634e78a640aef30f487089a4549d800973d93bf71e8fce60d573d2','1651579',NULL,0,'Y','F'),(5,'1759999','5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8','test_user',NULL,0,'Y','M'),(6,'2000000','a6d7b6ed262ed1cbf5bc4204491db65713a19c7acfda3d4f8c0c8c8ebd504291','Floyd',NULL,0,'Y','M'),(7,'1010101','938c2e85cbd732657ec8fbf93deb89cb4c73216630115bcb80552ce9bcf444b4','知乎',NULL,0,'Y','M'),(8,'1752066','920470d48cf946dd559a2b41578353f5d1ff6b75b951f50217f6e7f4d34f516e','吴子豪',NULL,0,'Y','M'),(9,'5202020','73a2af8864fc500fa49048bf3003776c19938f360e56bd03663866fb3087884a','wuhan2020',NULL,0,'Y','F'),(10,'1851579','079ad2fbf4e3edf3ea55d08b1a600cabc87852ed9144b49f402761442f8009cf','大二好难',NULL,0,'Y','M'),(11,'admin','8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918','系统管理员',NULL,1,'Y','M'),(12,'MAGA','a6d7b6ed262ed1cbf5bc4204491db65713a19c7acfda3d4f8c0c8c8ebd504291','MAGA！',NULL,0,'Y','F'),(13,'woaini','f72f3302519ee6484f54a7cbbbdf07e3f92543545a3d3174ee909b23807fdc1f','小孙同学',NULL,0,'Y','M'),(14,'1659999','de3dbef9594b2a022abf2f50eb03448c287cd848e06f51caeb08dae41c8dd56d','大四的老学长',NULL,0,'Y','M'),(15,'1750001','a56717cceb7c3fbb9554b2ec2a7fe9c9fce815eb0f38579aa83250adb5f39c07','追梦保研人',NULL,0,'Y','F'),(16,'1850566','49c266ce252623726a89613640b4a9615f6a43686cf57dc6646050b56186246d','nankemeng',NULL,0,'Y','F'),(17,'1752000','68bb7d970c8dc972d2e1b8128a0aeca29fb21197acef1dd3e282b03b6c4f702e','freeglove',NULL,0,'Y','F');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usr_class`
--

DROP TABLE IF EXISTS `usr_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usr_class` (
  `usr_id` int(11) NOT NULL,
  `cls_id` int(11) NOT NULL,
  PRIMARY KEY (`usr_id`,`cls_id`),
  KEY `fk_usr_class_classes1_idx` (`cls_id`),
  KEY `fk_class_usr_users1_idx` (`usr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usr_class`
--

LOCK TABLES `usr_class` WRITE;
/*!40000 ALTER TABLE `usr_class` DISABLE KEYS */;
/*!40000 ALTER TABLE `usr_class` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-26 23:04:07
