select * from Users order by username;

select * from Users order by registered desc limit 5;

select Users.username, count(*) from Listened inner join Users on Users.id = Listened.user_id group by user_id order by count(*) desc limit 5;

select Artists.name, count(*) from Albums inner join Artists on Artists.id = Albums.artist_id group by artist_id order by count(*);

select Artists.name, count(*) from Albums inner join Artists on Artists.id = Albums.artist_id inner join Songs on Songs.album_id = Albums.id group by Artists.name order by count(*);

select Artists.name, Albums.name, count(*) from Albums inner join Artists on Artists.id = Albums.artist_id inner join Songs on Songs.album_id = Albums.id group by Songs.album_id order by count(*) desc limit 1;

select Artists.name, Albums.name, total(Songs.duration) from Albums inner join Artists on Artists.id = Albums.artist_id inner join Songs on Songs.album_id = Albums.id group by Songs.album_id order by total(Songs.duration) desc limit 1;

select Artists.name, Albums.name, total(Songs.duration)/count(Songs.duration) from Albums inner join Artists on Artists.id = Albums.artist_id inner join Songs on Songs.album_id = Albums.id group by Songs.album_id order by total(Songs.duration)/count(Songs.duration) desc limit 1;

select Albums.artist_id, Albums.name, Listened.song_id, count(*) from Listened inner join Users on Users.id = Listened.user_id inner join Songs on Songs.id = Listened.song_id inner join Albums on Albums.id = Songs.album_id group by Listened.song_id order by count(*) desc limit 5;

select Albums.release_year, count(*) from Listened inner join Users on Users.id = Listened.user_id inner join Songs on Songs.id = Listened.song_id inner join Albums on Albums.id = Songs.album_id group by Albums.release_year order by count(*) desc limit 1;

select Artists.name, Albums.name, Songs.name, Listened.start_time from Listened inner join Songs on Songs.id = Listened.song_id inner join Albums on Albums.id = Songs.album_id inner join Artists on Artists.id = Albums.artist_id where Listened.user_id = 47 order by Listened.start_time desc limit 20;

select Users.username, Artists.name, Albums.name, Songs.name, count(*) from Listened inner join Songs on Songs.id = Listened.song_id inner join Albums on Albums.id = Songs.album_id inner join Artists on Artists.id = Albums.artist_id inner join Users on Users.id = Listened.user_id group by Listened.user_id, Listened.song_id;
