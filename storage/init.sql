------- Services data -------
CREATE TABLE IF NOT EXISTS services (
    token                   TEXT NOT NULL PRIMARY KEY,
    write_token             TEXT NOT NULL UNIQUE,
    name                    TEXT NOT NULL UNIQUE,
    js_parser_code          TEXT,
    registered   TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

------- Statistics data -------
CREATE TABLE IF NOT EXISTS statistics (
    id                      SERIAL PRIMARY KEY,
    service_write_token     TEXT NOT NULL REFERENCES services(write_token) ON DELETE CASCADE,
    text                    TEXT,
    value                   FLOAT,
    bool                    BOOLEAN,
    datetime                TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);
