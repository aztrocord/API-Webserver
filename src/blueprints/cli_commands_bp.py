from flask import Blueprint
from models.user import User
from models.user_application import Application
from models.major import Major
from models.degree_type import Degree_Type
from models.school import School
from init import db, bcrypt

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create_sample_data')
def seed_db():
    db.drop_all()
    print("Tables dropped")

    db.create_all()
    print("Tables created")

    university_majors = [
        Major(
            major_name='Computer_Science'
        ),
        Major(
            major_name='Neuroscience'
        ),
        Major(
            major_name='Psychology'
        ),
        Major(
            major_name='Civil_Engineering'
        ),
        Major(
            major_name='Chemical_Engineering'
        ),
    ]

    db.session.add_all(university_majors)
    db.session.commit()

    university_program_type = [
        Degree_Type(degree_type_name='MS/MSc'),
        Degree_Type(degree_type_name='MLA'),
        Degree_Type(degree_type_name='MFA'),
        Degree_Type(degree_type_name='PhD'),
    ]

    db.session.add_all(university_program_type)
    db.session.commit()
    
    universities = [
        School(school_name='Stanford', county='Santa_Clara', state='California', country='USA'),
        School(school_name='Harvard', county='Middlesex', state='Massachusetts', country='USA'),
        School(school_name='Princeton', county='Mercer', state='New_Jersey', country='USA'),
        School(school_name='Yale', county='New_Haven', state='Connecticut', country='USA'),
        School(school_name='MIT', county='Middlesex', state='Massachusetts', country='USA'),
    ]

    db.session.add_all(universities)
    db.session.commit()

    users = [
            User(
                email='admin@grad.com',
                password=bcrypt.generate_password_hash('harveynorman').decode('utf8'),
                is_admin=True
            ),
            User(
                email='normaluser@grad.com',
                first_name='John',
                last_name='Doe',
                password=bcrypt.generate_password_hash('john1984').decode('utf8'),
                undergrad_school_id=1,
                undergrad_major_id=1,
                undergrad_GPA='4.0',
                top_extracurriculars='Math Olympiad Gold Medalist, Google SWE Intern, Startup Founder with 50M in Seed Funding',
                gre_scores='327'
            )
        ]

    db.session.add_all(users)
    db.session.commit()

    user_applications = [
        Application(
            status='Rejected',
            school_id=3,
            major_id=1,
            user_id=2,
            degree_id=1
        )
    ]

    db.session.add_all(user_applications)
    db.session.commit()

    print("Users added")
    print("Universities added")
    print("Majors added")
    print("Degree Types added")
    print("Applications added")
    print("Tables seeded")
