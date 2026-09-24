CREATE
USER data_controller_user WITH PASSWORD 'data_controller';
CREATE
USER train_user WITH PASSWORD 'train';

CREATE TABLE training_data
(
    id          BIGSERIAL PRIMARY KEY,
    carat       DOUBLE PRECISION NOT NULL,
    depth       DOUBLE PRECISION,
    table_value DOUBLE PRECISION,
    x           DOUBLE PRECISION,
    y           DOUBLE PRECISION,
    z           DOUBLE PRECISION,
    cut         VARCHAR(32)      NOT NULL,
    color       VARCHAR(16)      NOT NULL,
    clarity     VARCHAR(16)      NOT NULL,
    price       DOUBLE PRECISION NOT NULL,
    created_at  TIMESTAMPTZ      NOT NULL DEFAULT NOW()
);

GRANT
CONNECT
ON DATABASE ml_service TO data_controller_user;
GRANT CONNECT
ON DATABASE ml_service TO train_user;

GRANT USAGE ON SCHEMA
public TO data_controller_user;
GRANT USAGE ON SCHEMA
public TO train_user;

GRANT SELECT, INSERT, UPDATE, DELETE
    ON TABLE training_data
    TO data_controller_user;

GRANT SELECT
    ON TABLE training_data
    TO train_user;

GRANT USAGE, SELECT
    ON SEQUENCE training_data_id_seq
    TO data_controller_user;