-- TO CREATE/POPULATE DATABASE, GO TO ROOT PROJECT FOLDER
-- dropdb ling; createdb ling; psql ling -af create.sql
-- psql ling -af load.sql

CREATE TABLE Authors
(name VARCHAR(256) NOT NULL PRIMARY KEY,
 birthdate INTEGER CHECK(birthdate < date_part('year', current_date)));

CREATE TABLE Books
(uid INTEGER NOT NULL PRIMARY KEY,
 title VARCHAR(256) NOT NULL,
 date_published VARCHAR(256) NOT NULL,
 link_to_book VARCHAR(256) NOT NULL);
					      					       
 CREATE TABLE Writes
 (uid INTEGER NOT NULL REFERENCES Books(uid) PRIMARY KEY,
  name VARCHAR(256) NOT NULL REFERENCES Authors(name));
						
CREATE TABLE BookWordAggregates
(uid INTEGER NOT NULL REFERENCES Books(uid) PRIMARY KEY,
 per_sentence REAL NOT NULL,
 total_count REAL NOT NULL,
 avg-word-length REAL NOT NULL);

CREATE TABLE CommonWords
(uid INTEGER NOT NULL REFERENCES Books(uid),
 word VARCHAR(256) NOT NULL,
 frequency REAL NOT NULL,
 PRIMARY KEY(uid, word));
	     
CREATE TABLE Downloads
(uid INTEGER NOT NULL REFERENCES Books(uid) PRIMARY KEY,
  download INTEGER NOT NULL);

CREATE TABLE Sequences
(uid INTEGER NOT NULL REFERENCES Books(uid),
 word VARCHAR(256) NOT NULL REFERENCES CommonWords(word),
 next_word VARCHAR(256) NOT NULL REFERENCES CommonWords(word),
 times_appear REAL NOT NULL,
 PRIMARY KEY(uid, word, next_word));

CREATE TABLE User
(username VARCHAR(256) NOT NULL PRIMARY KEY,
email VARCHAR(256) NOT NULL,
password BINARY(64) NOT NULL);

CREATE TABLE UserRatings
(username VARCHAR(256) NOT NULL REFERENCES User(username),
 book_id INTEGER NOT NULL REFERENCES Books(uid),
rating INTEGER NOT NULL,
CHECK(rating > 0),
CHECK (rating < 11),
timestamp INTEGER NOT NULL,
PRIMARY KEY(username, book_id));
	     
CREATE TABLE UserReview
(username VARCHAR(256) NOT NULL ,
book_id INTEGER NOT NULL REFERENCES Books(uid),
review VARCHAR(256) NOT NULL,
 timestamp INTEGER NOT NULL,
PRIMARY KEY(username, book_id)););
	     
 CREATE TABLE CosineSimilarity
 (uid1 INTEGER NOT NULL REFERENCES Books(uid),
  uid2 INTEGER NOT NULL REFERENCES Books(uid),
  cos_similarity REAL NOT NULL,
  PRIMARY KEY(uid1, uid2));

 CREATE TABLE AuthorSimilarity
 (author1 VARCHAR(256) NOT NULL REFERENCES Authors(name),
  author2 VARCHAR(256) NOT NULL REFERENCES Authors(name),
  LDA_score REAL NOT NULL,
  cos_similarity REAL NOT NULL,
  PRIMARY KEY(author1, author2));
