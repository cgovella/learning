PRAGMA Foreign_Keys=True;

drop table author;
create table author (
ID Integer PRIMARY KEY,
Name Text NOT NULL
);

drop table book;
create table book (
ID Integer PRIMARY KEY,
Title Text NOT NULL
);

drop table book_author;
create table book_author (
bookID Integer NOT NULL REFERENCES book(ID),
authorID Integer NOT NULL REFERENCES author(ID)
);

insert into author (Name) values ('Jane Austin');
insert into author (Name) values ('Grady Booch');
insert into author (Name) values ('Ivar Jacobson');
insert into author (Name) values ('James Rumbaugh');

insert into book (Title) values('Pride & Prejudice');
insert into book (Title) values('Emma');
insert into book (Title) values('Sense & Sensibility');
insert into book (Title) values ('Object Oriented Design with Applications');
insert into book (Title) values ('The UML User Guide');

insert into book_author (BookID,AuthorID) values (
(select ID from book where title = 'Pride & Prejudice'),
(select ID from author where Name = 'Jane Austin')
);

insert into book_author (BookID,AuthorID) values (
(select ID from book where title = 'Emma'),
(select ID from author where Name = 'Jane Austin')
);

insert into book_author (BookID,AuthorID) values (
(select ID from book where title = 'Sense & Sensibility'),
(select ID from author where Name = 'Jane Austin')
);

insert into book_author (BookID,AuthorID) values (
(select ID from book where title = 'Object Oriented Design with Applications'),
(select ID from author where Name = 'Grady Booch')
);

insert into book_author (BookID,AuthorID) values (
(select ID from book where title = 'The UML User Guide'),
(select ID from author where Name = 'Grady Booch')
);

insert into book_author (BookID,AuthorID) values (
(select ID from book where title = 'The UML User Guide'),
(select ID from author where Name = 'Ivar Jacobson')
);

insert into book_author (BookID,AuthorID) values (
(select ID from book where title = 'The UML User Guide'),
(select ID from author where Name = 'James Rumbaugh')
);

