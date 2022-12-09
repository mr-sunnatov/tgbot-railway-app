import sqlite3



def preparate():
  connect = sqlite3.connect('db.sqlite3')
  cursor = connect.cursor()
  cursor.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, msg TEXT NOT NULL, ans TEXT NOT NULL);")
  connect.commit()


def get_message(msg):
  connect = sqlite3.connect('db.sqlite3')
  connect.row_factory = sqlite3.Row
  cursor = connect.cursor()
  cursor.execute('SELECT * FROM messages WHERE msg LIKE ? ORDER BY random() LIMIT 1;', ("%" + msg + "%",))

  return cursor.fetchone()

def add_message(msg, ans):
  connect = sqlite3.connect('db.sqlite3')
  cursor = connect.cursor()
  cursor.execute('INSERT INTO messages(msg, ans) VALUES (?, ?)', (msg, ans))
  connect.commit()
