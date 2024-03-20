import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from .env import get_env


class Database:
    connection: psycopg2.extensions.connection

    @classmethod
    def connect(cls) -> None:
        """ 
        Connect to database as defined in env
        Should be run once and only once
        """

        cls.host = "db"
        cls.port = get_env("DB_PORT")
        cls.dbname = get_env("DB_NAME")
        cls.user = get_env("DB_USER")
        cls.password = get_env("DB_PASSWORD")

        print(f"Connecting to database on {cls.host}:{cls.port}")
        cls._verify_db_exists()

    @classmethod
    def cursor(cls) -> psycopg2.extensions.cursor:
        return cls.connection.cursor()

    @classmethod
    def commit(cls):
        cls.connection.commit()

    @classmethod
    def close(cls):
        cls.connection.close()

    @classmethod
    def DEBUG_delete_all_tables(cls, verify: str):
        """
        Delete all tables in database
        verify must be "DANGEROUSLY DELETE ALL TABLES"
        """

        if verify != "DANGEROUSLY DELETE ALL TABLES":
            raise Exception("You must verify that you want to delete all tables \
                            in the database by passing the string 'DANGEROUSLY DELETE ALL TABLES'  \
                            as the first argument to this function")

        cur = cls.cursor()
        cur.execute("DROP SCHEMA public CASCADE;")
        cur.execute("CREATE SCHEMA public;")
        cur.execute("GRANT ALL ON SCHEMA public TO postgres;")
        cur.execute("GRANT ALL ON SCHEMA public TO public;")
        cls.commit()

    @classmethod
    def _create_db_connection(cls, dbname: str) -> None:
        """
        Create a database connection to given dbname
        Sets that database to cls.connection
        """

        cls.connection = psycopg2.connect(
            dbname=dbname,
            user=cls.user,
            password=cls.password,
            host=cls.host,
            port=cls.port
        )

    @classmethod
    def _verify_db_exists(cls) -> bool:
        """
        Check if database defined by cls.dbname exists and create it if it doesn't
        """

        dbname = cls.dbname
        cls._create_db_connection("postgres")
        cur = cls.cursor()

        cur.execute("SELECT datname FROM pg_database;")
        all_databases = cur.fetchall()

        if (dbname,) not in all_databases:
            print(f"Database {dbname} does not exist. Creating it now...")
            cls.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur.execute("create database "+dbname+";")
            cls.commit()
            print("Database created successfully")

        cls.close()

        cls._create_db_connection(cls.dbname)