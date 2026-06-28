# Практическая 15

#Приложение БЮРО ПО ТРУДОУСТРОЙСТВУ для некоторой организации.
#БД должна содержать таблицу Работник со следующей структурой записи:
#фамилия, имя, отчество, возраст, пол, профессия, стаж работы.

import sqlite3

conn = sqlite3.connect("job_bureau.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS worker (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name TEXT,
    first_name TEXT,
    sur_name TEXT,
    age INTEGER,
    gender TEXT,
    profession TEXT,
    experience INTEGER
)
""")
conn.commit()

cursor.execute("SELECT COUNT(*) FROM worker")
if cursor.fetchone()[0] == 0:
    initial_workers = [
        ('Иванов', 'Иван', 'Иванович', 25, 'М', 'Программист', 3),
        ('Петров', 'Петр', 'Петрович', 40, 'М', 'Инженер', 15),
        ('Сидорова', 'Анна', 'Сергеевна', 30, 'Ж', 'Бухгалтер', 7),
        ('Кузнецов', 'Алексей', 'Николаевич', 22, 'М', 'Программист', 1),
        ('Смирнова', 'Елена', 'Викторовна', 35, 'Ж', 'Дизайнер', 10),
        ('Попов', 'Сергей', 'Михайлович', 50, 'М', 'Директор', 25),
        ('Васильева', 'Ольга', 'Игоревна', 28, 'Ж', 'Маркетолог', 4),
        ('Соколов', 'Дмитрий', 'Андреевич', 45, 'М', 'Инженер', 20),
        ('Новикова', 'Мария', 'Алексеевна', 33, 'Ж', 'Бухгалтер', 9),
        ('Морозов', 'Артем', 'Павлович', 26, 'М', 'Дизайнер', 2)
    ]
    cursor.executemany("""
    INSERT INTO worker (last_name, first_name, sur_name, age, gender, profession, experience)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, initial_workers)
    conn.commit()

while True:
    print("\n--- МЕНЮ БЮРО ПО ТРУДОУСТРОЙСТВУ ---")
    print("1. Показать всех работников")
    print("2. Добавить нового работника")
    print("3. Поиск работников (3 варианта)")
    print("4. Редактировать данные (3 варианта)")
    print("5. Удалить работников (3 варианта)")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        cursor.execute("SELECT * FROM worker")
        rows = cursor.fetchall()
        print("\nСписок всех работников:")
        for r in rows:
            print(f"ID {r[0]}: {r[1]} {r[2]} {r[3]}, Возраст: {r[4]}, Пол: {r[5]}, Профессия: {r[6]}, Стаж: {r[7]} лет")

    elif choice == "2":
        print("\nВвод данных нового работника:")
        try:
            ln = input("Фамилия: ")
            fn = input("Имя: ")
            sn = input("Отчество: ")
            age = int(input("Возраст (число): "))
            gender = input("Пол (М/Ж): ")
            prof = input("Профессия: ")
            exp = int(input("Стаж работы (число): "))

            cursor.execute("""
            INSERT INTO worker (last_name, first_name, sur_name, age, gender, profession, experience)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (ln, fn, sn, age, gender, prof, exp))
            conn.commit()
            print("Работник успешно добавлен!")
        except ValueError:
            print("Ошибка: Возраст и Стаж должны быть числами!")

    elif choice == "3":
        print("\nВарианты поиска:")
        print("  1 - Поиск по профессии")
        print("  2 - Поиск по минимальному стажу")
        print("  3 - Поиск женщин старше определенного возраста")
        sub_choice = input("Выберите вариант поиска: ")

        if sub_choice == "1":
            prof = input("Введите профессию (например, Программист): ")
            cursor.execute("SELECT * FROM worker WHERE profession = ?", (prof,))
        elif sub_choice == "2":
            try:
                min_exp = int(input("Введите минимальный стаж: "))
                cursor.execute("SELECT * FROM worker WHERE experience >= ?", (min_exp,))
            except ValueError:
                print("Нужно ввести число!")
                continue
        elif sub_choice == "3":
            try:
                min_age = int(input("Введите возраст: "))
                cursor.execute("SELECT * FROM worker WHERE gender = 'Ж' AND age > ?", (min_age,))
            except ValueError:
                print("Нужно ввести число!")
                continue
        else:
            print("Неверный вариант")
            continue

        results = cursor.fetchall()
        print("\nРезультаты поиска:")
        for r in results:
            print(f"ID {r[0]}: {r[1]} {r[2]}. - {r[6]}, Стаж: {r[7]} л., Возраст: {r[4]}")

    elif choice == "4":
        print("\nВарианты редактирования:")
        print("  1 - Изменить профессию по ID работника")
        print("  2 - Увеличить стаж всем работникам на 1 год")
        print("  3 - Обновить фамилию по ID")
        sub_choice = input("Выберите вариант изменения: ")

        try:
            if sub_choice == "1":
                w_id = int(input("Введите ID работника: "))
                new_prof = input("Введите новую профессию: ")

                cursor.execute("UPDATE worker SET profession = ? WHERE id = ?", (new_prof, w_id))
            elif sub_choice == "2":
                print("Увеличиваем стаж всем на 1 год...")

                cursor.execute("UPDATE worker SET experience = experience + 1")
            elif sub_choice == "3":
                w_id = int(input("Введите ID работника: "))
                new_ln = input("Введите новую фамилию: ")

                cursor.execute("UPDATE worker SET last_name = ? WHERE id = ?", (new_ln, w_id))
            else:
                print("Неверный вариант")
                continue

            conn.commit()
            print("База успешно обновлена!")
        except ValueError:
            print("Ошибка ввода данных!")

    elif choice == "5":
        print("\nВарианты удаления:")
        print("  1 - Удалить конкретного работника по ID")
        print("  2 - Удалить всех работников с нулевым стажем")
        print("  3 - Удалить работников по конкретной профессии")
        sub_choice = input("Выберите вариант удаления: ")

        try:
            if sub_choice == "1":
                w_id = int(input("Введите ID для удаления: "))

                cursor.execute("DELETE FROM worker WHERE id = ?", (w_id,))
            elif sub_choice == "2":

                cursor.execute("DELETE FROM worker WHERE experience = 0")
            elif sub_choice == "3":
                prof = input("Какую профессию полностью удалить из базы?: ")

                cursor.execute("DELETE FROM worker WHERE profession = ?", (prof,))
            else:
                print("Неверный вариант")
                continue

            conn.commit()
            print("Удаление выполнено!")
        except ValueError:
            print("Ошибка ввода!")

    elif choice == "0":
        print("Выход из программы.")
        break
    else:
        print("Неверный пункт меню!")

conn.close()