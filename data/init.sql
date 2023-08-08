CREATE DATABASE IF NOT EXISTS mlt;

USE mlt;

CREATE TABLE IF NOT EXISTS words (
    id INT AUTO_INCREMENT PRIMARY KEY,
    form VARCHAR(255) NOT NULL,
    lang VARCHAR(2) NOT NULL,
    pos INT,
    eq_in_en TEXT,
    eq_in_es TEXT,
    eq_in_fr TEXT
);

INSERT INTO words (form, lang, pos, eq_in_en, eq_in_es, eq_in_fr)
VALUES
    ('dog', 'en', 1, '', '2', '3'),
    ('perro', 'es', 1, '1', '', '3'),
    ('chien', 'fr', 1, '1', '2', ''),
    ('cat', 'en', 1, '', '5', '6'),
    ('gato', 'es', 1, '4', '', '6'),
    ('chat', 'fr', 1, '4', '5', ''),
    ('like', 'en', 2, '', '8', '9'),
    ('gustar', 'es', 2, '7', '', '9'),
    ('aimer', 'fr', 2, '7', '8', '');

