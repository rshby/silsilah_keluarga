-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 09, 2022 at 08:01 AM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `keluarga`
--

-- --------------------------------------------------------

--
-- Table structure for table `keluarga`
--

CREATE TABLE `keluarga` (
  `id` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `jenis_kelamin` varchar(255) NOT NULL,
  `nama_ortu` varchar(255) DEFAULT NULL,
  `nama_kakek` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `keluarga`
--

INSERT INTO `keluarga` (`id`, `nama`, `jenis_kelamin`, `nama_ortu`, `nama_kakek`) VALUES
(1, 'Budi', 'Laki-Laki', NULL, NULL),
(2, 'Dedi', 'Laki-Laki', 'Budi', NULL),
(3, 'Dodi', 'Laki-Laki', 'Budi', NULL),
(4, 'Dede', 'Laki-Laki', 'Budi', NULL),
(5, 'Dewi', 'Perempuan', 'Budi', NULL),
(6, 'Feri', 'Laki-Laki', 'Dedi', 'Budi'),
(7, 'Farah', 'Perempuan', 'Dedi', 'Budi'),
(8, 'Gugus', 'Laki-Laki', 'Dodi', 'Budi'),
(9, 'Gandi', 'Laki-Laki', 'Dodi', 'Budi'),
(10, 'Hani', 'Perempuan', 'Dede', 'Budi'),
(11, 'Hana', 'Perempuan', 'Dede', 'Budi'),
(12, 'Reo', 'Laki-Laki', 'Dewi', 'Budi');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `keluarga`
--
ALTER TABLE `keluarga`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `keluarga`
--
ALTER TABLE `keluarga`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
