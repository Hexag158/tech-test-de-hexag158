DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS places;

CREATE TABLE places (
  id INT NOT NULL AUTO_INCREMENT,
  city VARCHAR(100),
  county VARCHAR(100),
  country VARCHAR(100),
  PRIMARY KEY (id)
);

CREATE TABLE people (
  id INT NOT NULL AUTO_INCREMENT,
  given_name VARCHAR(100),
  family_name VARCHAR(100),
  date_of_birth DATE,
  place_of_birth VARCHAR(100),
  place_id INT,
  FOREIGN KEY (place_id) references places(id),
  PRIMARY KEY (id)
);