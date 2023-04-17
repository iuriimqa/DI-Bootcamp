-- select * from customer;
-- select concat(first_name,last_name) as full_name from customer;
-- select distinct create_date from customer;
-- select * from customer order by first_name desc;
-- select film_id, title, description, release_year,rental_rate from film order by rental_rate;
-- select address,phone from address where district = 'Texas';
-- select * from film where film_id = 15 or film_id =150;
-- select film_id, title, description, length, rental_rate from film where title ='Avatar';
-- select film_id, title, description, length, rental_rate from film where title ='Av%';
-- select * from film order by rental_rate limit 10;
-- select * from film order by rental_rate offset 10 limit 10;
-- SELECT first_name,last_name, amount,payment_date
-- FROM customer
-- RIGHT JOIN payment ON payment.customer_id = customer.customer_id
-- ORDER BY payment.customer_id;
-- select film_id from film except select film_id from inventory;
-- 14 select city.city,country.country
-- from country
-- join city on city.country_id = country.country_id;
-- 15 select customer.customer_id,customer.first_name,customer.last_name,amount,payment_date
-- from customer
-- join payment on customer.customer_id = payment.customer_id
-- order by staff_id;



