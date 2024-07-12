from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from init import ma, db


class Major(db.Model):
    __tablename__ = "majors"

    id: Mapped[int] = mapped_column(primary_key=True)
    major_name: Mapped[str] = mapped_column(String(200))
    
class MajorSchema(ma.Schema):
    class Meta:
        fields = ('major_name')