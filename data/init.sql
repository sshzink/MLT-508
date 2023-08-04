CREATE DATABASE IF NOT EXISTS mlt;

USE mlt;

CREATE TABLE IF NOT EXISTS words (
    id INT AUTO_INCREMENT PRIMARY KEY,
    form VARCHAR(255) NOT NULL,
    lang VARCHAR(2) NOT NULL,
    pos VARCHAR(50),
    eq_in_en TEXT,
    eq_in_es TEXT,
    eq_in_fr TEXT
);

INSERT INTO words (form, lang, pos, eq_in_en, eq_in_es, eq_in_fr)
VALUES
    ('dog', 'en', 'Noun', '', '2', '3'),
    ('perro', 'es', 'Noun', '1', '', '3'),
    ('chien', 'fr', 'Noun', '1', '2', ''),
    ('cat', 'en', 'Noun', '', '5', '6'),
    ('gato', 'es', 'Noun', '4', '', '6'),
    ('chat', 'fr', 'Noun', '4', '5', ''),
    ('like', 'en', 'Verb', '', '8', '9'),
    ('gustar', 'es', 'Verb', '7', '', '9'),
    ('aimer', 'fr', 'Verb', '7', '8', '');

