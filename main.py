from user import User,UserInterface
from text import Text,TextInterface

print('Добро пожаловать в приложение\nПроцесс регистрации')
user_name = input('Введите ваш имя\n')
password = input('Введите ваш пароль\n')

user = User(user_name,password)
user_interface = UserInterface(user)
text = Text(user)
int_text = TextInterface(text)

while True:
    authorization_name = input('Введите ваше Имя при регистрации\n')
    authorization_password = input('Введите ваш Пароль при регистрации\n')
    if user_interface.print_authorization(authorization_name, authorization_password) == True:
        break


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
        text.save_to_json(user, add_text)
        print('текст успешно сохранился')

    elif user_choice == 2:
        user_hashtag = input('введите хэштег(он должен начанаться с #)\n')
        if user_hashtag.startswith('#'):
            int_text.output_texts_with_a_hashtag(user_hashtag)
        else:
            print('ошибка вводе')
    
    elif user_choice == 3:
        user_mention = input('введите имя пользователя(он должен начанаться с @)\n')
        if user.check_for_registered_user(user_mention) == True:
            text.output_of_the_marked_user_in_the_text(user_mention)
    
    elif user_choice == 4:
        user_name = input('введите имя пользователя\n')
        int_text.display_text_specific_user(user_name)

    elif user_choice == 5:
        print('вы вышли из программы')
        break