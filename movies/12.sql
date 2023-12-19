SELECT title FROM people, stars, movies WHERE people.id = stars.person_id AND stars.movie_id = movies.id
AND IN (people.name = 'Bradley Cooper' AND IN people.name = 'Jennifer Lawrence';
