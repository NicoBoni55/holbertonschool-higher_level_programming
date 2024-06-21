-- enumerar todos los registros con un score >= 10 en la tabla second_table
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;