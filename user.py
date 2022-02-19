from write_read_json import*



class User:

    @staticmethod
    def user_authorization(name, password):
        for users in read_json_file('registered_users.json'):
            if users["name"] == name and users["password"] == password:
                return True
            
            else:
                continue
                

    def __init__(self, name):
        self.name = name
        
    def user_registration(self, password):
        data = read_json_file('registered_users.json')
        data.append({
            "name":self.name,
            "password":password
        })
        write_json_file('registered_users.json',data)
        
        user = User(self.name)
        return user

    def check_for_registered_user(self, user):
        """Проверяем зарегистрирован пользователь или нет"""
        if user.startswith('@'):
            user_mention = user[1:]
            for users in read_json_file('registered_users.json'):
                #так как польватель вводит @ то мы ее обрезаем для того чтоб сверить есть
                #ли данный пользователь в базе зарегистрированных
                if users["name"] == user_mention:
                    return True

            if users["name"] != user_mention:
                return False
                
        else:
            return 'error'
            # print('ошибка вводе')

class UserInterface:
    def __init__(self, user):
        self.user = user
    
    def registered_int(self, password):
        if self.user.user_registration(password):
            print('Регистрация прошла успешно')

    def print_authorization(self, name, password):
        """Вывод результатов авторизации"""

        if self.user.user_authorization(name, password) == True:
            print('Авторизация прошла успешна')
            return True
        else:
            print('Ошибка вводе данных')

    def int_check_for_registered_user(self, user):
        """Вывод всех принтов при регистрации"""

        if self.user.check_for_registered_user(user) == True:
            return True
        
        elif self.user.check_for_registered_user(user) == False:
            print('Такой пользователь не зарегистрирован')
        
        elif self.user.check_for_registered_user(user) == 'error':
            print('ошибка вводе')