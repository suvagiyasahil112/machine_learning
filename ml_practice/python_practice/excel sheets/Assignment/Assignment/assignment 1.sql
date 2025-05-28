show databases;
use assignment_1;
show tables;
use bigmart;
Create Table products (
Code int auto_increment primary key,
Name varchar(15),
Price int(3),
Manufacturer int(2)
);






use sahil;

show tables;
select * from company c ;

delete sahil;




 
select * from products;
insert into products(code,name,price,Manufacturer) values 
(1,'Hard drive',240,5),
(2,'Memory',120,6),
(3,'ZIP drive',150,4),
(4,'Floppy disk',5,6),
(5,'Monitor',240,1),
(6,'DVD drive',180,2),
(7,'CD drive',90,2),
(8,'Printer',270,3),
(9,'Toner cartridge',66,3),
(10,'DVD burner',180,2);

show tables;

select * from manufactures ;
create table manufactures(
code int(2),
name varchar(15)
);

insert into manufactures (code,name) values
(1,'Sony'),
(2,'Creative Labs'),
(3,'Hewlett-Packard'),
(4,'Lomega'),
(5,'Fujitsu'),
(6,'Winchester');

select *from products;

#1. Select the names of all the products in the store
select name from products;

#2. Select the names and the prices of all the products in the store
select name, price from products ;

#3. Select the name of the products with a price less than or equal to $200
select price from products where price <200;

#4. Select all the products with a price between $60 and $120.
select price from products where price between 60 and 120;

#5. Select the name and price in cents (i.e. the price must be multiplied by 100).
select name,price,price*100 as price_in_cents from products;

#6. Compute the average price of all the products.
select avg(price) from products;


#7. Compute the average price of all products with manufacturer code equal to 2.
select avg(price) from products where manufacturer=2;

#8. Compute the number of products with a price larger than or equal to $180.
select count(price) from products where price>=180;

#9. Select the name and price of all products with a 
#price larger than or equal to $180, and sort first by
# price (in descending order), and then by name (in ascending order).
select name,price from products where price >=180 order by price desc, name asc;

#10. Select all the data from the products, including all the data for each product's manufacturer.
select*from products join manufactures 
on products.manufacturer=manufactures.code;

#11. Select the product name, price, and manufacturer name of all the products.
select products.Name,products.Price, manufactures.name as Manufacturer_name 
from products join manufactures 
on products.Manufacturer=Manufactures.code;

#12. Select the average price of each manufacturer's products, showing only the manufacturer's code.
select avg(price), Manufactures.code 
from products join manufactures on products.manufacturer=Manufactures.code 
group by Manufacturer ;

#13. Select the average price of each manufacturer's products, showing the manufacturer's name
select avg(price), Manufactures.name 
from products join manufactures on products.manufacturer=Manufactures.code 
group by Manufacturer ;

14. Select the names of manufacturer whose products have an average price larger than or equal to $150.
select avg(price), Manufactures.name 
from products join manufactures on products.manufacturer=Manufactures.code 
group by Manufacturer having avg(price)>=150 ;

#15. Select the name and price of the cheapest product
select name,price from products order by  Price asc limit 1;

#16. Select the name of each manufacturer along with the name and price of its most expensive product.
select pt.Name ,pt.Price, m.name 
from products pt join manufactures m
on pt.manufacturer=m.code order by pt.Price desc limit 1;

#17. Add a new product: Loudspeakers, $70, manufacturer 2.
insert into products (name,Price,Manufacturer)
values ('loudspeakers',70,2);

select *from products p ;

#18. Update the name of product 8 to "Laser Printer".
update products set name='leser printer' where code=8 ;

#19. Apply a 10% discount to all products.
select price*0.90 from products p ;

#20. Apply a 10% discount to all products with a price larger than or equal to $120.
select Price, price*0.9 as discount from products having Price>=120;


create table feedback (
Firstname varchar(24),middlename varchar(24),Lastname varchar(24),
Phone integer(10),Email varchar(24),Password varchar(24));








create table feedback(
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    feedback TEXT NOT NULL,
    rating VARCHAR(40) NOT NULL
);


select * from feedback;












-- 2024

-- 

select * from manufactures m ;

select * from product_table pt  ;


-- 1
select name  from product_table pt ;


-- 2
select name,price  from product_table pt ;


-- 3
select name,price from product_table pt where price <200;

-- 4


select name,price  from product_table pt where price <120 and price >60 ;

-- 5

select name ,price *100 as price_in_cents from product_table pt ;

-- 6
select avg(price)  from product_table pt where manufacturer =2 and code!=11;


-- 7

-- delete from product_table where code =11;
-- select * from product_table pt ;

select pt.name ,pt.price ,m.name ,pt.manufacturer ,m.code  from product_table pt join manufactures m on pt.manufacturer =m.code order by pt.manufacturer asc ;




-- 8
select count(*)  from product_table pt where price >=180 ;




-- 9

select pt.name ,pt.price  from product_table pt where pt.price>=180 order by pt.price desc  ;

select pt.name ,pt.price  from product_table pt where pt.price>=180 order by pt.name asc  ;



-- 10
select * from product_table pt join manufactures m on pt.manufacturer =m.code ;



-- 11
select pt.name as product_name ,pt.price ,m.name as manufecturers_name  from product_table pt join manufactures m on pt.manufacturer =m.code ;




-- 12 and 13
select m.name ,avg(pt.price)  from product_table pt join manufactures m on pt.manufacturer =m.code group by pt.manufacturer  ;


-- 14

select * from product_table pt join manufactures m on pt.manufacturer =m.code ;


-- 15

select name,price  from product_table order by price asc limit 1;



-- 16

select m.name, pt.name,min( pt.price) as min_price  from product_table pt join manufactures m on pt.manufacturer =m.code group by m.name  ;



select * from product_table pt ;



-- 17

insert into product_table (code,name,price,manufacturer) values (11,'loudspeaker',90,2);


-- 18

update product_table set name='laser printer' where code=8;


select * from product_table pt ;


-- 19

select *,price*0.90 as after_discount from product_table pt ;


-- 20

select *,price*0.90 as after_discount from product_table pt having price >=120 ;




-- assignment 2222222222222
use sahil;
show databases;
use feedback;
show tables;
select * from bigmart;
select * from feedback f;

