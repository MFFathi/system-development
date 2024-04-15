CREATE TABLE IF NOT EXISTS city(
    id uuid NOT NULL DEFAULT gen_random_uuid() UNIQUE,
    name text NOT NULL UNIQUE,
    PRIMARY KEY (id)
)