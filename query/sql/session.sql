SELECT film.f_name, sessions.date_of_session, cinema_hall.name 
FROM sessions
JOIN film ON sessions.id_film = film.id_film
JOIN cinema_hall ON sessions.id_cinema_hall = cinema_hall.id_cinema_hall;
where cinema_hall.name = "$cinema_hall_name"