import sqlite3


class UserDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        # Create the table if it doesn't exist
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT
                )
            ''')
            conn.commit()

    def register(self, username, password):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (username, password) VALUES (?, ?)
            ''', (username, password))
            conn.commit()

    def get_user(self, username):
        self.cursor.execute('''
            SELECT * FROM users WHERE username = ?
        ''', (username,))
        return self.cursor.fetchone()

    def update_password(self, username, new_password):
        self.cursor.execute('''
            UPDATE users SET password = ? WHERE username = ?
        ''', (new_password, username))
        self.conn.commit()

    def delete_user(self, username):
        self.cursor.execute('''
            DELETE FROM users WHERE username = ?
        ''', (username,))
        self.conn.commit()
