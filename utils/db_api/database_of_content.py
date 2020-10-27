import sqlite3


class DataBaseOfContent:
    def __init__(self, path_to_db="data/content.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        data = None
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_content(self):
        sql = """
        CREATE TABLE Content(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        name_of_content VARCHAR(255) NOT NULL,
        overview_of_content TEXT NOT NULL,
        picture TEXT
        );
        """
        self.execute(sql, commit=True)

    def add_content(self, name_of_content: str, overview_of_content: str, picture: str):
        sql = "INSERT INTO Content(name_of_content, overview_of_content, picture) VALUES(?, ?, ?)"
        parameters = (name_of_content, overview_of_content, picture)
        self.execute(sql, parameters=parameters, commit=True)

    def select_all_content(self):
        sql = "SELECT * FROM Content"
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND".join([
            f"{item}= ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def select_content(self, **kwargs):
        sql = "SELECT * FROM Content WHERE name = ?"
        sql, parameters = self.format_args(sql, kwargs)
        self.execute(sql, parameters, fetchone=True)

    def random_serial_from_db(self):
        sql = "SELECT * FROM Content ORDER BY RANDOM() LIMIT 1"
        return self.execute(sql, fetchone=True)

    def count_content(self):
        return self.execute("SELECT COUNT(*) FROM Content;", fetchone=True)


def logger(statement):
    print(f"""
=====================================================================
Executing:
{statement}
=====================================================================
""")
