# Grad School Admissions Data API

## Explain the problem that this app will solve, and explain how this app solves or addresses the problem.

## Describe the way tasks are allocated and tracked in your project.

## List and explain the third-party services, packages and dependencies used in this app.

## Explain the benefits and drawbacks of this app’s underlying database system.

## Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app.

## Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design. 

## This should focus on the database design BEFORE coding has begun, eg. during the project planning or design phase.

## Explain the implemented models and their relationships, including how the relationships aid the database implementation. This should focus on the database implementation AFTER coding has begun, eg. during the project development phase.

## Explain how to use this application’s API endpoints. Each endpoint should be explained, including the following data for each endpoint: HTTP verb, Path or route, Any required body or header data, Response

## Github Repo

[Github Project Link](https://github.com/duskpeyl/Graduate-School-Admissions-API)

## Description

### Features

## Implementation Plan

## Entity Relationship Diagram for Database (ERD)

### Overall Plan

### Dependencies  

* blinker==1.8.2
* click==8.1.7
* Flask==3.0.3
* greenlet==3.0.3
* itsdangerous==2.2.0
* Jinja2==3.1.4
* MarkupSafe==2.1.5
* marshmallow==3.21.3
* marshmallow-sqlalchemy==1.0.0
* packaging==24.0
* SQLAlchemy==2.0.30
* typing_extensions==4.12.2
* Werkzeug==3.0.3

### Imported Packages/Modules

* Flask
* marshmallow-sqlalchemy
* flask-sqlalchemy
* psycopg2-binary

### Functions/API Manual Page

## Additional Information

### Why did I use an ORM for this project?

SQLAlchemy interacts with the database model using Python instead of raw SQL. I find that this reduces the amount of boilerplate code I need to write and makes it faster to iterate over in terms of testing and development.

SQLAlchemy and Flask require both little overhead for developers to run, whereas setting up a project without these libraries handling HTTP requests, routing, url handling, networking, database integration and database queries require a more in-depth understanding of web development, networking and databases.. It's a lot of unnecessary work for setting up an API webserver.

### How did Database Normalization affect the project Database Model?

### Benefits and Drawbacks of using PostgreSQL

### References
