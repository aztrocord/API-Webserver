from typing import Optional, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, ForeignKey
from marshmallow import fields
from init import ma, db


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[Optional[str]] = mapped_column(String(100))
    last_name: Mapped[Optional[str]] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(250), unique=True)
    password: Mapped[str] = mapped_column(String(250))
    is_admin: Mapped[bool] = mapped_column(Boolean(), server_default='false')

    undergrad_GPA: Mapped[Optional[str]] = mapped_column(String(250))
    top_extracurriculars: Mapped[Optional[str]] = mapped_column(String(250))
    gre_scores: Mapped[Optional[str]] = mapped_column(String(250))

    undergrad_school_id: Mapped[Optional[int]] = mapped_column(ForeignKey('schools.id'))
    undergrad_school: Mapped['School'] = relationship()

    undergrad_major_id: Mapped[Optional[int]] = mapped_column(ForeignKey('majors.id'))
    undergrad_major: Mapped['Major'] = relationship()

class UserSchema(ma.Schema):
    undergrad_school = fields.Nested('SchoolSchema')
    undergrad_major = fields.Nested('MajorSchema')
    user_applications = fields.Nested('ApplicationSchema')
    email = fields.Email(required=True)
    password = fields.String(min=8, required=True)

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'is_admin', 'undergrad_school', 'undergrad_major', 'undergrad_GPA', 'top_extracurriculars', 'gre_scores')
        include_relationships = True

class UpdateUserSchema(ma.Schema):
    undergrad_school = fields.Nested('SchoolSchema')
    undergrad_major = fields.Nested('MajorSchema')
    user_applications = fields.Nested('ApplicationSchema')

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'is_admin', 'undergrad_school', 'undergrad_major', 'undergrad_GPA', 'top_extracurriculars', 'gre_scores')
        include_relationships = True