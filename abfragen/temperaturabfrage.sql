SELECT
    MIN(tempwert) as "Maximal Temperatur",
    MAX(tempwert) as "Minimal Temperatur",
    AVG(tempwert) as "Durschnittstemperatur"
FROM temperaturUndLuftdruck
WHERE
    strftime('%m.%d', datetime) = '03.14' AND
    strftime('%Y', datetime) = strftime('%Y', DATE('NOW', '-1 year'));