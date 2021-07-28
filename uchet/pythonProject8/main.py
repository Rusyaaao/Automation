import json
import sqlite3

database_name = 'sqlite_python.sqlite'
name_json = 'goods_schema.json'
sqlite_create_tables = 'sqlite_create_tables.sql'


def create_db_and_table():
    try:
        sqlite_connection = sqlite3.connect(database_name)
        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")

        with open(sqlite_create_tables, 'r') as sqlite_file:
            sql_script = sqlite_file.read()

        cursor.executescript(sql_script)
        print("Скрипт SQLite успешно выполнен")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")


def create_or_update_into_goods_shops_goods(location_and_quantity, id):
    conn = sqlite3.connect(database_name)
    cur = conn.cursor()

    for j in location_and_quantity:
        id_good = id
        location = j['location']
        amount = j['amount']
        lc = (id_good, location, amount)

        cur.execute(f"SELECT * FROM shops_goods WHERE id_good='{id_good}' AND location='{location}'")
        if len(cur.fetchall()) == 0:
            cur.execute("INSERT INTO shops_goods (id_good, location, amount) VALUES(?, ?, ?);", lc)
            conn.commit()
            print(f"Cоздан новый адрес с id товара = {id_good}")

        else:
            sqlite_update_query = f"UPDATE shops_goods set amount = ? WHERE id_good = ? AND location = ?"
            cur.execute(sqlite_update_query, (amount, id_good, location))
            conn.commit()
            print(f'Обновлено кол-во товара с id товара = {id_good} по адресу "{location}"')


def create_item_into_goods(id, name, width, height):
    conn = sqlite3.connect(database_name)
    cur = conn.cursor()

    # cur.execute("INSERT OR IGNORE  INTO goods VALUES(?, ?, ?, ?);", item)
    # conn.commit()
    # print(f"Найден товар с id = {id}")

    cur.execute(f"SELECT * FROM goods WHERE id='{id}' ")
    if len(cur.fetchall()) == 0:
        cur.execute("INSERT INTO goods VALUES(?, ?, ?, ?);", (id, name, width, height))
        conn.commit()
        print(f"Cоздан товар id = {id}")

    else:
        sqlite_update_query = f"""UPDATE goods SET `name` = ?, package_height = ?, package_width = ?  WHERE id = ?"""
        cur.execute(sqlite_update_query, (name, width, height, id))
        conn.commit()
        print(f'Обновлен товара с id {id}')
    return True


def valid(items):
    for i in items:
        id = i['id']
        width = i['package_params']['width']
        height = i['package_params']['height']
        location_and_quantity = i['location_and_quantity']

        if int(id) <= 0 or float(width) <= 0 or float(height) <= 0:
            print("Json parse item error")
            return False
        for j in location_and_quantity:
            amount = j['amount']
            if int(amount) < 0:
                print("Json parse amount error")
                return False
    return True


def append_into_db():
    with open(name_json) as f:
        templates = json.load(f)

    items = templates['examples']

    if not valid(items):
        return False

    for i in items:
        id = i['id']
        name = i['name']
        width = i['package_params']['width']
        height = i['package_params']['height']
        location_and_quantity = i['location_and_quantity']

        create_item_into_goods(id, name, width, height)
        create_or_update_into_goods_shops_goods(location_and_quantity, id)


try:
    create_db_and_table()
    append_into_db()
except:
    print("Error")
