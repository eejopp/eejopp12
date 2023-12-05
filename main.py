import sqlite3
import movieDB

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


    def __str__(self):#полиморфизм
        return self.username+" "+self.password
    def save(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                  (self.username, self.password))
        conn.commit()
        conn.close()

    @staticmethod
    def find(username):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        result = c.fetchone()
        conn.close()
        if result:
            return User(result[1], result[2])
        else:
            return None

def create_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
    conn.commit()
    conn.close()

def register():
    username = input("Введите имя пользователя: ")
    temp=User.find(username)
    if temp==None:
        password = input("Введите пароль: ")
        user = User(username, password)  # создание нового объекта
        user.save()  # обращаемся к методу save объекта user
        print("Регистрация успешна!")
    else:
        print("Пользователь с таким именем существует")


def login():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    user = User.find(username)
    if user and user.password == password:
        print("Авторизация успешна!")
        #пойти работать с MovieDB
        movieDB.MovieDB()
    else:
        print("Неверное имя пользователя или пароль")

create_table()

while True:
    choice = input("Выберите действие (1 - Регистрация, 2 - Авторизация, 3 - Выход): ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Неверный выбор")