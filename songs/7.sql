Select Avg(energy) from songs Where artist_id = (Select id From artists Where name = 'Drake');
