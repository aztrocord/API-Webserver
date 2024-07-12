from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from marshmallow import fields
from init import ma, db


class Application(db.Model):
    __tablename__ = "Applications"

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String(50))
    school_id: Mapped[int] = mapped_column(ForeignKey('schools.id'))
    major_id: Mapped[int] = mapped_column(ForeignKey('majors.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    school: Mapped['School'] = relationship('School')
    major: Mapped['Major'] = relationship('Major')
    user: Mapped['User'] = relationship('User')

class ApplicationSchema(ma.Schema):
    school = fields.Nested('SchoolSchema')
    major = fields.Nested('MajorSchema')
    user = fields.Nested('UserSchema')
    class Meta:
        fields = ('status', 'school', 'major', 'user')