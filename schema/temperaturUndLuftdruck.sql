
CREATE TABLE temperaturUndLuftdruck (
    SensorID int,
    datetime DATETIME,
    luftwert float,
    tempwert float,

    PRIMARY KEY(SensorID, datetime)
);
