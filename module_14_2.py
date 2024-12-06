import sqlite3


conection = sqlite3.connect('not_telegram.db')
cursor = conection.cursor()

cursor.execute("""                          
CREATE TABLE IF NOT EXISTS Users_(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")

for i in range(10):
    cursor.execute('INSERT INTO Users_ (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{i+1}', f'example{i+1}@gmail.com', (i + 1) * 10, 1000))

for i in range(1,11,2):
    cursor.execute("UPDATE Users_ SET balance = ? WHERE username = ?", ("500", f"User{i}"))

for i in range(1,11,3):
    cursor.execute("DELETE FROM Users_  WHERE username = ?", (f"User{i}",))

cursor.execute("SELECT username, email, age, balance FROM Users_ WHERE age != ?", ("60",))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

cursor.execute("DELETE FROM Users_  WHERE id = ?", (6,))

cursor.execute("SELECT COUNT(*) FROM Users_")
total_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users_")
all_balance = cursor.fetchone()[0]

print(all_balance / total_users)

conection.commit()
conection.close()