-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 26, 2025 at 07:33 AM
-- Server version: 10.4.28-MariaDB-log
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_rekomendasi`
--

-- --------------------------------------------------------

--
-- Table structure for table `buku`
--

CREATE TABLE `buku` (
  `id` int(11) NOT NULL,
  `judul` varchar(255) DEFAULT NULL,
  `minat` varchar(100) DEFAULT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `author` varchar(150) DEFAULT NULL,
  `tahun_terbit` year(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `buku`
--

INSERT INTO `buku` (`id`, `judul`, `minat`, `image_url`, `author`, `tahun_terbit`) VALUES
(1, 'Clean Code', 'teknologi', 'https://marketplace.canva.com/EAFFDGFkcdM/1/0/1003w/canva-hijau-biru-sederhana-ruang-sunyi-sampul-buku-novel-K3WxwPzlPyk.jpg', 'Robert C. Martin', '2008'),
(2, 'The Pragmatic Programmer', 'teknologi', 'https://siplah-oss.tokoladang.co.id/merchant/12268/product/f1AAsq6jg0R24pEqVKoR8kklvHKCixK3MY5DLyp3.jpg', 'Andrew Hunt', '1999'),
(3, 'Harry Potter', 'fiksi', 'https://nnc-media.netralnews.com/IMG-Netral-News-User-10866-KC1JV2Y0AI.jpg', 'J.K. Rowling', '1997'),
(4, 'Sapiens', 'sejarah', 'https://i0.wp.com/agosbookstore.com/wp-content/uploads/2023/11/e4653435-72ff-49dc-a500-d105140c0664.png?fit=359%2C514&ssl=1\r\n', 'Yuval Noah Harari', '2011'),
(6, 'dasfadsf', 'adfadf', 'https://lh5.googleusercontent.com/proxy/l6Bz_Fvb7noo7Ksa-J9dXviEU3F5gs5HLjSR9FVkrzz6jsFICiPQPcFRgRpSKb5zl5OEoH7oXUfaSIqHFYEr4B52NWZolDmftBy8Pl0jTvLJny5d0Lp40kXoDQvg8LeFzzh4lpLSKpE84ROJ7LFiUI4OJncZVCk5xAkpJ-h9UzikrnBzttfvCbMLPA', 'adfadf', '2021');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `buku`
--
ALTER TABLE `buku`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `buku`
--
ALTER TABLE `buku`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
