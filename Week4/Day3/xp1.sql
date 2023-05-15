-- 1 select name from language;
-- 2 select title,description, language.name
-- from film
-- join language on film.language_id = language.language_id;
-- 2/1 select title,description, language.name
-- from film
-- left join language on film.language_id = language.language_id;
-- 2/2 select title,description, language.name
-- from film
-- right join language on film.language_id = language.language_id;
-- create table new_film(id serial primary key,
-- 					 name varchar(30));

-- insert into new_film(name)
-- values('Born');
-- insert into new_film(name)
-- values('Armageddon')

-- create table customer_review(review_id serial primary key,
-- 							film_id int references new_film(id),
-- 							language_id int references language(language_id),
-- 							title varchar(50),
-- 							score int,
-- 							review_text varchar,
-- 							last_update date);
-- insert into customer_review(title,score,review_text,last_update)
-- values('Great  film about something',7,'Great film about earthquake','2023/03/20');
-- insert into customer_review(title,score,review_text,last_update)
-- values('Great  film about something',7,'Great film about hurricane','2023/03/20')

-- create table customer_review(review_id serial primary key,
-- 							film_id int not null,
-- 							language_id int not null,
-- 							foreign key (language_id)  references language(language_id),
-- 							title varchar(50),
-- 							score int,
-- 							review_text varchar,
-- 							last_update date,
-- 							foreign key (film_id)  references new_film(id)
-- 							on delete cascade
-- 							);
-- insert into customer_review(film_id, language_id, title, score, review_text, last_update)
-- values (2, 1, 'Great film about something', 7, 'Great film about earthquake', '2023-03-20'),
--        (3, 2, 'Awesome movie about nothing', 8, 'Awesome movie about love and friendship', '2023-04-01');
-- delete from new_film where id=2;