from io import StringIO

from api.psql import db
from api.psql.utils import copy_query_to_file
from flask import Response
from flask import current_app as app


@app.route("/patients.csv", methods=["GET"])
def serve_patients_csv():
    buf = StringIO()
    with db.getconn() as conn:
        copy_query_to_file("patient", buf, conn)
        buf.flush()  # Do we need this?
    res = Response(buf.getvalue(), status=200, mimetype="text/csv")
    res.headers.set("Content-Disposition", "attachment", filename="patients.csv")
    return res

@app.route("/questions.csv", methods=["GET"])
def get_questions_csv():
    buf = StringIO()
    with db.getconn() as conn:
        copy_query_to_file("question", buf, conn)
        buf.flush() 
    res = Response(buf.getvalue(), status=200, mimetype="text/csv")
    res.headers.set("Content-Disposition", "attachment", filename="questions.csv")
    return res



@app.route("/stations.csv", methods=["GET"])
def get_stations_csv():
    buf = StringIO()
    with db.getconn() as conn:
        copy_query_to_file("station", buf, conn)
        buf.flush() 
    res = Response(buf.getvalue(), status=200, mimetype="text/csv")
    res.headers.set("Content-Disposition", "attachment", filename="stations.csv")
    return res


@app.route("/answers.csv", methods=["GET"])
def get_answers_csv():
    buf = StringIO()
    with db.getconn() as conn:
        copy_query_to_file("answer", buf, conn)
        buf.flush() 
    res = Response(buf.getvalue(), status=200, mimetype="text/csv")
    res.headers.set("Content-Disposition", "attachment", filename="answers.csv")
    return res

@app.route("/types.csv", methods=["GET"])
def get_types_csv():
    buf = StringIO()
    with db.getconn() as conn:
        copy_query_to_file("type", buf, conn)
        buf.flush() 
    res = Response(buf.getvalue(), status=200, mimetype="text/csv")
    res.headers.set("Content-Disposition", "attachment", filename="types.csv")
    return res
