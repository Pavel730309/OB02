class User:
    def __init__(self, user_id, name):
        self._user_id = user_id  # Защищенный атрибут
        self._name = name        # Защищенный атрибут
        self._access_level = 'user'  # Уровень доступа для обычных сотрудников

    # Геттеры для доступа к защищенным атрибутам
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    # Сеттеры для изменения защищенных атрибутов
    def set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'  # Уровень доступа для администраторов

    def get_access_level(self):
        return self._access_level

    def add_user(self, user_list, user):
        if self._access_level == 'admin':
            user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен в систему.")
        else:
            print("Недостаточно прав для добавления пользователя.")

    def remove_user(self, user_list, user_id):
        if self._access_level == 'admin':
            user_list = [user for user in user_list if user.get_user_id() != user_id]
            print(f"Пользователь с ID {user_id} удален из системы.")
        else:
            print("Недостаточно прав для удаления пользователя.")
        return user_list

# Пример использования
users = []

# Создание администратора
admin = Admin(user_id=1, name="Admin")

# Создание обычных пользователей
user1 = User(user_id=2, name="Сергей")
user2 = User(user_id=3, name="Тимур")

# Добавление пользователей
admin.add_user(users, user1)
admin.add_user(users, user2)

# Удаление пользователя
users = admin.remove_user(users, user_id=2)

# Вывод текущего списка пользователей
for user in users:
    print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")