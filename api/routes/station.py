from flask import current_app as app
from flask import request

from api.psql import db


@app.route("/get_availability", methods=["GET"])
def get_station_availability():
    with db.getconn() as connection:
        cursor = connection.cursor()

        postgres_select_query = """SELECT station_name, availability FROM station"""
        cursor.execute(postgres_select_query)
        connection.commit()

        results = cursor.fetchall()
        results = dict(results)

        print("Successful query of station table.")
        print(results)

        # {'Tobacco Questionnare': True,
        # 'Anemia Questionnare': True,
        # 'BMI (Underweight measurement)': True,
        # 'Haemoglobin (Anemia measurement)': True,
        # 'Post campaign survey': True,
        # 'Registration': False}

        return results


@app.route("/set_availability", methods=["POST"])
def set_availability():
    with db.getconn() as connection:
        cursor = connection.cursor()

        data = request.get_json()
        print(data)
        for key, value in data.items():
            postgres_select_query = (
                """ UPDATE station SET availability = %s WHERE station_name = %s"""
            )
            record_to_select = (
                value,
                key,
            )
            cursor.execute(postgres_select_query, record_to_select)
            connection.commit()
            print("Availability of {} station set to {}".format(key, str(value)))
            print("ok")

        return "Availability of {} station set to {}".format(key, str(value))
