import json
clients = []

def load_data():
    try:
        with open("clients.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data():
    with open("clients.json", "w") as f:
        json.dump(clients, f, indent=4)

def menu():
    print("Выберите действие\n",
          "1 - Добавить клиента\n",
          "2 - Показать всех клиентов\n",
          "3 - Поиск клиентов\n",
          "4 - Удалить клиента")
    return input("Выбор: ")

def output():
    print("=== Список клиентов ===")
    for client in clients:
        print(f"№:{clients.index(client)}, {client['name']}, {client['age']}, {client['geo']}, {client['food']}")

def add():
    print("+++ Добавление клиента +++")
    name = input("Введите имя: ")
    age = input("Введите возраст: ")
    geo = input("Введите город проживания: ")
    food = input("Заказанное блюдо: ")
    clients.append({
        "name": name,
        "age": age,
        "geo": geo,
        "food": food
    })
    save_data()

def delete_element():
    id = input("--- Удаление клиента ---\nПосле удаления клиента, номера у некоторых клиентов может измениться! Проверяйте номер перед удалением\n"
                   "Введите номер клиента для удаления: ")
    if id.isdigit():
        try:
            clients.pop(int(id))
            save_data()
            print("Клиент удален")
        except IndexError:
            print("🚫Ошибка: введенного номера не существует")
    else:
        print("🚫Ошибка: введите номер (номер является целым числом)")

def search_fields(field, value):
    value = value.lower()
    found = False

    for client in clients:
        client_value = client[field]

        if field == "age":
            if client_value == value:
                print(f" №:{clients.index(client)}, {client['name']}, {client['age']}, {client['geo']}, {client['food']}")
                found = True
        else:
            if client_value.lower().startswith(value):
                print(f" №:{clients.index(client)}, {client['name']}, {client['age']}, {client['geo']}, {client['food']}")
                found = True
    if not found:
        print("⚠️Ничего не найдено")

def search():
    print("### Поиск клиента ###")
    choose = input("1 - По имени\n"
                   "2 - По возрасту\n"
                   "3 - По городу\n"
                   "4 - По блюдам\n")
    fields = {
        "1": "name",
        "2": "age",
        "3": "geo",
        "4": "food"
    }
    if choose not in fields:
        print("🚫Ошибка выбора")
        return

    value = input("Введите значение для поиска: ")
    print("⬇ ⬇ ⬇")
    search_fields(fields[choose], value)

clients = load_data() # В ЭТОЙ ПЕРЕМЕННОЙ ТЕКУЩИЙ json СПИСОК С СЛОВАРЯМИ, для изменений в файле, изменять этот список
while True:
    move = menu()

    if move not in ["1", "2", "3", "4"]:
        print("Ошибка: некорректный выбор")
        continue

    if move == "1":
        add()
    elif move == "2":
        output()
    elif move == "3":
        search()
    elif move == "4":
        delete_element()
    print("------------------------")
a = 1