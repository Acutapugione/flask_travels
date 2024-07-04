from sqlalchemy import create_engine
from sqlalchemy.orm import (
    MappedAsDataclass,
    DeclarativeBase,
    scoped_session,
    sessionmaker,
)


class Base(MappedAsDataclass, DeclarativeBase):
    pass


from .models import Tour, Direction

engine = create_engine("sqlite:///my_db.db", echo=True)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


from .crud import CRUD


def migrate():
    session = Session()

    japan_direction = Direction("Японія", "підтекст", "опис")
    japan_tour = Tour(
        "Квітучі сакури",
        4,
        18,
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Emperor_Jimmu.jpg/800px-Emperor_Jimmu.jpg",
        "Опис туру",
        "Японія",
        japan_direction,
    )
    japan_tour2 = Tour(
        "Квітучі сакури",
        4,
        18,
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Emperor_Jimmu.jpg/800px-Emperor_Jimmu.jpg",
        "Опис туру",
        "Японія",
        japan_direction,
    )
    session.add(japan_direction)
    session.commit()


migrate()
