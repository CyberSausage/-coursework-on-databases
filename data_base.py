import sqlite3


connection = sqlite3.connect("Курсовая_DB.db")
cursor = connection.cursor()

def crate_table_Bilets():
    cursor.execute('''create table Билеты 
    (id_билета text primary key,
    Номер_билета text,
    Цена_билета money,
    id_рейса text,
    id_пассажира text)''')

def create_table_Ekipaz():
    cursor.execute('''create table Экипаж
    (id_экипажа text primary key,
    Командир text,
    Помошник_командира text,
    КолВо_экипажа integer)''')

def create_table_Inf_Pass():
    cursor.execute('''create table Пассажиры
    (id_пассажира text primary key,
    Фамилия text,
    Имя text,
    Статус text)''')

def create_table_Reis():
    cursor.execute('''create table Рейсы
    (id_рейса text primary key,
    Номер_рейса text,
    ПунктОтправления text,
    ПунктПрибытия text,
    ВремяОтправления text,
    ВремяПрибытия text,
    КолВо_мест integer,
    Цена_билета money,
    Перевозчик text,
    id_экипажа text)''')

def create_table_Zaderzh_reis():
    cursor.execute('''create table Задержанные_рейсы
    (id_рейса text primary key,
    Причина задержки text,
    Время задержки text)''')

def create_stype_table():
    cursor.execute('''create table Style
    (key_word text,
     styleSheet text,
     contentTopBg text,
     leftMenuBg text,
     bottomBar text,
     bgApp text,
     stackedWidget text,
     btn_start_aktive text,
     btn_pilot text,
     btn_people text,
     btn_reis text,
     btn_reis_stop text,
     btn_qwery text,
     theme_mod text,
     add_row text,
     update_row text,
     delete_row text,
     onn bool)''')


def insert():
    cursor.execute('''select * from Стили where key_word="dark"''')
    select = cursor.fetchone()
    cursor.execute(f'''insert into Style (key_word, styleSheet, contentTopBg, leftMenuBg,
    bottomBar, bgApp, stackedWidget, btn_start_aktive, btn_pilot, btn_people, btn_reis,
    btn_reis_stop, btn_qwery, theme_mod, add_row, update_row, delete_row, onn) values ("{select[0]}",
    "1", "{select[1]}", "{select[2]}", "{select[3]}", "{select[4]}", "{select[5]}", "{select[6]}", "{select[7]}",
    "{select[8]}", "{select[9]}", "{select[10]}", "{select[11]}", "{select[12]}", "{select[13]}", "{select[14]}",
    "{select[15]}", "{select[16]}")''')
    connection.commit()

def insert_Style():
    cursor.execute('''update Style set leftMenuBg='
' where key_word="dark"''')
    connection.commit()
