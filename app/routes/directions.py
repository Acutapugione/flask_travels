from .. import app
from flask import render_template
from db import Direction, CRUD

crud = CRUD()


@app.get("/directions")
def direction_list():
    directions = crud.items(Direction)
    return render_template("index.html", title="Directions", directions=directions)


@app.get("/directions/<int:id>")
def direction_item(id: int):
    direction = crud.item(Direction, Direction.id == id)
    return render_template("detail.html", title=direction.title, item=direction)
