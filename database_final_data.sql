-- Creating Database Information

-- CREATE DATABASE cs340_db;

--
-- Access The DATABASE
--
-- USE cs_340_db;
-- source scratch.sql
--
-- Build Tables in DATABASE
--

--
-- Employee Table
--

DROP TABLE IF EXISTS `employee`;

CREATE TABLE `employee` (
	`employee_id` int(11) NOT NULL AUTO_INCREMENT,
	`first_name` varchar(255) NOT NULL,
	`last_name` varchar(255) NOT NULL,
	`employment_start_date` date NOT NULL,
	`employment_end_date` date DEFAULT NULL,
	`title` varchar(255) NOT NULL,
	`salary` float NOT NULL,
	PRIMARY KEY(`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;


--
-- Jet Data TABLE
-- 

DROP TABLE IF EXISTS `jet_data`;

CREATE TABLE `jet_data` (
	`jet_id` int(11) NOT NULL AUTO_INCREMENT,
	`derivative_id` int(11) NOT NULL,
	`num_engine` int(11) NOT NULL,
	`flight_cycle` int(11) NOT NULL,
	`market_value` int(11) NOT NULL,
	`payload` int(11) NOT NULL,
	PRIMARY KEY(`jet_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;


--
-- Derivative Data TABLE
--

DROP TABLE IF EXISTS `derivative_data`;

CREATE TABLE `derivative_data` (
	`derivative_id` int(11) NOT NULL AUTO_INCREMENT,
	`model_derivative` varchar(255) NOT NULL,
	`body_style` varchar(255) NOT NULL, 
	`primary_use` varchar(255) NOT NULL,
	`flight_range` int(11) NOT NULL,
	`max_seating` int(11) NOT NULL,
	`fuel_efficiency` float NOT NULL,
	`max_take_off_weight` float NOT NULL,
	PRIMARY KEY(`derivative_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;


--
-- Customers TABLE
--

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
	`customer_id` int(11) NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	`contact_num` varchar(255) NOT NULL,
	`address` varchar(255) NOT NULL,
	PRIMARY KEY(`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;


--
-- Lease Requests TABLE
--

DROP TABLE IF EXISTS `lease_request`;

CREATE TABLE `lease_request` (
	`request_id` int(11) NOT NULL AUTO_INCREMENT,
	`customer_id` int(11) NOT NULL, 
	`derivative_id` int(11) NOT NULL,
	`need_ground_staff` boolean NOT NULL,
	`need_crew` boolean NOT NULL,
	PRIMARY KEY(`request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Active Leases TABLE
--

DROP TABLE IF EXISTS `lease`;

CREATE TABLE `lease` (
	`lease_id` int(11) NOT NULL AUTO_INCREMENT,
	`customer_id` int(11) NOT NULL,
	`jet_id` int(11) NOT NULL,
	`lease_status` varchar(255) NOT NULL,
	`start_date` date NOT NULL,
	`end_date` date NOT NULL,
	`duration` int(11) DEFAULT NULL,
	`ground_staff_included` boolean NOT NULL,
	`crew_included` boolean NOT NULL,
	`lease_value` int(11) NOT NULL,
	`payment_to_date` boolean NOT NULL,
	`payment_remaining` int(11) NOT NULL,
	 PRIMARY KEY(`lease_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Aircraft Assignment Table 
--
DROP TABLE IF EXISTS `aircraft_assignment`;

CREATE TABLE `aircraft_assignment` (
	`lease_id` int(11) NOT NULL,
	`employee_id` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- *** --

-- Alter Table To Establish Foreign Keys

ALTER TABLE jet_data
ADD CONSTRAINT fk_jd_1
FOREIGN KEY (derivative_id)
REFERENCES derivative_data(derivative_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE lease
ADD CONSTRAINT fk_lease_1
FOREIGN KEY (customer_id)
REFERENCES customer(customer_id)
ON DELETE CASCADE
ON UPDATE CASCADE,

ADD CONSTRAINT fk_lease_2
FOREIGN KEY (jet_id)
REFERENCES jet_data(jet_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE lease_request
ADD CONSTRAINT fk_lr_1
FOREIGN KEY (customer_id)
REFERENCES customer(customer_id)
ON DELETE CASCADE
ON UPDATE CASCADE,

ADD CONSTRAINT fk_lr_2
FOREIGN KEY (derivative_id)
REFERENCES derivative_data(derivative_id)
ON DELETE CASCADE
ON UPDATE CASCADE;



-- *** -- 
-- Start Data DUMP

--
-- Dump info Into Employees
--

LOCK TABLES `employee` WRITE;
INSERT INTO `employee` VALUES (1,'Kyle','Creek','2014-05-04',NULL,'Junior Lease Agent',100000), (2,'Chris','Dela Pena','2012-01-01',NULL,'Legal',150000), (3,'Donald','Duck','1996-04-07','2021-03-21','Regional Supervisor',250000), (4,'Brett','Lewis','2001-08-12',NULL,'CEO',1500000);
UNLOCK TABLES;

--
-- Dump info into Jet Data'
--

LOCK TABLES `jet_data` WRITE;
INSERT INTO `jet_data` VALUES (1,2,2,1000,78900000,100), (2,3,2,200,54100000,200), (3,1,2,300,41200000,300), (4,4,2,400,39300000,400);
UNLOCK TABLES;

--
-- Dump Derivative Data
--

LOCK TABLES `derivative_data` WRITE;
INSERT INTO `derivative_data` VALUES (1,'737 Max 8','narrow-body','passenger',3550,175,110,181200), (2, '747-8','wide-body','freighter',9320,0,89,987000), (3,'787-8','wide-body','passenger',7305,300,104,502500), (4,'A320Neo','narrow-body','passenger',3401,186,97,169756);
UNLOCK TABLES;

--
-- Dump Customer 
--
LOCK TABLES `customer` WRITE;
INSERT INTO `customer` VALUES (1,'Southwest Air','800-533-1222','16215 Air Cargo Rd, SeTac, WA 98158'), (2,'Alaska Air','206-433-3200','19300 Intnl Blvd, SeaTac, WA 98188'), (3,'Spirit Airlines','954-447-7828','6542, 2800 Executive Way, Miramar FL, 33025'), (4,'Amazon Air','206-266-1000','410 Terry Ave N. Seattle, WA 98109');
UNLOCK TABLES;
