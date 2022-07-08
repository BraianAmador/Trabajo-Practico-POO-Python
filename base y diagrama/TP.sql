-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.18-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for tp1
CREATE DATABASE IF NOT EXISTS `tp1` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `tp1`;

-- Dumping structure for table tp1.administrador
CREATE TABLE IF NOT EXISTS `administrador` (
  `administrador_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL DEFAULT '0',
  `apellido` varchar(50) NOT NULL DEFAULT '0',
  `mail` varchar(100) NOT NULL,
  `interno` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`administrador_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table tp1.administrador: ~5 rows (approximately)
/*!40000 ALTER TABLE `administrador` DISABLE KEYS */;
INSERT INTO `administrador` (`administrador_id`, `nombre`, `apellido`, `mail`, `interno`, `password`) VALUES
	(7, 'Pepe', 'Alvarez', 'pepe@gmail.com', '486', 'UGVwZUAxMjM0\n'),
	(8, 'leo', 'gonzalez', 'leo@gmail.com', '777', 'TGVvMTIzNA==\n'),
	(13, 'Tito', 'Blanco', 'tito@gmail.com', '9996', 'VGl0b0AxMjM0\n'),
	(14, 'Braian', 'Amador', 'braian.amador@gmail.com', '777', 'QnJhaWFuQDEyMzQ=\n'),
	(15, 'gustavo', 'Salas', 'gustavo@gmail.com', '777', 'R3VzdGF2b0AxMjM0\n');
/*!40000 ALTER TABLE `administrador` ENABLE KEYS */;

-- Dumping structure for table tp1.asignaciones
CREATE TABLE IF NOT EXISTS `asignaciones` (
  `asignacion_id` int(11) NOT NULL AUTO_INCREMENT,
  `producto_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`asignacion_id`) USING BTREE,
  KEY `producto_id` (`producto_id`),
  KEY `usuario_id` (`usuario_id`)
) ENGINE=InnoDB AUTO_INCREMENT=584 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table tp1.asignaciones: ~21 rows (approximately)
/*!40000 ALTER TABLE `asignaciones` DISABLE KEYS */;
INSERT INTO `asignaciones` (`asignacion_id`, `producto_id`, `usuario_id`) VALUES
	(1, 1, 1),
	(2, 2, 2),
	(3, 3, 1),
	(4, 16, 9),
	(5, 18, 7),
	(6, 17, 10),
	(7, 4, 2),
	(8, 5, 5),
	(9, 6, 6),
	(10, 10, 3),
	(11, 19, 9),
	(12, 11, 4),
	(13, 7, 3),
	(14, 12, 8),
	(15, 13, 6),
	(16, 14, 7),
	(17, 8, 4),
	(18, 9, 5),
	(19, 15, 8),
	(20, 20, 10),
	(579, 17, 3);
/*!40000 ALTER TABLE `asignaciones` ENABLE KEYS */;

-- Dumping structure for procedure tp1.eliminarUsuario
DELIMITER //
CREATE PROCEDURE `eliminarUsuario`(idUsuario INT)
BEGIN
DELETE FROM usuarios WHERE usuario_id = idUsuario;
END//
DELIMITER ;

-- Dumping structure for table tp1.facturas
CREATE TABLE IF NOT EXISTS `facturas` (
  `factura_id` int(11) NOT NULL AUTO_INCREMENT,
  `numero` varchar(50) NOT NULL,
  `fechaDeCompra` date DEFAULT NULL,
  `proveedor_id` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`factura_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table tp1.facturas: ~17 rows (approximately)
/*!40000 ALTER TABLE `facturas` DISABLE KEYS */;
INSERT INTO `facturas` (`factura_id`, `numero`, `fechaDeCompra`, `proveedor_id`) VALUES
	(1, '0003-00000849', '2020-02-10', 1),
	(2, '0001-00000784', '2021-05-06', 2),
	(3, '0002-00000987', '2020-11-21', 3),
	(4, '0003-00000249', '2020-02-10', 4),
	(5, '0004-00000245', '2021-01-05', 5),
	(6, '0005-00000112', '2020-09-15', 6),
	(7, '0001-00000447', '2020-08-07', 7),
	(8, '0001-00000487', '2019-12-29', 8),
	(9, '0001-00000235', '2019-12-22', 9),
	(10, '0002-00000780', '2021-02-22', 10),
	(11, '0001-00000488', '2021-03-02', 6),
	(12, '0002-00000784', '2021-06-02', 7),
	(13, '0003-00000145', '2020-11-04', 8),
	(14, '0002-00000632', '2019-12-02', 9),
	(15, '0001-00000785', '2021-10-02', 10),
	(16, '0003-00002020', '2020-12-02', 2),
	(18, '001', '2022-08-11', 1);
/*!40000 ALTER TABLE `facturas` ENABLE KEYS */;

-- Dumping structure for view tp1.listaproductos
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `listaproductos` (
	`producto_id` INT(11) NOT NULL,
	`producto` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_general_ci',
	`marca` VARCHAR(50) NULL COLLATE 'utf8mb4_general_ci',
	`modelo` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_general_ci'
) ENGINE=MyISAM;

-- Dumping structure for view tp1.listausuarios
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `listausuarios` (
	`usuario_id` INT(11) NOT NULL,
	`Nombre y Apellido` VARCHAR(101) NULL COLLATE 'utf8mb4_general_ci',
	`telefono` VARCHAR(50) NULL COLLATE 'utf8mb4_general_ci',
	`Sector` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_general_ci'
) ENGINE=MyISAM;

-- Dumping structure for table tp1.marcas
CREATE TABLE IF NOT EXISTS `marcas` (
  `marca_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`marca_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table tp1.marcas: ~11 rows (approximately)
/*!40000 ALTER TABLE `marcas` DISABLE KEYS */;
INSERT INTO `marcas` (`marca_id`, `nombre`) VALUES
	(1, 'Grandstream'),
	(2, 'Dell'),
	(3, 'HP'),
	(4, 'Lenovo'),
	(5, 'Apple'),
	(6, 'Cisco'),
	(7, 'Asus'),
	(8, 'Yealink'),
	(9, 'Panasonic'),
	(10, 'Acer'),
	(11, 'LG');
/*!40000 ALTER TABLE `marcas` ENABLE KEYS */;

-- Dumping structure for procedure tp1.modificarTelefonoUsuario
DELIMITER //
CREATE PROCEDURE `modificarTelefonoUsuario`(IN nuevoTelefono VARCHAR(50), IN idUsuario INT)
BEGIN
UPDATE usuarios
SET telefono = nuevoTelefono
WHERE usuario_id = idUsuario;
END//
DELIMITER ;

-- Dumping structure for view tp1.preciotelefonos
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `preciotelefonos` (
	`modelo` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_general_ci',
	`precio` FLOAT NOT NULL,
	`marca` VARCHAR(50) NULL COLLATE 'utf8mb4_general_ci'
) ENGINE=MyISAM;

-- Dumping structure for table tp1.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `producto_id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) NOT NULL DEFAULT '0',
  `marca_id` int(11) NOT NULL DEFAULT 0,
  `modelo` varchar(50) NOT NULL DEFAULT '0',
  `precio` float NOT NULL DEFAULT 0,
  `factura_id` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`producto_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table tp1.productos: ~20 rows (approximately)
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` (`producto_id`, `descripcion`, `marca_id`, `modelo`, `precio`, `factura_id`) VALUES
	(1, 'Telefono', 1, 'GXP1610', 5796, 1),
	(2, 'Telefono', 1, 'GXP1610', 5796, 1),
	(3, 'Notebook', 2, 'Inspiron 3505', 139999, 3),
	(4, 'Notebook', 3, 'Pavilion x360 15-DQ1003LA', 120999, 3),
	(5, 'Impresora', 3, 'LaserJet 107a', 15600, 5),
	(6, 'Impresora', 3, 'Deskjet Ink Advantage 2375', 7899, 5),
	(7, 'Pc All In One', 4, 'F0ex0089ar', 150000, 6),
	(8, 'Pc All In One', 5, 'MHK03LE/A', 195229, 7),
	(9, 'Pc All In One', 5, 'MXWUL2E/A', 799999, 8),
	(10, 'Telefono', 6, 'CP 6921', 6300, 3),
	(11, 'Telefono', 6, 'CP 6921', 6300, 3),
	(12, 'Notebook', 4, 'Thinkpad E495', 85999, 9),
	(13, 'Notebook', 5, 'A2179', 154999, 2),
	(14, 'Notebook', 5, 'A2179', 154999, 2),
	(15, 'Telefono', 6, 'CP8845', 12913, 10),
	(16, 'Telefono', 8, 't21p', 6900, 11),
	(17, 'Telefono', 1, 'GXP1610', 5796, 12),
	(18, 'Telefono', 9, 'KX-HDV130', 9500, 13),
	(19, 'Pc All In One', 10, 'C24-963-UA91', 165000, 14),
	(20, 'Notebook', 7, 'X543MA', 72000, 15);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;

-- Dumping structure for view tp1.productosasignados
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `productosasignados` (
	`usuario_id` INT(11) NOT NULL,
	`Nombre y Apellido` VARCHAR(101) NULL COLLATE 'utf8mb4_general_ci',
	`producto_id` INT(11) NOT NULL,
	`Producto` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_general_ci'
) ENGINE=MyISAM;

-- Dumping structure for table tp1.proveedores
CREATE TABLE IF NOT EXISTS `proveedores` (
  `proveedor_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL DEFAULT '',
  `direccion` varchar(50) NOT NULL DEFAULT '',
  `telefono` varchar(50) NOT NULL DEFAULT '',
  `localidad` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`proveedor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table tp1.proveedores: ~11 rows (approximately)
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
INSERT INTO `proveedores` (`proveedor_id`, `nombre`, `direccion`, `telefono`, `localidad`) VALUES
	(1, 'sms', 'Paso 480', '4875-9658', 'CABA'),
	(2, 'Oportutek', 'Rodríguez Peña 825', '4785-0214', 'CABA'),
	(3, 'Mexx', 'Av. Juan Bautista Alberdi 1233', '4857-6698', 'CABA'),
	(4, 'bytecom', 'Crisólogo Larralde 818', '4627-7171', 'Moron'),
	(5, 'Computec', 'Castro Barros 650', '4241-7322', 'Burzaco'),
	(6, 'Computech', 'Av. Vélez Sarsfield 192', '2524-0010', 'La Matanza'),
	(7, 'Gigaflop', 'Paraná 223', '5252-2233', 'CABA'),
	(8, 'Pcenter', 'Ituzaingó 1542', '7398-2696', 'Lanus'),
	(9, 'HyperGAMING', 'Adolfo Alsina 1554', '4796-5607', 'Vicente Lopez'),
	(10, 'FsComputers', 'Bulnes 1783', '4824-6399', 'CABA'),
	(11, 'Sys', 'Mitre 222', '5588-9988', 'Moron');
/*!40000 ALTER TABLE `proveedores` ENABLE KEYS */;

-- Dumping structure for table tp1.sectores
CREATE TABLE IF NOT EXISTS `sectores` (
  `sector_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`sector_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table tp1.sectores: ~12 rows (approximately)
/*!40000 ALTER TABLE `sectores` DISABLE KEYS */;
INSERT INTO `sectores` (`sector_id`, `nombre`) VALUES
	(1, 'RRHH'),
	(2, 'Atencion al cliente'),
	(3, 'Auditoria'),
	(4, 'Facturacion'),
	(5, 'Administracion'),
	(6, 'Contabilidad'),
	(7, 'Desarrollo'),
	(8, 'Adm. de datos'),
	(9, 'Soporte tecnico'),
	(10, 'Tramites'),
	(11, 'Ventas'),
	(12, 'RRHH');
/*!40000 ALTER TABLE `sectores` ENABLE KEYS */;

-- Dumping structure for table tp1.tickets
CREATE TABLE IF NOT EXISTS `tickets` (
  `ticket_id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` text DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `prioridad` varchar(50) DEFAULT NULL,
  `estado` varchar(50) DEFAULT NULL,
  `administrador_id` int(11) DEFAULT 1000,
  PRIMARY KEY (`ticket_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1005 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table tp1.tickets: ~5 rows (approximately)
/*!40000 ALTER TABLE `tickets` DISABLE KEYS */;
INSERT INTO `tickets` (`ticket_id`, `titulo`, `descripcion`, `prioridad`, `estado`, `administrador_id`) VALUES
	(1000, 'Hola', 'Hola como estas?', '4', '4', 4),
	(1001, 'Ticket de Tito', 'Esto es un ticket generado por tito', '4', '4', 13),
	(1002, 'Hola!', 'Esto es un ticket de leo', '3', '1', 8),
	(1003, 'Hola', 'Este es un ticket generado por Braian.', '2', '2', 14),
	(1004, 'Hola2', 'Esto es una descripcion', '4', '2', 8);
/*!40000 ALTER TABLE `tickets` ENABLE KEYS */;

-- Dumping structure for table tp1.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `usuario_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(50) DEFAULT NULL,
  `telefono` varchar(50) DEFAULT NULL,
  `sector_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`usuario_id`),
  KEY `sector_id` (`sector_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table tp1.usuarios: ~17 rows (approximately)
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` (`usuario_id`, `nombre`, `apellido`, `telefono`, `sector_id`) VALUES
	(1, 'Braian', 'Amador', '1168826828', 1),
	(2, 'Esteban', 'Quito', '1162581578', 2),
	(3, 'Elsa', 'Capunta', '1122356897', 3),
	(4, 'Armando', 'Paredes', '1184526984', 4),
	(5, 'Luz', 'Rojas', '1158496230', 5),
	(6, 'Susana', 'Torio', '1148759235', 6),
	(7, 'Alan', 'Brito', '1196526157', 7),
	(8, 'German', 'Zana', '1148597215', 8),
	(9, 'Pedro', 'Alvarez', '1166528951', 9),
	(10, 'Jorge', 'Melo', '1168952414', 10),
	(16, 'Dario', 'Coria', '1125478963', 3),
	(17, 'Jose', 'Perez', '1155887755', 1),
	(18, 'Pablo', 'Mormol', '1144558877', 2),
	(19, 'Hector', 'Paso', '1144778855', 2),
	(20, 'Juan', 'Perez', '1544885522', 9),
	(21, 'Jose', 'Sosa', '1122005588', 4),
	(26, 'Juan', 'Gonzalez', '555555555', 2);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

-- Dumping structure for view tp1.listaproductos
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `listaproductos`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `listaproductos` AS SELECT productos.producto_id, productos.descripcion AS producto, marcas.nombre AS marca, productos.modelo FROM productos
INNER JOIN marcas ON productos.marca_id = marcas.marca_id ;

-- Dumping structure for view tp1.listausuarios
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `listausuarios`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `listausuarios` AS SELECT usuarios.usuario_id,concat(usuarios.nombre, SPACE(1), usuarios.apellido) AS 'Nombre y Apellido', usuarios.telefono, sectores.nombre AS Sector FROM usuarios
INNER JOIN sectores ON sectores.sector_id = usuarios.sector_id ;

-- Dumping structure for view tp1.preciotelefonos
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `preciotelefonos`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `preciotelefonos` AS SELECT DISTINCT productos.modelo, productos.precio, marcas.nombre AS marca FROM productos
INNER JOIN marcas ON productos.marca_id = marcas.marca_id
WHERE productos.descripcion = 'Telefono' ;

-- Dumping structure for view tp1.productosasignados
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `productosasignados`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `productosasignados` AS SELECT usuarios.usuario_id,concat(usuarios.nombre, SPACE(1), usuarios.apellido) AS 'Nombre y Apellido', productos.producto_id, productos.descripcion AS Producto FROM asignaciones
INNER JOIN usuarios ON asignaciones.usuario_id = usuarios.usuario_id
INNER JOIN productos ON asignaciones.producto_id = productos.producto_id ;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
