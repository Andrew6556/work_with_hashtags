from write_read_json import*
import re
import os
from user import User

class Text:

    @staticmethod
    def output_of_the_marked_user_in_the_text(search_user):
        """Выводим все тексты где упоминается данный пользователь"""

        reg_exp = fr'{search_user}\b'
        for mention_text in read_json_file('data.json'):
            if re.search(reg_exp, mention_text["text"]):
                print(f'{mention_text["text"]}\n') 

    def __init__(self, user):
        self.user = user
    
    def save_to_json(self, text):
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
            "name":self.user.name,
            "text":text
        })
        write_json_file('data_user_text.json', data)

    def hashtag_search(self, hashtag):
        "Осуществляем поиск хэштега в тексте"

        if re.match(r'#прог\w+', hashtag):
            for i in read_json_file('data.json'):
                if re.search(r'#прог\w+',i["text"], flags=re.IGNORECASE):
                    return True
        else:
            return False
            
    def check_for_registered_user(self,name_user):
        """Проверяем зарегистрирован пользователь или нет"""
        if self.user.check_for_registered_user(name_user) == True:
            self.output_of_the_marked_user_in_the_text(name_user)


    def search_text_specific_user(self, search_user):
        for users in read_json_file('data_user_text.json'):
            if users["name"] == search_user:
                print(users["text"])
                
        if users["name"] != search_user:
            print('данный пользователь не найден')

class TextInterface:

    def __init__(self, text):
        self.text = text

    def output_of_the_found_hashtag(self, search):
        """Выводим текста с найденным хэштегом"""

        if self.text.hashtag_search(search) == True:
            for texts in read_json_file('data.json'):
                if re.search(r'#прог\w+',texts["text"], flags=re.IGNORECASE):
                    print(f'{texts["text"]}\n')
        else:
            print('такого хэштега нету')

user = User('name')
text = Text(user)
int_text = TextInterface(text)
int_text.output_of_the_found_hashtag('#прога')
# text.check_for_registered_user("@ivan")

