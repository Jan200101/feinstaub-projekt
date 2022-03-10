SELECT
    MIN(tempwert) as "Maximal Temperatur",
    MAX(tempwert) as "Minimal Temperatur",
    AVG(tempwert) as "Durschnittstemperatur"
FROM temperaturUndLuftdruck
WHERE
    strftime('%m.%d', datetime) = '03.14'