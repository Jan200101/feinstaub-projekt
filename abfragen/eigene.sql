SELECT
	strftime("%Y-%m-%d", datetime) as short_date,
	MIN(tempwert),
	MAX(tempwert),
	AVG(tempwert)
FROM temperaturUndLuftdruck
GROUP BY tempwert
ORDER BY tempwert DESC
LIMIT 10;