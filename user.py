from write_read_json import*
import re
import os


class User:

    @staticmethod
    def user_authorization(name, password):
        for users in read_json_file('registered_users.json'):
            if users["name"] == name and users["name"] == password:
                True

            else:
                False

    def __init__(self, name):
        self.name = name
        
    def user_registration(self, password):
        data = read_json_file('registered_users.json')
        data.append({
            "name":self.name,
            "password":password
        })
        write_json_file('registered_users.json',data)

    def check_for_registered_user(self, user):
        """Проверяем зарегистрирован пользователь или нет"""
        user_mention = user[1:]
        for users in read_json_file('registered_users.json'):
            #так как польватель вводит @ то мы ее обрезаем для того чтоб сверить есть
            #ли данный пользователь в базе зарегистрированных
            if users["name"] == user_mention:
                return True

        if users["name"] != user_mention:
            print('Такой пользователь не зарегистрирован')

class UserInterface:
    def __init__(self, user):
        self.user = user
    
    def print_authorization(self,name, password):
        """Вывод результатов авторизации"""

        if self.user.user_authorization(name, password) == True:
            print('Авторизация прошла успешна')
        
        else:
            print('Ошибка вводе данных')

    



# text = User('name','2')
# text.user_registration('2','2')
# text.user_authorization('2',2)
# if self.name == name and self.password == password:
        #     print('авторизация прошла успешна')
        #     self._add_user_to_json(name)
        #     return True
        # else:
        #     return False 