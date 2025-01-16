# Создаём словарь для сохранения данных о заметках
information_note = {}

# Ввод данных от пользователя
information_note['username'] = input('Введите ваше имя:')
information_note['conten'] = input('Введите описание заметки:')
information_note['status'] = input('Введите текущий статус: "В процессе", "Выполнено", "Отложено":')
created_date = input('Введите дату начала: дд.мм.гггг.')
issue_date = input('Введите дату окончания: дд.мм.гггг.')
information_note['temp_issue_date'] = created_date[0:5] # Преобразование формата отображения дат без года
information_note['temp_created_date'] = issue_date[0:5] # Преобразование формата отображения дат без года

# Пользователь вводит три заголовка, которые сохраняются в список
titles = []
headings_of_notes_1 = titles.append(input('Введите заголовок заметки 1й или оставьте пустым для продолжения:'))
headings_of_notes_2 = titles.append(input('Введите заголовок заметки 2ой или оставьте пустым для продолжения:'))
headings_of_notes_3 = titles.append(input('Введите заголовок заметки 3й или оставьте пустым для продолжения:'))
information_note['title'] = titles # Добавляем список в словарь

# Вывод данных в структурированном виде
for key, value in information_note.items():
    print(f"{key}: {value}")