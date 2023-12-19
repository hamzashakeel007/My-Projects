SELECT title FROM people, stars, movies WHERE people.id = stars.person_id AND stars.movie_id = movies.id
AND people.name = 'Bradley Cooper' UNION SELECT title FROM people, stars, movies WHERE people.id = stars.person_id
AND stars.movie_id = movies.id AND people.name = 'Jennifer Lawrence';
