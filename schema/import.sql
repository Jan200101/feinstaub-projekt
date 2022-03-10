
CREATE TABLE DHT22_SCHEMA (
    sensor_id int,
    sensor_type TEXT,
    location int,
    lat float,
    lon float,
    timestamp DATETIME,
    temperatur float,
    humidity float
);

CREATE TABLE SDS011_SCHEMA (
    sensor_id int,
    sensor_type TEXT,
    location int,
    lat float,
    lon float,
    timestamp DATETIME,

    P1 int,
    durP1 float,
    ratioP1 float,

    P2 int,
    durP2 float,
    ratioP2 float
);