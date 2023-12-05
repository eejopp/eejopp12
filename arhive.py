import sqlite3
conn=sqlite3.connect('example.db')
cursor=conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS passangers (id INTEGER PRIMARY KEY AUTOINCREMENT, passanger_id INTEGER NOT NULL, Surname NOT NULL, Name_ NOT NULL, Patronymic NOT NULL, Passport_series NOT NULL, Passport_number NOT NULL, Date_of_birth NOT NULL, Gender NOT NULL, Contact_details NOT NULL)')
#cursor.execute('DROP TABLE IF EXISTS users')

cursor.execute('CREATE TABLE IF NOT EXISTS Airline (id INTEGER PRIMARY KEY, Airline_id INTEGER NOT NULL, Title NOT NULL, Code NOT NULL, Address NOT NULL, Contact_details NOT NULL)')

cursor.execute('CREATE TABLE IF NOT EXISTS Flight (id INTEGER PRIMARY KEY, Flight_id INTEGER NOT NULL, Number NOT NULL, Departure_airport NOT NULL, Departure_city NOT NULL, Arrival_airport NOT NULL)')

cursor.execute('CREATE TABLE IF NOT EXISTS Date_ (id INTEGER PRIMARY KEY, Date__id INTEGER NOT NULL, Departure_date NOT NULL, DepartureDate NOT NULL, Boarding_date NOT NULL)')

cursor.execute('CREATE TABLE IF NOT EXISTS Airline_sales_deparment (id INTEGER PRIMARY KEY, Airline_sales_deparment_id INTEGER NOT NULL,)')