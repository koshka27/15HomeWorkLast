import sqlite3
from flask import Flask, jsonify
import query

app = Flask(__name__)

DATABASE_PATH = "animal.db"


def serialize_row(row: sqlite3.Row):
    return {key: row[key] for key in row.keys()}


@app.route('/<animal_id>/')
def get_animal_id(animal_id):

    con: sqlite3.Connection = app.config["db"]  # sqlite.Connection - позволяет иметь подсказку pycharm
    cursor = con.cursor()

    cursor.execute(query.GET_ANIMAL_ID_QUERY, (animal_id,))
    row = cursor.fetchone()
    cursor.close()

    return jsonify(serialize_row(row))


if __name__ == "__main__":
    connection = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    app.config["db"] = connection
    try:
        app.run()
    except KeyboardInterrupt:
        connection.close()