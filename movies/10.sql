SELECT name FROM people, directors, movies, ratings, WHERE people.id = directors.person_id AND directors.movie_id = movies.id AND
movies.year = 2004
