# Ввод пользователем даты с подсказкой формата
created_date = input('Введите дату начала: "дд.мм.гггг."')
issue_date = input('Введите дату окончания: "дд.мм.гггг."')
temp_issue_date = created_date[0:5] # Преобразование формата отображения дат без года
temp_created_date = issue_date[0:5] # Преобразование формата отображения дат без года

# Вывод всех значений
print('Дата начала заметки:', temp_issue_date)
print('Дата окончания заметки:', temp_created_date)