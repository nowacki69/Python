sqlite3 cats_db.db

CREATE TABLE dogs (name TEXT, breed TEXT, age INTEGER);
CREATE TABLE cats (name TEXT, breed TEXT, age INTEGER);

INSERT INTO cats (name, breed, age) VALUES ("Blue","Scottish Fold", 3);
SELECT * FROM cats


INSERT INTO dogs (name, age, breed) VALUES ("Champ", 4, "Husky");
INSERT INTO dogs (name, age, breed) VALUES ("Rose", 11, "Chihuahua");
INSERT INTO dogs (name, age, breed) VALUES ("Moose", 5, "Lab");
INSERT INTO dogs (name, age, breed) VALUES ("Piggy", 9, "Corgi");

SELECT * FROM dogs WHERE breed IS NOT "Chihuahua" AND breed IS NOT "Corgi";
SELECT * FROM dogs WHERE name LIKE "%gg%";
