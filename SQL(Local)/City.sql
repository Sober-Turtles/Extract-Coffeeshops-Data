-- Database export via SQLPro (https://www.sqlprostudio.com/allapps.html)
-- Exported by dibaaminshahidi at 17-11-1401 10:32 PM.
-- WARNING: This file may contain descructive statements such as DROPs.
-- Please ensure that you are running the script at the proper location.


-- BEGIN TABLE City
DROP TABLE IF EXISTS City;
CREATE TABLE `City` (
  `id` int NOT NULL,
  `name` varchar(16) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Inserting 17 rows into City
-- Insert batch #1
INSERT INTO City (id, name) VALUES
(0, 'tabriz'),
(1, 'zanjan'),
(2, 'urmia'),
(3, 'hamedan'),
(4, 'isfahan'),
(5, 'kish'),
(6, 'kerman'),
(7, 'karaj'),
(8, 'bandarabbas'),
(9, 'sabzevar'),
(10, 'mashhad'),
(11, 'shiraz'),
(12, 'ghom'),
(13, 'ahwaz'),
(14, 'arak'),
(15, 'qazvin'),
(16, 'tehran');

-- END TABLE City

