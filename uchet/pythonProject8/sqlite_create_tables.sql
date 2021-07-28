create table if not exists goods
(
    id             INTEGER PRIMARY KEY NOT NULL,
    `name`         VARCHAR             NOT NULL,
    package_height FLOAT               NOT NULL,
    package_width  FLOAT               NOT NULL
);
create table if not exists shops_goods
(
    id       INTEGER PRIMARY KEY NOT NULL,
    id_good  INTEGER             NOT NULL,
    location VARCHAR             NOT NULL,
    amount   INTEGER             NOT NULL,
    FOREIGN KEY (id_good) REFERENCES goods (id)
);