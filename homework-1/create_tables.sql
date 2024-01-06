-- SQL-команды для создания таблиц
CREATE TABLE employees_data
(employee_id serial PRIMARY KEY,
 first_name varchar(50) NOT NULL,
 last_name varchar(50) NOT NULL,
 title varchar(100) NOT NULL,
 birth_date date NOT NULL,
 notes text
);

CREATE TABLE customers_data
(customer_id varchar(20) PRIMARY KEY,
 company_name varchar(100) NOT NULL,
 contact_name varchar(50) NOT NULL
);

CREATE TABLE orders_data
(order_id int PRIMARY KEY,
 customer_id varchar(20) REFERENCES customers_data(customer_id),
 employee_id int REFERENCES employees_data(employee_id),
 order_date date NOT NULL,
 ship_city varchar(50) NOT NULL
);
