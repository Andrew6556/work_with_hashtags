
# print('Добро пожаловать в приложение\nПроцесс регистрации')

# user = User(input('Введите ваше имя\n'),
#         int(input('Напишите пароль(цифрами)\n')))

# user.user_authorization(input('Введите ваше имя\n'),
#                     int(input('Напишите пароль\n')))

# from user import User


# if User.user_authorization('1','1') == True:
#     print('ok')

# else:
#     print_erorr()


# while True:
#     print("""
#     У вас есть возможности:
#     1.Добавить свой текст
#     2.Поиск конкретных текстов по хэштегу(#)
#     3.Найти все упоминание пользователя каком либо тексте(так @Ivan)
#     4.Вывод всех текстов созданные этим пользователем (Введите имя пользоавтеля без @)
#     5.Для выхода из программы напишите 
#     """)  

#     user_choice = int(input('Введите номер действия которое хотите сделать\n'))

#     if user_choice == 1:
#         add_text = input('ваш текст\n')
#         text.add_text_to_json(user, add_text)
#         print('текст успешно сохранился')

#     elif user_choice == 2:
#         user_hashtag = input('введите хэштег(он должен начанаться с #)\n')
#         if user_hashtag.startswith('#'):
#             text.hashtag_search(user_hashtag)
#         else:
#             print('ошибка вводе')
    
#     elif user_choice == 3:
#         user_hashtag = input('введите хэштег(он должен начанаться с @)\n')
#         if user_hashtag.startswith('@'):
#             text.check_for_registered_user(user_hashtag)
#         else:
#             print('ошибка вводе')
    
#     elif user_choice == 4:
#         user_name = input('введите имя пользователя\n')
#         text.search_text_specific_user(user_name)

#     elif user_choice == 5:
#         print('вы вышли из программы')
#         break