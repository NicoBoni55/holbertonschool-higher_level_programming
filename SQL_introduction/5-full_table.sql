-- descripcion completa de una tabla sql
SELECT 
    *
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_NAME = 'first_table'
    AND TABLE_SCHEMA = 'hbtn_0c_0';