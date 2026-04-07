--Basic Setup
USE movies_db;

--SELECT STATEMENT
SELECT * FROM movies;
SELECT title, industry FROM movies;

--WHERE CLAUSE
SELECT * FROM movies WHERE industry = "Hollywood";
SELECT * FROM movies WHERE imdb_rating = 7;

-- NULL check (correct way)
SELECT * FROM movies WHERE imdb_rating IS NULL;

--COUNT FUNCTION
SELECT COUNT(*) FROM movies;
SELECT COUNT(*) FROM movies WHERE industry = "Bollywood";

--DISTINCT KEYWORD
SELECT DISTINCT industry FROM movies;

--LIKE OPERATOR
SELECT * FROM movies WHERE title LIKE "%Thor%";
SELECT * FROM movies WHERE title LIKE "Avengers%";
SELECT * FROM movies WHERE title LIKE "%Man";

--AND / OR / BETWEEN / IN 
-- AND
SELECT * FROM movies 
WHERE imdb_rating >= 6 AND imdb_rating <= 8;

-- BETWEEN (better)
SELECT * FROM movies 
WHERE imdb_rating BETWEEN 6 AND 8;

-- OR
SELECT * FROM movies 
WHERE industry = "Hollywood" OR industry = "Bollywood";

-- IN (better than OR)
SELECT * FROM movies 
WHERE release_year IN (2019, 2022);

--NULL check
SELECT * FROM movies WHERE imdb_rating IS NULL;
SELECT * FROM movies WHERE imdb_rating IS NOT NULL;

--ORDER BY / LIMIT / OFFSET
-- Ascending
SELECT * FROM movies 
ORDER BY imdb_rating;

-- Descending
SELECT * FROM movies 
ORDER BY imdb_rating DESC;

-- Top 5
SELECT * FROM movies 
ORDER BY imdb_rating DESC 
LIMIT 5;

-- Offset
SELECT * FROM movies 
ORDER BY imdb_rating DESC 
LIMIT 5 OFFSET 1;

--SUMMARY ANALYTICS
SELECT MIN(imdb_rating) FROM movies WHERE industry = "Bollywood";
SELECT MAX(imdb_rating) FROM movies WHERE industry = "Bollywood";
SELECT AVG(imdb_rating) FROM movies WHERE industry = "Hollywood";

--ROUND
SELECT ROUND(AVG(imdb_rating), 2) 
FROM movies 
WHERE studio = "Marvel Studios";

--ALIAS
SELECT ROUND(AVG(imdb_rating), 2) AS average_rating
FROM movies 
WHERE studio = "Marvel Studios";

--GROUP BY
SELECT industry, COUNT(*) 
FROM movies 
GROUP BY industry;

--HAVING
SELECT industry, COUNT(*) AS total_movies
FROM movies
GROUP BY industry
HAVING total_movies > 2;

select release_year,count(*) as mov_count
from movies
where imdb_rating >= 2
group by release_year
having mov_count > 2
order by mov_count desc;

--YEAR and CURRENT_DATE
select year(current_date());
select curdate()


--IF
select *, if(currency='usd', revenue*77,revenue) as revenue_inr  from financials;

--CASE
select *,
case 
	when unit="thousands" then revenue/1000
    when unit="billions" then revenue*1000
    else revenue
end as revenue_mln
from financials;

--SQL JOINS
--inner JOIN
select 
m.movie_id,budget,revenue, currency, unit 
from movies m
join financials f
on m.movie_id=f.movie_id;


