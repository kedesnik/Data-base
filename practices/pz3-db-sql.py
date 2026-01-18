import sqlite3

# con = sqlite3.connect("films_db_.sqlite")
# cur = con.cursor()
# # Выполнение запроса и получение всех результатов
# result = cur.execute(f"""SELECT f.title, g.title FROM films f
#                      JOIN genres g ON f.genre = g.id
#                      WHERE duration > {90} AND g.title = 'ужасы' """).fetchall()
# # Вывод результатов на экран
# for elem in result:
#     print(elem)
# con.close()

# import sqlite3

# con = sqlite3.connect("films_db_.sqlite")
# cur = con.cursor()
# # Выполнение запроса и получение всех результатов
# result = cur.execute(f"""UPDATE films
#                      SET title = 'А теперь не смотрим'
#                      WHERE title = 'А теперь не смотри' """)
# con.commit()
# con.close()
# print('ok')

def Task1():
    con = sqlite3.connect("films_db_.sqlite")
    cur = con.cursor()

    result = cur.execute(f"""SELECT title FROM films
                                WHERE title LIKE  '%?' """).fetchall()

    for elem in result:
        print(elem[0])
    con.close()

def Task2():
    con = sqlite3.connect("films_db_.sqlite")
    cur = con.cursor()

    result = cur.execute(f"""SELECT f.title, g.title, duration FROM films f
                JOIN genres AS g ON f.genre = g.ID
                WHERE duration >= {60} AND g.title ='комедия' """).fetchall()

    for elem in result:
        print(elem)
    con.close()

def Task3():
    con = sqlite3.connect("films_db_.sqlite")
    cur = con.cursor()

    result = cur.execute(f"""SELECT f.title, g.title FROM films f
                JOIN genres AS g ON f.genre = g.ID
                WHERE f.title like '%Астерикс%' AND f.title NOT LIKE '%Обеликс%'""").fetchall()

    for elem in result:
        print(elem)
    con.close()

def Task4():
    con = sqlite3.connect("films_db_.sqlite")
    cur = con.cursor()

    action_f = cur.execute(f"""SELECT f.title, g.title, f.year FROM films f
        JOIN genres AS g ON f.genre = g.ID
        WHERE g.title = 'боевик' AND f.year BETWEEN 1995 AND 2007
        ORDER by f.title """).fetchall()

    horror_f = cur.execute(f"""SELECT f.title, g.title, f.year FROM films f
        JOIN genres AS g ON f.genre = g.ID
        WHERE g.title = 'ужасы' AND f.year BETWEEN 1995 AND 2007 
        ORDER by f.title""").fetchall()
    
    ac_hor_cnt = cur.execute(f"""SELECT COUNT(*) FROM films f
        JOIN genres AS g ON f.genre = g.ID
        WHERE g.title = 'боевик' OR g.title = 'ужасы'""").fetchall()
    
    ac_hor_cnt_crit = cur.execute(f"""SELECT COUNT(*) FROM films f
        JOIN genres AS g ON f.genre = g.ID
        WHERE (g.title = 'боевик' AND f.year BETWEEN 1995 AND 2007) 
        OR (g.title = 'ужасы' AND f.year BETWEEN 1995 AND 2007)""").fetchall()

    for title1,title2, year in action_f:
        print(f"{title1} ({title2}, {year})")
    for title1,title2, year in horror_f:
        print(f"{title1} ({title2}, {year})")
    print(f"Количество боевиков и ужасов всего: {ac_hor_cnt[0][0]}")
    print(f"Количество боевиков и ужасов, выпущенных с 1995 по 2007 года: {ac_hor_cnt_crit[0][0]}")
    con.close()

def Task5():
    def get_result(name):
        con = sqlite3.connect(name)
        cur = con.cursor()

        cur.execute(f"""UPDATE films
            SET duration = 42
            WHERE duration = ''""")
        con.commit()
        con.close()
        print("Готово.")

    get_result(input("Введите название файла базы данных: "))

def Task6():
    def get_result(name):
        con = sqlite3.connect(name)
        cur = con.cursor()

        cur.execute(f"""UPDATE films
            SET duration = duration / 3
            WHERE year = 1973""")
        con.commit()
        con.close()
        print("Готово.")

    get_result(input("Введите название файла базы данных: "))

def Task7():
    def get_result(name):
        con = sqlite3.connect(name)
        cur = con.cursor()

        cur.execute(f"""DELETE FROM films
            JOIN genres AS g ON f.genre = g.ID
            WHERE genre = 'фантастика' AND year < 2000 AND duration > 90""")
        con.commit()
        con.close()
        print("Готово.")

    get_result(input("Введите название файла базы данных: "))

def main():
    n = int(input("Номер задания: "))
    match n:
        case 1:
            Task1()
        case 2:
            Task2()
        case 3:
            Task3()
        case 4:
            Task4()
        case 5:
            Task5()
        case 6:
            Task6()
        case 7:
            Task7()

main()
