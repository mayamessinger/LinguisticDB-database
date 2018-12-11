-- TO CREATE/POPULATE DATABASE, GO TO ROOT PROJECT FOLDER
-- dropdb ldb; createdb ldb; psql ldb -af create.sql
-- psql ldb -af load.sql

CREATE TABLE Authors
(name VARCHAR(256) NOT NULL PRIMARY KEY,
 birthdate INTEGER CHECK(birthdate < date_part('year', current_date)));

CREATE TABLE Books
(uid INTEGER NOT NULL PRIMARY KEY,
 title VARCHAR(512) NOT NULL,
 date_published VARCHAR(256) NOT NULL,
 link_to_book VARCHAR(256) NOT NULL);

 CREATE TABLE Writes
 (uid INTEGER NOT NULL REFERENCES Books(uid) PRIMARY KEY,
  name VARCHAR(256) NOT NULL REFERENCES Authors(name));

CREATE TABLE BookWordAggregates
(uid INTEGER NOT NULL REFERENCES Books(uid) PRIMARY KEY,
 per_sentence REAL NOT NULL,
 total_count REAL NOT NULL,
 avg_word_length REAL NOT NULL);

CREATE TABLE CommonWords
(uid INTEGER NOT NULL REFERENCES Books(uid),
 word VARCHAR(256) NOT NULL,
 frequency INTEGER NOT NULL,
 PRIMARY KEY(uid, word));

CREATE TABLE Downloads
(uid INTEGER NOT NULL REFERENCES Books(uid) PRIMARY KEY,
  download INTEGER NOT NULL);

CREATE TABLE Sequences
(uid INTEGER NOT NULL REFERENCES Books(uid),
 word VARCHAR(256) NOT NULL,
 next_word VARCHAR(256) NOT NULL,
 times_appear REAL NOT NULL,
 PRIMARY KEY(uid, word, next_word));

CREATE TABLE Users
(username VARCHAR(256) NOT NULL PRIMARY KEY,
email VARCHAR(256) NOT NULL,
password VARCHAR(256) NOT NULL);

CREATE TABLE UserRatings
(username VARCHAR(256) NOT NULL REFERENCES Users(username),
 book_id INTEGER NOT NULL REFERENCES Books(uid),
rating INTEGER NOT NULL CHECK(rating > 0) AND (rating < 11),
timestamp TIMESTAMP NOT NULL,
PRIMARY KEY(username, book_id));

CREATE TABLE UserReview
(username VARCHAR(256) NOT NULL REFERENCES Users(username),
book_id INTEGER NOT NULL REFERENCES Books(uid),
review VARCHAR(256) NOT NULL,
timestamp TIMESTAMP NOT NULL,
PRIMARY KEY(username, book_id));

 CREATE TABLE CosineSimilarity
 (uid1 INTEGER NOT NULL REFERENCES Books(uid),
  uid2 INTEGER NOT NULL REFERENCES Books(uid),
  cos_similarity REAL NOT NULL,
  rank INTEGER NOT NULL,
  PRIMARY KEY(uid1, uid2));

 CREATE TABLE AuthorSimilarity
 (author1 VARCHAR(256) NOT NULL REFERENCES Authors(name),
  author2 VARCHAR(256) NOT NULL REFERENCES Authors(name),
  cos_similarity REAL NOT NULL,
  rank INTEGER NOT NULL,
  PRIMARY KEY(author1, author2));

CREATE INDEX BookTitles ON Books(title);
CREATE INDEX AuthorWrites ON Writes(name);
CREATE INDEX Aggregates1 ON BookWordAggregates(per_sentence);
CREATE INDEX Aggregates2 ON BookWordAggregates(total_count);
CREATE INDEX Aggregates3 ON BookWordAggregates(avg_word_length);
CREATE INDEX CommonWordsIndex ON CommonWords(word);
CREATE INDEX SequencesIndex ON Sequences(word);
CREATE INDEX Cos1 ON CosineSimilarity(uid1);
CREATE INDEX Author1 ON AuthorSimilarity(author1);
