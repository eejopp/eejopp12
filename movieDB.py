import sqlite3

class Movie:
    def __init__(self, title, genre, year, director):
        self.title = title
        self.genre = genre
        self.year = year
        self.director = director

    def __str__(self):
        return self.title+" "+self.genre+" "+self.year+" "+self.director
    def save(self):
        conn = sqlite3.connect('movies.db')
        c = conn.cursor()
        c.execute("INSERT INTO movies (title, genre, year, director) VALUES (?, ?, ?, ?)",
                  (self.title, self.genre, self.year, self.director))
        conn.commit()
        conn.close()

    @staticmethod
    def find(title):
        conn = sqlite3.connect('movies.db')
        c = conn.cursor()
        c.execute("SELECT * FROM movies WHERE title=?", (title,))
        result = c.fetchone()
        conn.close()
        if result:
            return Movie(result[1], result[2], result[3], result[4])
        else:
            return None

    @staticmethod
    def display_all():
        conn = sqlite3.connect('movies.db')
        c = conn.cursor()
        c.execute("SELECT * FROM movies")
        movies = c.fetchall()
        conn.close()
        if movies:
            for movie in movies:
                print("ID:",movie[0])
                print("Название: ", movie[1])
                print("Жанр: ", movie[2])
                print("Год создания: ", movie[3])
                print("Режиссер: ", movie[4])
                print("--------------------")
        else:
            print("База данных пуста")

def create_table():
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, genre TEXT, year INTEGER, director TEXT)")
    conn.commit()
    conn.close()

def add_movie():
    title = input("Введите название фильма: ")
    temp=Movie.find(title)
    if (temp==None):
        genre = input("Введите жанр фильма: ")
        f=1
        while f==1:
            try:#Блок перехвата ошибок (исключительные ситуации)
                year = int(input("Введите год создания фильма: "))
                if (year>2024 or year<1800):
                    f=1
                f=0
            except:#если ошибка произошла, то переход в блок excep
                print("Не правильно введен год")
                f=1


        director = input("Введите режиссера фильма: ")
        movie = Movie(title, genre, year, director)
        movie.save()
        print("Фильм успешно добавлен!")
    else:
        print("Такой фильм уже добавлен")

def search_movie():
    title = input("Введите название фильма: ")
    movie = Movie.find(title)
    if movie:
        #print("ID: ",movie.id)
        print("Название: ", movie.title)
        print("Жанр: ", movie.genre)
        print("Год создания: ", movie.year)
        print("Режиссер: ", movie.director)
    else:
        print("Фильм не найден")

def display_movies():
    Movie.display_all()

def MovieDB():
    create_table()

    while True:
        choice = input("Выберите действие (1 - Добавить фильм, 2 - Поиск фильма, 3 - Вывести базу данных, 4 - Выход): ")
        if choice == "1":
            add_movie()
        elif choice == "2":
            search_movie()
        elif choice == "3":
            display_movies()
        elif choice == "4":
            exit(0)
        else:
            print("Неверный выбор")

#MovieDB()