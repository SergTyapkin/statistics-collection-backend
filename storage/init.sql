------- Services data -------
CREATE TABLE IF NOT EXISTS services (
    token                   TEXT NOT NULL PRIMARY KEY,
    name                    TEXT NOT NULL,
    registration_datetime   TIMESTAMP WITH TIMEZONE NOT NULL DEFAULT NOW()
);

------- Statistics data -------
CREATE TABLE IF NOT EXISTS statistics (
    id                      SERIAL PRIMARY KEY,
    service_token           TEXT NOT NULL REFERENCES services(token) ON DELETE CASCADE,
    text                    TEXT,
    value                   DOUBLE,
    datetime                TIMESTAMP WITH TIMEZONE NOT NULL DEFAULT NOW()
);
