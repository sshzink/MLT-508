CREATE TABLE IF NOT EXISTS translations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    word VARCHAR(255) NOT NULL,
    source_language VARCHAR(255) NOT NULL,
    target_language VARCHAR(255) NOT NULL,
    translation TEXT,
    synonyms TEXT,
    pos VARCHAR(50)
);

INSERT INTO translations (word, source_language, target_language, translation, synonyms, pos)
VALUES
    ('hello', 'English', 'Spanish', 'hola', 'saludo', 'Noun'),
    ('cat', 'English', 'French', 'chat', 'felin', 'Noun');
