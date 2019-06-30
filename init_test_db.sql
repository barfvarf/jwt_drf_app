-- Resets test database and required role
DROP DATABASE IF EXISTS drf_test_database;
DROP ROLE IF EXISTS drf_test_user;

CREATE ROLE drf_test_user WITH LOGIN PASSWORD 'password123';
ALTER ROLE drf_test_user SET client_encoding TO 'utf8';
ALTER ROLE drf_test_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE drf_test_user SET timezone TO 'UTC';
CREATE DATABASE drf_test_database WITH
    TEMPLATE = template0
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8';

ALTER DATABASE drf_test_database OWNER TO drf_test_user;
GRANT ALL PRIVILEGES ON DATABASE drf_test_database TO drf_test_user;
