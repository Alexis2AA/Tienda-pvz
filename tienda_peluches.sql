-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-12-2024 a las 18:55:44
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tienda_peluches`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `insertar` (IN `nombreproducto` VARCHAR(255), IN `precioproducto` INT, IN `imagenproducto` VARCHAR(255))   BEGIN
    INSERT INTO peluches (nombre, precio, imagen)
    VALUES (nombreproducto, precioproducto, imagenproducto);
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador`
--

CREATE TABLE `administrador` (
  `nombre` varchar(30) NOT NULL,
  `contraseña` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `administrador`
--

INSERT INTO `administrador` (`nombre`, `contraseña`) VALUES
('alexis', 'holamundo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `idcategoria` int(11) UNSIGNED NOT NULL,
  `nombre` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`idcategoria`, `nombre`) VALUES
(1, 'peluches'),
(2, 'figuras');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `peluches`
--

CREATE TABLE `peluches` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `precio` int(11) DEFAULT NULL,
  `imagen` varchar(255) DEFAULT NULL,
  `fkcategoria` int(11) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `peluches`
--

INSERT INTO `peluches` (`id`, `nombre`, `precio`, `imagen`, `fkcategoria`) VALUES
(1, 'Apisanoflor', 5000, 'static\\images/apisonaflor-de-peluche-plantas-vs-zombis.png', 1),
(2, 'Boomerang', 6000, 'static\\images/boomerang-plant-peluche-plantas-contra-zombies-2.png', 1),
(3, 'Faraon zombie', 7000, 'static\\images/faraon-zombie-plantas-vs-zombis-juguete-de-accion-figura.png', 2),
(4, 'Girasol Gigante', 5000, 'static\\images/girasol-gigante-de-peluche-plants-vs-zombies.png', 1),
(10, 'Jalapeno', 7000, 'static\\images/jalapeno-de-peluche-plants-vs-zombies.png', 1),
(11, 'Lanzamaiz', 5000, 'static\\images/juguete-de-peluche-lanzamaiz-plantas-vs-zombies.png', 1),
(12, 'DR Zombie', 8000, 'static\\images/juguete-dr-zomboss-de-plantas-vs-zombis.png', 2),
(13, 'Zombie Yeti', 7000, 'static\\images/juguete-yeti-de-plantas-vs-zombis.png', 2),
(14, 'Zombie Cono', 5000, 'static\\images/juguete-zombie-cono-de-plantas-vs-zombis.png', 2),
(15, 'Zombie Cubo', 5000, 'static\\images/juguete-zombie-cubo-de-plantas-vs-zombis.png', 2),
(16, 'Zombie Futbolista', 8000, 'static\\images/juguete-zombie-futbolista-de-plantas-vs-zombis.png', 2),
(17, 'Zombie Lector', 7000, 'static\\images/juguete-zombie-lector-de-plantas-vs-zombis.png', 2),
(18, 'Zombot Sphixinator', 6000, 'static\\images/juguete-zombot-sphinxinator-de-plantas-vs-zombis.png', 2),
(19, 'Zombie Zombit Submarino', 7000, 'static\\images/juguete-zombot-submarino-de-plantas-vs-zombis.png', 2),
(21, 'Lechuga De HIelo', 8000, 'static\\images/lechuga-iceberg-peluche-plantas-vs-zombies.png', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`idcategoria`);

--
-- Indices de la tabla `peluches`
--
ALTER TABLE `peluches`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fkcategoria` (`fkcategoria`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `peluches`
--
ALTER TABLE `peluches`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `peluches`
--
ALTER TABLE `peluches`
  ADD CONSTRAINT `peluches_ibfk_1` FOREIGN KEY (`fkcategoria`) REFERENCES `categoria` (`idcategoria`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
