SELECT
    strftime("%Y-%m-%d", datetime) as short_date,
    MIN(tempwert),
    MAX(tempwert),
    AVG(tempwert)
FROM temperaturUndLuftdruck
GROUP BY short_date
ORDER BY short_date DESC
LIMIT 10;