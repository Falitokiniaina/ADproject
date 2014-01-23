# Introduction

YADI was written by Marcello Benedetti, Ephrem Berhe Gebremariam, Falitokiniaina Rabearison, Kiril Sardjoski, Reddy Aldino, and Ivan Vukić. It was written as a project for the Advance databases course which is part of Data Mining and Knowledge Management european master.


# What is it?

YADI is Command Line Interpreter for Datalog queries. It parses and evaluates Datalog queries on top of an SQL engine. Python language is used. Parsing of Datalog queries is achieved with PLY (Python Lex-Yacc). PostgreSQL database system is used.


# YADI's dynamics

YADI transforms a Datalog query to an Abstract Syntax Tree and provides with a query evaluation mechanism. YADI convert the query to an SQL statement and delegate the evaluation to the backend SQL engine, moreower additional evaluation algorithms were designed. 


# What can I do with it?

To be edited later on. According to our level of achievement.


# Installation instructions

The programming language is Python 3. It is available for any Win32/Linux/MacOSX box. 
A local or remote PostgreSQL database is also needed.

Dependecies
In order to run this software, it is necessary to have the following libraries installed in the machine:
- ply (Python Lex-Yacc)
- psycopg2 (PostgreSQL connection driver) 
- sqlalchemy (SQL toolkit)
The last version of these libraries can be easily intalled using pip (Python Package Index).

Pre-requisites
For running YADI it is necessary to have a connection to PostgreSQL database.
When starting the program it would be necessary to provide a username, database name, host, port and password.
The user will need having write/read permission over the database.


# Documentation

Documentation for YADI is available online via link(s). 


# Example
A Datalog rule for the database { movie(Title,Director), actor(Name,Lastname,Title) } looks like this:

	q(Y,Z) :- movie(X,Y) and actor(_,Z,X) and X!=shining.
	
Such rule create a view of movie.director and actor.lastname for all the movies except "Shining".
A Datalog query using the new rule would be:

	q(kubrick,X).
	
Such query returns lastnames of all the actors who worked with "Kubrick" except in "Shining".

# Usage – operating instructions

	python gui.py


Connection to the database can be done from the graphical user interface.
Default connection string:
postgresql+psycopg2://postgres:root@localhost:5432/adb
	

# Contributing and Contact

Please feel free to send us feedback about forks, patches and any other kind. You can contact us via GitHub and also via email.

Ivan Vukic: vukicivan@yahoo.com

Ephrem Berhe Gebremariam: eepphhrreemm@gmail.com

Marcello Benedetti: 4marcello@gmail.com 

Falitokiniaina Rabearison: r.falitokiniaina@gmail.com 

Kiril Sardjoski: kiril.sardjoski@gmail.com 

Reddy Aldino: redino26@gmail.com 


# Credits and Aknowledgments

(TODO)


# License

Copyright (c) 2013. Authors. 

This code is distributed freely with no charges. Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without limitation of the rights to use, copy, modify, merge or distribute this software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
