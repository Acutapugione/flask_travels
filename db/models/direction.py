from typing import List
from .. import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Direction(Base):
    __tablename__ = "directions"
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    title: Mapped[str]
    sub_title: Mapped[str]
    description: Mapped[str]
    tours: Mapped[List["Tour"]] = relationship(back_populates="direction", init=False)
