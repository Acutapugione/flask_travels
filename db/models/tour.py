from .. import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class Tour(Base):
    __tablename__ = "tours"
    id: Mapped[int] = mapped_column(primary_key=True, init=False)

    title: Mapped[str]
    stars: Mapped[int]
    time: Mapped[int]
    img: Mapped[str]
    description: Mapped[str]
    country: Mapped[str]

    direction_id: Mapped[int] = mapped_column(ForeignKey("directions.id"), init=False)
    direction: Mapped["Direction"] = relationship(back_populates="tours")
