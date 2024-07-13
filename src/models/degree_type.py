from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from init import ma, db


class Degree_Type(db.Model):
    __tablename__ = "degree_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    degree_type_name: Mapped[str] = mapped_column(String(200))
    
class DegreeTypeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'major_name')