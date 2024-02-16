DROP TABLE IF EXISTS movies;
DROP SEQUENCE IF EXISTS movies_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS movies_id_seq;
CREATE TABLE movies (
  id SERIAL PRIMARY KEY,
  title VARCHAR,
  genre VARCHAR,
  release_year INT
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO movies (title, genre, release_year) VALUES ('The Dark Knight', 'Action/crime', 2008);


