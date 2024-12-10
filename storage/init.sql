------- Services data -------
CREATE TABLE IF NOT EXISTS services (
    token                   TEXT NOT NULL PRIMARY KEY,
    name                    TEXT NOT NULL UNIQUE,
    registration_datetime   TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

------- Statistics data -------
CREATE TABLE IF NOT EXISTS statistics (
    id                      SERIAL PRIMARY KEY,
    service_token           TEXT NOT NULL REFERENCES services(token) ON DELETE CASCADE,
    text                    TEXT,
    value                   FLOAT,
    datetime                TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);
