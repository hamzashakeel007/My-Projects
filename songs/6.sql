Select name From songs where artist_id = (Select id From artists Where name = 'Post Malone');
