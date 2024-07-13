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
    degree_id: Mapped[int] = mapped_column(ForeignKey('degree_types.id'))

    school: Mapped['School'] = relationship()
    major: Mapped['Major'] = relationship()
    user: Mapped['User'] = relationship()
    degree_type: Mapped['DegreeType'] = relationship()

class ApplicationSchema(ma.Schema):
    school = fields.Nested('SchoolSchema')
    major = fields.Nested('MajorSchema')
    degree_type = fields.Nested('DegreeTypeSchema')
    user = fields.Nested('UserSchema', exclude=['password'])
    class Meta:
        fields = ('id', 'status', 'school', 'major', 'user', 'degree_type')