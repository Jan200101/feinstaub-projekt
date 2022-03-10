
CREATE TABLE feinstaubsensor (
    SensorID int,
    datetime DATETIME,
    p1wert float,
    p2wert float,
    
    PRIMARY KEY(SensorID, datetime)
);

