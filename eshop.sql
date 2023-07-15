--sqlite3
-- create table products(id, title, price)

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price INTEGER
);

INSERT INTO products(title, price) VALUES
('iPhone', 1000),
('Samsung', 800),
('Xiaomi', 600),
('Huawei', 500),
('Nokia', 400),
('Sony', 300),
('LG', 200),
('HTC', 100);