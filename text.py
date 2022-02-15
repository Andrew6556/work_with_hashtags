from write_read_json import*
import re
import os

class Text:

    @staticmethod
    def output_of_the_marked_user_in_the_text(search_user):
        """Выводим все тексты,где упоминается данный пользователь"""
        reg_exp = fr'{search_user}\b'
        for mention_text in read_json_file('all_text.json'):
            if re.search(reg_exp, mention_text["text"]):
                return True

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
            for texts in read_json_file('all_text.json'):
                if re.search(r'#прог\w+',texts["text"], flags=re.IGNORECASE):
                    print(f'{texts["text"]}\n')
        else:
            return False

    def search_text_specific_user(self, search_user):
        for users in read_json_file('data_user_text.json'):
            if users["name"] == search_user:
                return True
                
        if users["name"] != search_user:
            return False

class TextInterface:

    def __init__(self, text):
        self.text = text

    def output_texts_with_a_hashtag(self, search):
        """Выводим ошибку при неправильном вводе хэштега"""
        if self.text.hashtag_search(search) == False:
            print('такого хэштега нету')

    def display_text_specific_user(self, search_user):
        """Выводим все текста найденного пользователя"""

        if self.text.search_text_specific_user(search_user) == True:
            for users in read_json_file('data_user_text.json'):
                if users["name"] == search_user:
                    print(users["text"])
        else:
            print('Error')

    def mention_of_user_in_the_text(self, search_user):
        """Вывод текстов с упоминанием"""
        
        if self.text.output_of_the_marked_user_in_the_text(search_user) == True:
            for mention_text in read_json_file('all_text.json'):
                if re.search(search_user, mention_text["text"]):
                    print(f'{mention_text["text"]}\n')
        