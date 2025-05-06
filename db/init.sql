CREATE DATABASE db
  WITH ENCODING 'UTF8'
  LC_COLLATE='tr_TR.UTF-8'
  LC_CTYPE='tr_TR.UTF-8'
  TEMPLATE=template0;

GRANT ALL PRIVILEGES ON DATABASE db TO admin;

\c db

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_schema = 'public'
        AND table_name = 'users'
    ) THEN
        CREATE TABLE users (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            username VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        );

        INSERT INTO users (username, password) VALUES ('ÖMER', '12345678');
        INSERT INTO users (username, password) VALUES ('FURKAN', '87654321');
    END IF;
END $$;
