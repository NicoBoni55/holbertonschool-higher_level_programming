-- crear una tabla completa
-- con los datos id, name y score
CREATE TABLE IF NOT EXISTS second_table
(
    id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    score INT NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO second_table (id, name, score)
VALUES (1, 'Jhon', 10)
ON DUPLICATE KEY UPDATE name=VALUES(name), score=VALUES(score);

INSERT INTO second_table (id, name, score)
VALUES (2, 'Alex', 3)
ON DUPLICATE KEY UPDATE name=VALUES(name), score=VALUES(score);

INSERT INTO second_table (id, name, score)
VALUES (3, 'Bob', 14)
ON DUPLICATE KEY UPDATE name=VALUES(name), score=VALUES(score);

INSERT INTO second_table (id, name, score)
VALUES (4, 'George', 8)
ON DUPLICATE KEY UPDATE name=VALUES(name), score=VALUES(score);