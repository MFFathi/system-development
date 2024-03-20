import psycopg2


def test_underlying_pg_connection():
    psycopg2.connect(
        "dbname=postgres user=postgres password=postgres host=db port=5432")