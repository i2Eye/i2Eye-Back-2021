from flask import current_app as app
from psycopg2.pool import ThreadedConnectionPool

# Create a connection pool.
db = ThreadedConnectionPool(5, 20, app.config["DB_CONN_STRING"])
