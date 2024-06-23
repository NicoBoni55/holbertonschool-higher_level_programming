-- Listar todos los registros con nombre en second_table ordenados por score descendente
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;