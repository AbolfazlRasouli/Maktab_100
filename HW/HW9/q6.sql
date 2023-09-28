--1
-- select * from film
-- where release_year = 2006 and rental_rate >= 4.0



--2
-- select * from film
-- order by length desc
-- limit 10


--3
-- select count(customer.customer_id) , country.country
-- from customer
-- join address
-- on customer.address_id = address.address_id
-- join city
-- on address.city_id = city.city_id
-- join country
-- on city.country_id = country.country_id
-- group by country.country_id
-- order by country.country 


--4
-- select  title , rental_duration , Avg(rental_rate) from film
-- group by title, rental_duration
-- order by title



--5
-- select  customer.first_name, count(customer.customer_id) as c
-- from customer
-- join rental
-- on customer.customer_id = rental.customer_id
-- group by customer.customer_id
-- order by c
-- desc
-- limit 10





--6
-- select  customer.first_name , country.country
-- from customer
-- join address
-- on customer.address_id = address.address_id
-- join city
-- on address.city_id = city.city_id
-- join country
-- on city.country_id = country.country_id
-- where country.country = 'United States' and customer.first_name like 'A%'



--7
-- select * from film
-- where rental_duration > 5 and replacement_cost < 15.0




















