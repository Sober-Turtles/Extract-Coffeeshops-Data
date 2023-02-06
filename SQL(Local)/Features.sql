-- Database export via SQLPro (https://www.sqlprostudio.com/allapps.html)
-- Exported by dibaaminshahidi at 17-11-1401 10:32 PM.
-- WARNING: This file may contain descructive statements such as DROPs.
-- Please ensure that you are running the script at the proper location.


-- BEGIN TABLE Features
DROP TABLE IF EXISTS Features;
CREATE TABLE `Features` (
  `id` int NOT NULL,
  `feature_name` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Inserting 12 rows into Features
-- Insert batch #1
INSERT INTO Features (id, feature_name) VALUES
(0, 'چشم انداز'),
(1, 'محل بازی کودکان'),
(2, 'صبحانه'),
(3, 'موسیقی زنده'),
(4, 'ارسال رایگان (Delivery)'),
(5, 'اینترنت رایگان'),
(6, 'سالاد بار'),
(7, 'سیگار'),
(8, 'قلیان'),
(9, 'دستگاه کارت خوان'),
(10, 'فضای باز'),
(11, 'پارکینگ');

-- END TABLE Features

