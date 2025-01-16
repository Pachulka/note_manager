# Создаём список для сохранения данных о заметках
information_the_note = []

# Ввод данных от пользователя с добавлением всех переменных в словарь
username = information_the_note.append(input('Введите ваше имя:'))
content = information_the_note.append(input('Введите описание заметки:'))
status = information_the_note.append(input('Введите текущий статус: "В процессе", "Выполнено", "Отложено":'))
created_date = input('Введите дату начала: дд.мм.гггг.')
issue_date = input('Введите дату окончания: дд.мм.гггг.')
temp_issue_date = information_the_note.append(created_date[0:5]) # Преобразование формата отображения дат без года
temp_created_date = information_the_note.append(issue_date[0:5]) # Преобразование формата отображения дат без года

# Пользователь вводит три заголовка, которые сохраняются в список
title = []
headings_of_notes_1 = title.append(input('Введите заголовок заметки 1й или оставьте пустым для продолжения:'))
headings_of_notes_2 = title.append(input('Введите заголовок заметки 2ой или оставьте пустым для продолжения:'))
headings_of_notes_3 = title.append(input('Введите заголовок заметки 3й или оставьте пустым для продолжения:'))
# Добавляем список с заголовками в общий список
information_the_note.append(title)

# Вывод всех значений
print(information_the_note)