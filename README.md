# Introduction

YADI was written by Marcello Benedetti, Ephrem Berhe Gebremariam, Falitokiniaina Rabearison, Kiril Sardjoski, Reddy Aldino, and Ivan Vukić. It was written as a project for the Advance databases course which is part of Data Mining and Knowledge Management european master.


# What is it?

YADI is Command Line Interpreter for Datalog queries. It parses and evaluates Datalog queries on top of an SQL engine. Python language is used. Parsing of Datalog queries is achieved with PLY (Python Lex-Yacc). PostgreSQL database system is used.


# YADI's dynamics

YADI transforms a Datalog query to an Abstract Syntax Tree and provides with a query evaluation mechanism. YADI convert the query to an SQL statement and delegate the evaluation to the backend SQL engine (if any), moreower additional evaluation algorithms were designed. 


# What can I do with it?

To be edited later on. According to our level of achievement.


# Installation instructions

Dependecies
In order to compile this software, it is necessary to have the following software installed in the machine;
- Ocaml 4.0.0
- PostgreSQL 9.0
- Postgresql-ocaml 2.0.1
- findlib 1.3.1
- GNU Make 3.81

Pre-requisites
For running YADI it is necessary to have a connection to PostgreSQL database.
when starting the program it would be necessary to provide a username, database name, host, port and password.
the user will need having write/read permission over the database.

Follow these steps:
- Uncompress the source archive and go to the root directory,
- From the root directory, run "make",
- The final executable file can be found in the''bin/" directory and it will be called "YADI", i.e: \emph{bin/yadi},
- From starting to use the program, just execute the \emph{yadi} file, for information about the command line, 
  pass the ''--help" flag,

# Documentation

Documentation for YADI is available online via link(s). 


# Example
	A Datalog query against {R(A,B), S(B,C,D)} database looks like this:
		V(x,y) :- R(x,y) and S(y,_,_). 
		Q(x,y) :- S(x,y,z) and V(z,t) and t>=3.
		?- Q(x,y).
	Where the two first lines define idb predicates and the third line provides the actual query, i.e. the idb of the result set.
	The above Datalog query can be translated into the following SQL statement:
		SELECT S2.B, S2.C 
		FROM R, S S1, S S2  
		WHERE R.B=S1.B AND R.A=S2.D AND S1.B>=3
		

# Usage – operating instructions
To be edited later on.
	

# Requirements – configuration instructions

The programming language is Python. It is available for any Win32/Linux/MacOSX box. 

PLY (Python Lex-Yacc) Datalog Parser

Other ???

These can be installed by PIP from PyPI


# Contributing and Contact

Please feel free to send us feedback about forks, patches and any other kind. You can contact us via GitHub and also via email.

Ivan Vukic: vukicivan@yahoo.com
Ephrem Berhe Gebremariam: eepphhrreemm@gmail.com
Marcello Benedetti: 4marcello@gmail.com
Falitokiniaina Rabearison: r.falitokiniaina@gmail.com
Kiril Sardjoski: kiril.sardjoski@gmail.com
Reddy Aldino: redino26@gmail.com


# Credits and Aknowledgments

ddd


# License

Copyright (c) 2013. Authors. 

This code is distributed freely with no charges. Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without limitation of the rights to use, copy, modify, merge or distribute this software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
