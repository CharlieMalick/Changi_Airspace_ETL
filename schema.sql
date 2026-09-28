CREATE TABLE sin_flight_snapshots (
    icao24 VARCHAR,
    callsign VARCHAR,
    longitude DOUBLE PRECISION,
    latitude DOUBLE PRECISION,
    altitude FLOAT,
    snapshot_time BIGINT,
    phase VARCHAR,
    PRIMARY KEY (icao24, snapshot_time)
);