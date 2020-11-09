--Create tables
CREATE TABLE products (
    p_id varchar PRIMARY KEY,
    p_name varchar UNIQUE,
    p_onhand int NOT NULL,
    p_made int,
    p_shipped int,
    p_size int,
    p_unitweight int,
    p_desc string
);

CREATE TABLE orders(
    o_customer varchar PRIMARY KEY,
    o_amount int,
    o_price int UNIQUE,
    o_product varchar(20) NOT NULL,
    o_date int,
    o_shipdate string,
    o_recievedate string,
    o_id int
);

CREATE TABLE customers(
    c_id int PRIMARY KEY,
    c_fname varchar,
    c_lname varchar(20) NOT NULL,
    c_email int,
    c_address string(40)
);

CREATE TABLE suppliers(
    s_id varchar PRIMARY KEY,
    s_name varchar,
    s_product
);

CREATE TABLE payment(
    pay_id varchar PRIMARY KEY,
    pay_type varchar UNIQUE,
    pay_allowed varchar(20) NOT NULL

);

CREATE TABLE categories(
    cat_id varchar PRIMARY KEY,
    cat_name varchar UNIQUE,
    cat_desc varchar(20) NOT NULL

);










--Populate tables
INSERT INTO Products (
p_id,
p_name,
p_desc,
p_unitweight,
p_onhand, 
p_made ,
p_shipped


)
VALUES 
(1, 'healing salve','herbal healing', 6, 10,15, 5),
(2, 'Orange Cream', 'body butter', 6, 9,15, 6),
(3, 'Cocao Baby', 'body butter', 6, 14,15,1 ),
(4, 'Turmeric', 'facial bar', 2, 9,15,9 ),
(5, 'Chlorella', 'body bar',2, 15,15, 0),
(6, 'Himalayan Clay', 'body bar', 2, 15,15, 0),
(7, 'Clay' ,'body bar', 2, 14,15, 1),
(8, 'Rose', 'facial bar', 2, 7,15,8)
;


INSERT INTO orders(
    o_customer,
    o_price ,
    o_product, 
    o_amount,
    o_date,
    o_shipdate,
    o_recievedate,
    o_id
)
VALUES
(07, 120, '2,3,5,7',3,'10-25-2011','10-26-2011','10-30-2011',1004),
(09, 35,'2,8,5,1',1,'7-25-2011','7-26-2011','7-30-2011',1002 ),
(05, 16, '2,5,5,5',2,'2-25-2011','2-26-2011','2-30-2011',1001)
;

INSERT INTO Customers (
    c_id,
    c_fname,
    c_lname,
    c_email,
    c_address

)
VALUES 
(01, 'Alexa', 'Adams', 'aa11@gmail.com', '1234 Camino Ave'),
(02, 'David', 'Dire', 'dd44@gmail.com', '3387 Overland Ave'),
(03, 'Nathan', 'Night', 'nateman16@yahoo.com', '1224 1st St'),
(04, 'Shantelle', 'Snow', 'ss1818@gmail.com', '2359 Yosemite Ave'),
(05, 'Charles', 'Charleston', 'cc33@hotmail.com', '2466 Bear creek Rd'),
(06, 'Preston', 'Prescott', 'pp1616@yahoo.com', '3321 Gun Club Rd'),
(07, 'Estrella', 'Espinosa', 'ee890@gmail.com', '2399 Vera Cruz Rd'),
(08, 'Britney', 'Bodea', 'bb22@gmail.com', '1776 America Ave'),
(09, 'Jerome', 'Jakobs', 'jj1010@outlook.com', '3356 Main St'),
(10, 'Fatima', 'Fastin', 'ff66@outlook.com', '9909 Pickle Ct')
;

INSERT INTO Payment(
    pay_id, 
    pay_type, 
    pay_allowed 

)
VALUES
(007, 'cashapp', 'yes'),
(009, 'venmo', 'yes'),
(005, 'paypal', 'no')
;

INSERT INTO Suppliers(
	s_id,
	s_name,
	s_product
)
VALUES
(1, 'Supplier A', 'Rose'),
(2, 'Supplier B', 'Orange Cream'),
(3, 'Supplier C', 'Tumeric'),
(4, 'Supplier C', 'healing salve'),
(5, 'Supplier D', 'Himalayan Clay')
;

INSERT INTO Categories(
     cat_id, 
    cat_name,
    cat_desc
)
VALUES 
(007, 'body butter', 'whipped'),
(009, 'healing', 'herbal'),
(005, 'bar', 'detox')
;






--SQL Statements
--1
Select *
from suppliers;

--2
select c_fname, c_lname
from customers;

--3
select p_name 
from products 
where p_onhand <= 10;

--4
select o_amount, c_fname, c_lname
from orders, customers
where o_customer = c_id
and o_date like '10-25-2011';

--5
select p_name
from products
where p_unitweight < 5
group by p_desc;

--6
select distinct c_fname, c_lname, pay_allowed, pay_type
from customers, payment
where pay_id = c_id
and pay_type not like 'venmo'
group by pay_type; 

--7 
select distinct o_product, c_fname, c_lname
from customers, orders
where o_customer = c_id
and o_price > 20
group by c_id;

--8
select s_name
from suppliers, products
where s_product = p_name
and p_onhand <= 10
group by s_name;

--9
select count(distinct c_id) as custcount
from customers, orders
where o_customer = c_id
and o_amount >= 2;

--10
select c_fname, c_lname, o_price
from customers, orders
where o_customer = c_id
order by o_price desc;

--11 
select SUM(o_price)
from Orders;

--12 
select p_name
from products
where p_unitweight > 6
group by p_name;

--13 
select *
from categories;

--14 
select p_desc, c_fname
from products, customers, orders
where o_customer = c_id AND c_id = p_id
group by p_desc;

--15 
select s_name
from suppliers
where s_product ='Orange';

--16 
select AVG (p_onhand)
from products;

--17 
select *
from products;

--18 
select c_fname
from customers
order by c_fname ASC;


--19 
select o_customer
from orders,customers
where o_customer= c_id AND o_recievedate >'2-30-2011';


--20 
select cat_id
from categories
where cat_name ='bar';

/*
delete from customers
where c_id > 5;

insert into customers (c_id, c_fname, c_lname, c_email, c_address)
values (11, 'Xander', 'Rodriguez', 'XR30@protonmail.com', '9909 Pickle Ct');

update customers
set c_email = 'XR30@gmail.com'
where c_email like '%@protonmail.com';

update products
set p_onhand = 10
where p_onhand > 10;
*/



/*drop table products;
drop table orders;
drop table customers;
drop table Categories;
drop table Payment;
drop table suppliers;
*/