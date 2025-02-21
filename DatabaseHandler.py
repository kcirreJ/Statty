import psycopg2
class DatabaseHandler:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host, database=self.database, user=self.user, password=self.password
            )
            return True #connection successful
        except psycopg2.Error as e:
            print(f"Database Connection Error: {e}")
            return False #connection failed

    def create_table(self):
        if self.conn:
            cursor = self.conn.cursor()
            sql = """
            """
            self.conn.commit()
            cursor.close()

    def close(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")