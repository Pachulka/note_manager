username = input('Введите ваше имя:')
title = []
headings_of_notes_1 = title.append(input('Введите заголовок заметки 1й или оставьте пустым для продолжения:'))
headings_of_notes_2 = title.append(input('Введите заголовок заметки 2ой или оставьте пустым для продолжения:'))
headings_of_notes_3 = title.append(input('Введите заголовок заметки 3й или оставьте пустым для продолжения:'))
content = input('Введите описание заметки:')
status = input('Введите текущий статус: "В процессе", "Выполнено", "Отложено"')
created_date = input('Введите дату начала: дд.мм.гггг.')
issue_date = input('Введите дату окончания: дд.мм.гггг.')
temp_issue_date = created_date[0:5]
temp_created_date = issue_date[0:5]


print('Имя пользователя:', username)
print('Заголовок заметки:', title)
print('Описание заметки:', content)
print('Статус заметки:', status)
print(f'Дата начала заметки: {temp_issue_date}')
print(f'Дата озончаня заметки: {temp_created_date}')

