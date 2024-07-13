# Grad School Admissions Data API

## Github Repo

[Github Project Link](https://github.com/duskpeyl/GradX-Graduate-School-Admissions-API)

## Description

### Features

- **User Registration and Authentication**:
  - **Sign Up**: Users can create an account by providing an email and password.
  - **Login**: Registered users can log in using their credentials.

- **Profile Management**:
  - **View Profile**: Users can view their profile information including submitted applications.
  - **Edit Profile**: Users can update their personal information and application details.

- **Application Submission**:
  - **Add Application**: Users can add new application records, including details such as GPA, GRE scores, and application status.
  - **Update Application**: Users can edit their existing application details.
  - **Delete Application**: Users can remove an application if needed.
  
## Implementation Plan

### Entity Relationship Diagram for Database (ERD)

![ERD Diagram](docs/grad-api-erd.png)

### Overall Plan

![Overall Plan](docs/day_1.PNG)

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

### Imported Packages

* flask
* marshmallow-sqlalchemy
* flask-jwt
* flask-marshmallow
* flask-sqlalchemy
* psycopg2-binary
* bcrypt
* python-dotenv

### Functions/API Manual Page

## Additional Information

### How were the imported packages and dependencies used in this app?

### Why did I use an ORM for this project?

SQLAlchemy interacts with the database model using Python instead of raw SQL. I find that this reduces the amount of boilerplate code I need to write and makes it faster to iterate over in terms of testing and development.

SQLAlchemy and Flask require both little overhead for developers to run, whereas setting up a project without these libraries handling HTTP requests, routing, url handling, networking, database integration and database queries require a more in-depth understanding of web development, networking and databases.. It's a lot of unnecessary work for setting up an API webserver.

### How did database normalization affect the project database model?

### Benefits and drawbacks of using PostgreSQL

## References
