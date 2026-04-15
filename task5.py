import sqlite3

def manage_animal_kingdom():
    connection = sqlite3.connect('AnimalKingdom.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Animals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            animal_type TEXT NOT NULL
        )
    ''')

    animals_data = [
        ("Лев", "Ссавець"),
        ("Крокодил", "Плазун"),
        ("Орел", "Птах"),
        ("Морська черепаха", "Плазун"),
        ("Мавпа", "Ссавець")
    ]
    
    cursor.executemany('INSERT INTO Animals (name, animal_type) VALUES (?, ?)', animals_data)
    connection.commit()
    print("--- Дані успішно вставлено ---")

    cursor.execute('UPDATE Animals SET name = ? WHERE name = ?', ("Сокіл", "Орел"))
    connection.commit()
    print("--- Назву 'Орел' змінено на 'Сокіл' ---")

    print("\nЗвірі типу 'Ссавець':")
    cursor.execute('SELECT * FROM Animals WHERE animal_type = ?', ("Ссавець",))
    mammals = cursor.fetchall()
    for animal in mammals:
        print(f"ID: {animal[0]}, Назва: {animal[1]}, Тип: {animal[2]}")

    print("\nВсі записи в таблиці Animals:")
    cursor.execute('SELECT * FROM Animals')
    all_animals = cursor.fetchall()
    for animal in all_animals:
        print(f"ID: {animal[0]} | Назва: {animal[1]} | Тип: {animal[2]}")

    connection.close()

if __name__ == "__main__":
    manage_animal_kingdom()
