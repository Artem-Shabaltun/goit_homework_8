from datetime import datetime, timedelta

def get_birthdays_per_week(users):

    birthdays = [[] for _ in range(7)] # створимо список та припишемо іменинників до кожного дня тижня, що припаде на день народження

    for user in users:
        birthday = user["birthday"].date() 
        birthday_day_of_week = birthday.weekday() # Отримаємо поточний день тижня (0 - понеділок, 6 - неділя)

        if birthday_day_of_week >=5: #Перевіримо, даний день є суботою, чи неділею
            need_days_to_add = 2 if birthday_day_of_week == 5 else 1 #Визначаємо скільки потрібно днів, аби перенести привітання на понеділок, в разі, якщо це вихідний
            birthday = birthday + timedelta(days=need_days_to_add)

        birthdays[birthday.weekday()].append(user["name"]) #Додаємо ім'я до списку іменинників на відповідний день, який ми створили

    for i in range(7):
        date_of_birthday = datetime.now() + timedelta(i)
        if birthdays[i]:
            print(f"{date_of_birthday.strftime('%A')}: {', '.join(birthdays[i])}")

users = [
    {"name": "Bill", "birthday": datetime(2023, 7, 30)},
    {"name": "Jill", "birthday": datetime(2023, 7, 31)},
    {"name": "Kim", "birthday": datetime(2023, 8, 1)},
    {"name": "Jan", "birthday": datetime(2023, 8, 2)},
    {"name": "Ivan", "birthday": datetime(2023, 8, 3)},
    {"name": "Nick", "birthday": datetime(2023, 8, 4)},
    {"name": "Artem", "birthday": datetime(2023, 8, 3)},
]

get_birthdays_per_week(users)
