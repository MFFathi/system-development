import psycopg2

from src.utils.Database import Database


def test_underlying_pg_connection():
    psycopg2.connect(
        "dbname=postgresql user=postgresql password=Postgresql host=db port=5432")


def test_database_connection():
    Database.connect()
    assert Database.connection is not None


def test_can_delete_all_tables():
    Database.DEBUG_delete_all_tables("DANGEROUSLY DELETE ALL TABLES")


def test_can_create_table():
    cur = Database.cursor()
    sql = """
        CREATE TABLE test_table
        (
            name text,
            age integer,
            PRIMARY KEY (name)
        );
    """
    cur.execute(sql)
    Database.commit()
    cur.execute("SELECT * FROM test_table;")
    assert cur.fetchall() == []


def test_can_insert_into_table():
    cur = Database.cursor()
    sql = "INSERT INTO test_table VALUES ('test', 1);"
    cur.execute(sql)
    Database.commit()
    cur.execute("SELECT * FROM test_table;")
    assert cur.fetchall() == [('test', 1)]


def test_can_close_connection():
    Database.close()
    assert Database.connection.closed == 1