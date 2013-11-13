ADproject
=========

Yet Another Datalog Interpreter (YADI) 2

Yet Another Datalog Interpreter (YADI) 2

Abstract

The main purpose of the project is to develop a Command Line Interpreter for Datalog queries. It aims at parsing and evaluating Datalog queries on top of an SQL engine.

Outline

1. Groups and Grades
2. Functional Requirements
3. Technical Requirements
4. Project Management
5. Getting Started
6. References
Change log

2013-09-20: * Edited a pre-version of the project description
2013-10-04: * Added one maturity level on each scale
            * Added directions for the grammar and more...
	    * Added a local copy of the DES Manual V3.3.1 to bypass (temporary) dead links

1. Groups and Grades

up
This assignment is for groups of 6 non co-located students. Please, decide at least pairs of students on each location by Mon 30 September, 2013. Ultimately, we could arrange remote associations if required.

Take care of overall skills of the entire team by checking for basics in programming and database.

Grades for the project are assigned w.r.t. (a) strict observation of the directions, (b) quality of deliverables required in milestones, and (c) levels of achievement, as described in Sections below. Team members activity and project management may also have a (positive) impact on the final grade. It is of primary importance that each team member can show her own contribution to the project and that the overall workload is balanced among all the 6 members.

2. Functional Requirements

up
General Presentation

Yet Another Datalog Interpreter (YADI) 2 is basically a query engine for the Datalog language. It has to transforms a Datalog query to an Abstract Syntax Tree and provide with a query evaluation mechanism. There are three options: (a) convert the query to an SQL statement and delegate the evaluation to the backend SQL engine (if any), (b) design your own evaluation algorithms, and (c) mix both!

A Datalog query against {R(A,B), S(B,C,D)} database looks like this:

V(x,y) :- R(x,y) and S(y,_,_). 
Q(x,y) :- S(x,y,z) and V(z,t) and t>=3.
?- Q(x,y).
where the two first lines define idb predicates and the third line provides the actual query, i.e. the idb of the result set.
Despite its multiple-rules form, the above Datalog query is a Conjunctive Query that can be translated into the following SQL statement:

SELECT S2.B, S2.C 
FROM R, S S1, S S2  
WHERE R.B=S1.B AND R.A=S2.D AND S1.B>=3
The interpreter

The basic workflow of the interpreter is as follows:

Lexical analysis/parsing to extract tokens from charstream (Lex-like)
from "Movie(x, y)" to ("Movie", '(', "x", ',', "y", ')')
Syntactic analysis/parsing w.r.t. a grammar (Yacc-like)
...to Predicate ( Ident ("Movie"), [Var ("x"), Var ("y")] )
Static analysis for consistency, safety, etc.
Safe rule? check for x and y variables in a positive relational subgoal -> ok
[opt.] Rewritting for optimization purpose
SQL statement generation
SELECT * FROM Movies;
Query evaluation and pretty-print answer set
title           | director
-----------------------------
Seven Samurai     Kurosawa
Son of the Nile   Chahine
Earth and Ashes	  Rahimi
La Dolce Vita	  Fellini
For the query evaluation purpose, the communication with the backend SQL database must be well-established, including:

connect db;
get db state;
catch exceptions (wrong SQL statement, table doesn't exist, etc.);
retrieve answer set.
Levels of Achievement

The YADI project permits improvements along paths in three directions.

Expressive power

L1. CQ: one Datalog rule (or an equivalent decomposition program)
L2. FO: Datalog program with multiple rules
L3. Recursive queries w/o negation : SQL only
L4. Recursive queries w/o negation : non-recursive SQL + self-made recursion (semi-naive evaluation)
L5. Stratified negation
L6. DES (or death) maturity! 
User interface

L1. Command line interpreter with DB connexion
L2. Read/write script files and basic error handling (syntax)
L3. Full help/option commands with DB infos 
L4. Enhanced error handling (semantics)
L5. Syntactic color and completion features
L6. DES maturity
Datalog-like syntax

L1. Basic rules with relational predicates and equality and negation
L2. DDL (Data Definition Language) part: schemas and facts
L3. Built-in boolean predicates and anonymous variables and constants as predicate arguments
L4. Aggregate functions
L5. Attribute types management
L6. DES maturity
Details about the Datalog grammar are coming soon... available:
Follow the guidelines from the DES project V3.3.1+.
Both SQL and Relational Algebra parts are out of the scope of this project.
Please, focus on Datalog-related topics in the User's Manual. (grab the local copy)
2. Technical Requirements

up
The programming language is Python, preferably V3 or higher. It is available for any Win32/Linux/MacOSX box.

Eligible backend DBMS are relational (SQL) ones that map to the SQLAlchemy library and that can manage recursive (CTE) queries. PostgreSQL is probably the right choice.

Parsing of Datalog queries is achieved b.t.w. of the pyparsing library.

3. Project Management

up
YADI project must adhere to the many good practices of Open Source projects, among which setting up a virtual environment, testing, version control, project management and documentation. 

Each project team is required to use GitHub as source code hosting and collaborative software development tool.

Wiki and (automated) web pages of the GitHub repository serve the purpose of presenting the project.

In addition, each project team is required to open GitHub repository access to the four ADB instructors. The GitHub repos is going to be the first place where we can check for the project advancement. You are then asked to create issues with due dates and assign to team members.

The project is divided into 2 milestones (MS). All team members must equally contribute to both MS's.

MS1

up
There are four (4) tasks in MS1. At the end of MS1, each and every team masters the technical environment of the project and is capable to contribute in the development of new features, fix bugs and achieve new maturity levels.

Tasks and deliverables:
On a (>=L1, >=L1, >=L1) achievement level basis, provide with the source code in the GitHub repos.
Fill-in descriptive and setup files (README, install, license, etc.).
Edit Wiki and GitHub web pages with user manual, query examples, the current limitations and known issues, etc.
Expose your TODO list for the second milestone.
Due Date : Sun. November 17, 2013 23:59


MS2

up
The second part of the YADI project is basicaly a follow-on MS1. The primary goal is to achieve the highest maturity level on each of the three dimensions.

Tasks and deliverables: same as above, with more content inside.
Due Date: Sun. January 26, 2014 23:59


4. Getting Started

up
Find partners and form a (dream) team! post assignments in the Forum section. Warning: share skills among groups
Explore Python documentation/tutorials/examples/etc.
Learn basics in BNF grammars and experiment pyparsing librarie
Agree on workflows, standards, meeting dates, etc. with all other team members.
Set up your project environment, with virtual environment, version control system, backend database, GitHub collaborative tool, etc.
5. References

up
Python language
DES project
SQLAlchemy library
PostgreSQL database system
pyparsing library
good practices of Open Source projects
GitHub

Related projects worldwide:

Project proposal at the Univ. of British Columbia, CA and one report of achievement with the user guide.
Integrated Rule Inference System
Datalog Educational System
bddbddb
Datalog assignments in CS236
