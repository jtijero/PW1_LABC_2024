-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS prueba;

-- Usar la base de datos
USE prueba;

-- Crear tabla de actores
CREATE TABLE IF NOT EXISTS actores (
    actor_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100)
);

-- Crear tabla de películas
CREATE TABLE IF NOT EXISTS peliculas (
    pelicula_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    year INT,
    vote INT,
    score DECIMAL(3,1)
);

-- Crear tabla de casting
CREATE TABLE IF NOT EXISTS casting (
    casting_id INT PRIMARY KEY AUTO_INCREMENT,
    pelicula_id INT,
    actor_id INT,
    papel VARCHAR(100),
    FOREIGN KEY (pelicula_id) REFERENCES peliculas(pelicula_id) ON DELETE CASCADE,
    FOREIGN KEY (actor_id) REFERENCES actores(actor_id) ON DELETE CASCADE
);

-- Insertar datos de prueba en la tabla de actores
INSERT INTO actores (nombre) VALUES 
    ('Robert Downey Jr.'),
    ('Scarlett Johansson'), 
    ('Chris Hemsworth'),
    ('Mark Ruffalo'), 
    ('Chris Evans'), 
    ('Tom Holland');

-- Insertar datos de prueba en la tabla de películas
INSERT INTO peliculas (nombre, year, vote, score) VALUES 
    ('Avengers: Endgame', 2019, 8500, 8.4), 
    ('Iron Man', 2008, 4000, 7.9), 
    ('Thor', 2011, 3200, 7.0),
    ('Spider-Man: Homecoming', 2017, 6000, 7.4), 
    ('Avengers: Infinity War', 2018, 9000, 8.5), 
    ('Captain America: Civil War', 2016, 7500, 7.8);

-- Insertar datos de prueba en la tabla de casting
INSERT INTO casting (pelicula_id, actor_id, papel) VALUES 
    (1, 1, 'Iron Man'),
    (1, 2, 'Black Widow'), 
    (1, 3, 'Thor'),
    (1, 4, 'Hulk'),
    (1, 5, 'Captain America'),
    (1, 6, 'Spider-Man'),
    (2, 1, 'Iron Man'),
    (2, 2, 'Black Widow'),
    (3, 3, 'Thor'),
    (4, 6, 'Spider-Man'),
    (5, 1, 'Iron Man'),
    (5, 2, 'Black Widow'), 
    (5, 3, 'Thor'),
    (5, 4, 'Hulk'),
    (5, 5, 'Captain America'),
    (5, 6, 'Spider-Man'),
    (6, 5, 'Captain America'), 
    (6, 1, 'Iron Man'),
    (6, 2, 'Black Widow');

