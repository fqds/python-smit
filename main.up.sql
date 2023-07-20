create table cargo_date (
    id bigserial not null primary key,
    date date not null unique
);

create table cargo (
    id bigserial not null primary key,
    cargo_date_id bigserial references cargo_date (id),
    cargo_type varchar not null,
    cargo_rate float not null
);