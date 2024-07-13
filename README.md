# Grad School Admissions Data API

## Github Repo

[Github Project Link](https://github.com/duskpeyl/GradX-Graduate-School-Admissions-API)

## Description

College admissions is a difficult process.

Especially so for the 1.1 million members of the community [r/ApplyingToCollege](https://www.reddit.com/r/ApplyingToCollege/), many of which are obsessed with so-called "[t20 colleges](https://www.usnews.com/best-colleges/rankings/national-universities)". A term referring to colleges ranked amongst top 20 national universities in the United States, typically ranked by publications such as U.S. News & World Report.

Selective colleges within the t20 receive an upwards of [60,000 applications](https://www.forbes.com/sites/christopherrim/2024/03/29/this-year-was-a-historic-ivy-league-application-season-heres-what-you-need-to-know/) in a given year, making it truly difficult for students have a clearer understanding and grasp of their standing amongst other applicants. For those slightly older, many of these universities are also popular destinations for sudents aiming for postgraduate programs.

GradX is a REST API that aggregates self-reported postgraduate admissions data from top university programs and seeks to resolve that problem for aspiring postgraduate students, by allowing users to compare their applications to other candidates based on their extracurriculars, standardized testing scores and grades.

### Features

- **User Registration and Authentication**:
  - **Sign Up**: Users can create an account by providing an email and password.
  - **Login**: Registered users can log in using their credentials.

- **Profile Management**:
  - **View Profile**: Users can view their profile information on their account.
  - **Edit Profile**: Users can update their personal information on their account.
  - **Delete Profile**: Users can delete their profile.

- **Application Submission**:
  - **Add Application**: Users can add new application records, including details such as GPA, GRE scores, and application status.
  - **View Applications**: Users can view other people's applications and compare their stats.
  - **Update Application**: Users can edit their existing application details.
  - **Delete Application**: Users can remove an application if needed.
  
## Implementation Plan

### Entity Relationship Diagram for Database (ERD)

![ERD Diagram](docs/grad-api-erd.png)

### Overall Plan

![Day-to-Day-1](docs/day_1.PNG)
![Day-to-Day-2](docs/day_2.PNG)

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
