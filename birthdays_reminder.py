from datetime import datetime, timedelta

def get_birthdays_per_week(users):

    birthdays = [[] for _ in range(7)] # створимо список та припишемо іменинників до кожного дня тижня, що припаде на день народження

    today = datetime.now().date() #визначимо поточну дату

    for user in users:
        birthday = user["birthday"].date() 
        birthday_day_of_week = birthday.weekday() # визначає понеділок першим днем тижня 0 = понеділок, 6 = неділя
        monday = today - timedelta(days=today.weekday()) #від поточної дати виконуємо повернення на понеділок, щоб не збивалося визначення 0 = понеділок

        if birthday_day_of_week >=5: #проводимо перевірку чи даний день є вихідним (5 = субота, 6 = неділя)
            need_days_to_add = 2 if birthday_day_of_week == 5 else 1 #Визначаємо скільки потрібно днів, аби перенести привітання на понеділок, в разі, якщо це вихідний
            birthday = birthday + timedelta(days=need_days_to_add)

        birthdays[birthday.weekday()].append(user["name"]) #Додаємо ім'я до списку іменинників на відповідний день, який ми створили

    for i in range(7):
        date_of_birthday = monday + timedelta(days=i)
        if birthdays[i]:
            print(f"{date_of_birthday.strftime('%A')}: {', '.join(birthdays[i])}")

users = [
    {"name": "Bill", "birthday": datetime(2023, 7, 30)}, # Переноситься на понеділок
    {"name": "Jill", "birthday": datetime(2023, 7, 31)}, # Понеділок
    {"name": "Kim", "birthday": datetime(2023, 8, 1)}, # Вівторок
    {"name": "Alina", "birthday": datetime(2023, 8, 2)}, # Середа /Вівторок (перевірити чи зникне пуста середа в списку)
    {"name": "Jan", "birthday": datetime(2023, 8, 2)}, # Середа /Вівторок (перевірити чи зникне пуста середа в списку)
    {"name": "Mykola", "birthday": datetime(2023, 8, 1)}, # Вівторок
    {"name": "Ivan", "birthday": datetime(2023, 8, 3)}, # Четвер
    {"name": "Oles", "birthday": datetime(2023, 8, 3)}, # Четвер
    {"name": "Nick", "birthday": datetime(2023, 8, 4)}, # П'ятниця
    {"name": "Artem", "birthday": datetime(2023, 8, 4)}, # П'ятниця
    {"name": "Mykyta", "birthday": datetime(2023, 8, 1)}, # Понеділок
]

get_birthdays_per_week(users)
