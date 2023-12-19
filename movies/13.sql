SELECT DISTINCT name FROM people, stars, movies WHERE people.id = stars.person_id AND stars.movie_id = movies.id
AND LIKE people.name = 'Kevin Bacon' AND people.birth = 1958;
