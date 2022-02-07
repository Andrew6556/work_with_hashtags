from write_read_json import*
import re
import os

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def user_authorization(self, name, password):
        if self.name == name and self.password == password:
            print('авторизация прошла успешна')
            self._add_user_to_json(name)
        else:
            print('error')
        
    def _add_user_to_json(self, name):
        """
        Добавляем пользователя в json,
        где хранятся данные о всех зарегистрированных пользователей
        """
        data = read_json_file('registered_users.json')
        data.append({
            "name":name
        })
        write_json_file('registered_users.json',data)


class Text:
    def __init__(self, user):
        self.user = user
    
    def save_to_json(self, user, text):
        """
        Добавляем новый текст пользователя в json
        """

        if os.stat(f'data\data_user_text.json',).st_size:
            data = read_json_file('data_user_text.json')
            # если в файле уже присутсвуют какие-то данные, то к ним добавляем последующие данные
        else:
            # если в файле нет еще данных, то мы создаем список и потом добаляем в него данные пользователя
            data = []

        data.append({
            "name":user.name,
            "text":text
        })
        write_json_file('data_user_text.json', data)

    def hashtag_search(self, hashtag):
        "Осуществляем поиск хэштега в тексте"

        if re.match(r'#прог\w+', hashtag):
            for i in read_json_file('data.json'):
                if re.search(r'#прог\w+',i["text"], flags=re.IGNORECASE):
                    print(f'{i["text"]}\n')
        else:
            print('такого хэштега нету')

    def _output_of_the_marked_user_in_the_text(self, search_user):
        """Выводим все тексты где упоминается данный пользователь"""
        reg_exp = fr'{search_user}\b'
        for mention_text in read_json_file('data.json'):
            if re.search(reg_exp, mention_text["text"]):
                print(f'{mention_text["text"]}\n') 

    def check_for_registered_user(self, user):
        """Проверяем зарегистрирован пользователь или нет"""
        user_mention = user[1:]
        for users in read_json_file('registered_users.json'):
            #так как польватель вводит @ то мы ее обрезаем для того чтоб сверить есть
            #ли данный пользователь в базе зарегистрированных
            if users["name"] == user_mention:
                self._output_of_the_marked_user_in_the_text(user)
            
        if users["name"] != user_mention:
            print('Данный пользователь не зарегистрирован')

    def search_text_specific_user(self, search_user):
        for users in read_json_file('data_user_text.json'):
            if users["name"] == search_user:
                print(users["text"])
                
        if users["name"] != search_user:
            print('данный пользователь не найден')

print('Добро пожаловать в приложение\nПроцесс регистрации')

user = User(input('Введите ваше имя\n'),
        int(input('Напишите пароль(цифрами)\n')))

user.user_authorization(input('Введите ваше имя\n'),
                    int(input('Напишите пароль\n')))
text = Text(1)

while True:
    print("""
    У вас есть возможности:
    1.Добавить свой текст
    2.Поиск конкретных текстов по хэштегу(#)
    3.Найти все упоминание пользователя каком либо тексте(так @Ivan)
    4.Вывод всех текстов созданные этим пользователем (Введите имя пользоавтеля без @)
    5.Для выхода из программы напишите 
    """)  

    user_choice = int(input('Введите номер действия которое хотите сделать\n'))

    if user_choice == 1:
        add_text = input('ваш текст\n')
        text.add_text_to_json(user, add_text)
        print('текст успешно сохранился')

    elif user_choice == 2:
        user_hashtag = input('введите хэштег(он должен начанаться с #)\n')
        if user_hashtag.startswith('#'):
            text.hashtag_search(user_hashtag)
        else:
            print('ошибка вводе')
    
    elif user_choice == 3:
        user_hashtag = input('введите хэштег(он должен начанаться с @)\n')
        if user_hashtag.startswith('@'):
            text.check_for_registered_user(user_hashtag)
        else:
            print('ошибка вводе')
    
    elif user_choice == 4:
        user_name = input('введите имя пользователя\n')
        text.search_text_specific_user(user_name)

    elif user_choice == 5:
        print('вы вышли из программы')
        break