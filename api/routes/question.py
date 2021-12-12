import json

import psycopg2
from flask import current_app as app

from api.psql import db


@app.route("/get_questions", methods=["GET"])
def get_all_questions():
    with db.getconn() as connection:
        cursor = connection.cursor()
        cursor2 = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor3 = connection.cursor()
        postgres_select_query = """ SELECT station_id FROM station"""
        cursor.execute(postgres_select_query)
        connection.commit()
        station_id_list = cursor.fetchall()
        print(station_id_list)
        results = {}
        for i in station_id_list:
            (station_id,) = i
            postgres_select_query = """SELECT question_id, question, type_id FROM question WHERE station_id = {0}""".format(
                station_id
            )
            postgres_select_query2 = (
                """SELECT station_name FROM station WHERE station_id = {0}""".format(
                    station_id
                )
            )
            cursor3.execute(postgres_select_query2)
            (station_name,) = cursor3.fetchall()[0]
            cursor2.execute(postgres_select_query)
            connection.commit()

            results.update({station_name: cursor2.fetchall()})
            # print(results)
            print("Successful query of question table.")
        return json.dumps(results)

    # ^ {"Registration": [
    #     {"question_id": 1, "question": "Name", "type_id": 1},
    #     {"question_id": 2, "question": "Gender", "type_id": 2},
    #     {"question_id": 3, "question": "Age", "type_id": 3},
    #     {"question_id": 4, "question": "Birthday", "type_id": 4}
    #     ]
    # }
