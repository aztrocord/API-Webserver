from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from init import ma, db


class School(db.Model):
    __tablename__ = "schools"

    id: Mapped[int] = mapped_column(primary_key=True)
    school_name: Mapped[str] = mapped_column(String(200))
    county: Mapped[str] = mapped_column(String(200))
    state: Mapped[str] = mapped_column(String(200))
    country: Mapped[str] = mapped_column(String(200))
    
class SchoolSchema(ma.Schema):
    class Meta:
        fields = ('id', 'school_name', 'county', 'state', 'country')