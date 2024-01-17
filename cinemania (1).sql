-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 16, 2024 at 06:39 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cinemania`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer_details`
--

CREATE TABLE `customer_details` (
  `cus_name` varchar(50) NOT NULL,
  `cus_email` varchar(40) NOT NULL,
  `cus_phone_number` bigint(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer_details`
--

INSERT INTO `customer_details` (`cus_name`, `cus_email`, `cus_phone_number`) VALUES
('syazleen', 'aleen@gmail.com', 60178672536);

-- --------------------------------------------------------

--
-- Table structure for table `movie_info`
--

CREATE TABLE `movie_info` (
  `Title` varchar(30) NOT NULL,
  `Hall` varchar(30) NOT NULL,
  `Showtime` varchar(30) NOT NULL,
  `Seat` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `movie_info`
--

INSERT INTO `movie_info` (`Title`, `Hall`, `Showtime`, `Seat`) VALUES
('The Nun (Horror)', 'Family Session=RM30', '8PM - 10PM', '1F, 2F, 3F');

-- --------------------------------------------------------

--
-- Table structure for table `payment_info`
--

CREATE TABLE `payment_info` (
  `Method_of_Payment` varchar(30) NOT NULL,
  `card_number` bigint(16) NOT NULL,
  `expired_date` varchar(5) NOT NULL,
  `CVV_CVC` int(3) NOT NULL,
  `total_cost` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payment_info`
--

INSERT INTO `payment_info` (`Method_of_Payment`, `card_number`, `expired_date`, `CVV_CVC`, `total_cost`) VALUES
('Master Card', 1234567653787465, '07/23', 129, 90);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
