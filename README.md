# Grad School Admissions Data API

## Github Repo

[Github Project Link](https://github.com/duskpeyl/Graduate-School-Admissions-API)

## Description

### Features

## Implementation Plan

### Entity Relationship Diagram for Database (ERD)

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

* flask
* marshmallow-sqlalchemy
* flask-jwt
* flask-marshmallow
* flask-sqlalchemy
* psycopg2-binary
* bcrypt
* python-dotenv
* datetime

### Functions/API Manual Page

## Additional Information

### How Were the Imported Packages and Dependencies Used in This App?

### Why Did I Use an ORM for This Project?

SQLAlchemy interacts with the database model using Python instead of raw SQL. I find that this reduces the amount of boilerplate code I need to write and makes it faster to iterate over in terms of testing and development.

SQLAlchemy and Flask require both little overhead for developers to run, whereas setting up a project without these libraries handling HTTP requests, routing, url handling, networking, database integration and database queries require a more in-depth understanding of web development, networking and databases.. It's a lot of unnecessary work for setting up an API webserver.

### How Did Database Normalization Affect the Project Database Model?

### Benefits and Drawbacks of using PostgreSQL

### References
