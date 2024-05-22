-- This script group all the records with same scores
SELECT score, COUNT(1) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;

