import sqlite3

class User:
	def __init__(self, user_id: int, film: str | None = None):
		self.user_id = user_id
		self.film = film

class Database:
	def __init__(self):
		self.connection = sqlite3.connect("sqlite.db")
		self.cursor = self.connection.cursor()

	def close(self):
		self.connection.close()

	def get_user(self, user_id: int) -> User | None:
		query = "SELECT * FROM users WHERE id = ?"
		args = (user_id,)
		self.cursor.execute(query, args)
		row = self.cursor.fetchone()
		if row is None:
			return None

		return User(user_id=user_id, film=row[1])

	def create_user(self, user_id: int):
		query = "INSERT INTO users(id) VALUES (?)"
		args = (user_id,)
		self.cursor.execute(query, args)
		self.connection.commit()

	def set_city(self, user_id: int, film: str):
		query = "UPDATE users SET film= ? WHERE id = ?"
		args = (city, user_id)
		self.cursor.execute(query, args)
		self.connection.commit()
