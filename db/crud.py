from typing import Any, Type
from . import Base, Session
from sqlalchemy import select, delete


class CRUD:
    def __init__(self) -> None:
        self.session = Session()

    def items(self, model: Type[Any], limit: int = -1) -> list[Type[Any]]:
        query = select(model).limit(limit)
        result = []
        result.extend(self.session.scalars(query).all())
        return result

    def item(self, model: Type[Any], filter: Any) -> Type[Any] | None:
        query = select(model).filter(filter)
        return self.session.scalar(query)

    # TODO: ADD DELETE, CREATE, UPDATE


# if __name__ == "__main__":
#     crud = CRUD()
#     items = crud.item(model=Tour, filter=Tour.id == 15)
