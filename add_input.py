username = input('Введите ваше имя:')
title = input('Введите заголовок или оставьте пустым для продолжения:')
content = input('Введите описание заметки:')
status = input('Введите текущий статус: "В процессе", "Выполнено", "Отложено"')
created_date = input('Введите дату начала: дд.мм.гггг.')
issue_date = input('Введите дату окончания: дд.мм.гггг.')

print('Имя пользователя:', username)
print('Заголовок заметки:', title)
print('Описание заметки:', content)
print('Статус заметки:', status)
print('Дата создания заметки:', created_date)
print('Дата истечения заметки:', issue_date)
