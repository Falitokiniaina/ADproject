DROP TABLE IF EXISTS movie CASCADE;
DROP TABLE IF EXISTS actor CASCADE;

CREATE TABLE movie (
    title TEXT PRIMARY KEY NOT NULL,
    director TEXT NOT NULL
);

CREATE TABLE actor (
    name TEXT PRIMARY KEY NOT NULL,
    lastName TEXT NOT NULL,
    title TEXT NOT NULL
);


INSERT INTO movie(title,director) VALUES('sevensamurai','kurosawa');
INSERT INTO movie(title,director) VALUES('sonofthenile','chahine');
INSERT INTO movie(title,director) VALUES('earthandashes','rahimi');
INSERT INTO movie(title,director) VALUES('ladolcevita','fellini');
INSERT INTO movie(title,director) VALUES('testmovie','rabearison');
INSERT INTO movie(title,director) VALUES('testmovie2','benedetti');

INSERT INTO actor(name,lastname,title) VALUES('kiril','sardjoski','sevensamurai');
INSERT INTO actor(name,lastname,title) VALUES('ivan','vukic','sevensamurai');
INSERT INTO actor(name,lastname,title) VALUES('ephrem','berhe','sonofthenile');
INSERT INTO actor(name,lastname,title) VALUES('reddy','aldino','earthandashes');
INSERT INTO actor(name,lastname,title) VALUES('fali','rabearison','ladolcevita');
INSERT INTO actor(name,lastname,title) VALUES('marcello','benedetti','ladolcevita');