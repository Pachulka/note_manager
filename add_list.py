username = input("Введите ваше имя:")
title = []
headings_of_notes_1 = input("Введите заголовок заметки 1 или оставьте пустым для завершения:")
title.append(headings_of_notes_1)
headings_of_notes_2 = input("Введите заголовок заметки 2 или оставьте пустым для завершения:")
title.append(headings_of_notes_2)
headings_of_notes_3 = input("Введите заголовок заметки 3 или оставьте пустым для завершения:")
title.append(headings_of_notes_3)
content = input('Введите описание заметки:')
status = input('Введите текущий статус: "В процессе", "Выполнено", "Отложено"')
created_date = input("Введите дату начала заметки:")
issue_date = input("Введите дату окончания заметки:")
temp_issue_date = created_date[0:5]
temp_created_date = issue_date[0:5]


print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print(f"Дата начала заметки: {temp_issue_date}")
print(f"Дата озончаня заметки: {temp_created_date}")

