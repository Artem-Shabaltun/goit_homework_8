from datetime import datetime, timedelta


def get_period(next_week_start:bool) -> dict[int,datetime]: # створюємо словник із датами наступних 7 днів тижня
    next_days = []
    curent_date = datetime.now()
    
    if next_week_start: # визначаємо дату, з якої почненться період для виводу іменин
        period_to_start = curent_date + timedelta(days=4-curent_date.weekday())  # від найближчого понеділка
    else:
        period_to_start = curent_date # відсьогодні, якщо сьогодні  понеділок

    count = 1

    while count <= 7:
        period_to_start += timedelta(1)
        next_days.append((period_to_start.weekday(), period_to_start))
        count += 1

    return dict(next_days)


def get_datetime_date(date: datetime|str) -> datetime: # передбачимо використання різних форматів дати
    if isinstance(date, str):
        if date.find("-") == 4:
            return datetime.strptime(date, "%Y-%m-%d")
        elif date.find("-") == 2:
            return datetime.strptime(date, "%d-%m-%Y")
        elif date.find(".") == 4:
            return datetime.strptime(date, "%Y.%m.%d")
        elif date.find(".") == 2:
            return datetime.strptime(date, "%d.%m.%Y")
        elif date.find("/") == 4:
            return datetime.strptime(date, "%Y/%m/%d")
        elif date.find("/") == 2:
            return datetime.strptime(date, "%d/%m/%Y")
        else:
            return datetime(1, 1, 1)
    else:
        return date
    

def get_birthdays_per_week(users: list[dict[str,datetime|str]], next_week_start:bool=True) -> None: # виводимо імена користувачів, які мають день народження , починаючи з понеділка
    weekdays = get_period(next_week_start)
    
    moove_users_lst = [] # Створюємо список. Якщо день народження випадає на вихіний - іменинники додаються до цього списку
    
    for weekday_int, weekday_datetime in weekdays.items():
        users_lst = [] # Створюємо список. Для будніх днів - іменинники потрапляють в цей список
        
        for user_data in users:
            user_name = user_data.get("name")
            user_birthday = get_datetime_date(user_data.get("birthday"))
            
            if user_birthday.month == weekday_datetime.month and user_birthday.day == weekday_datetime.day:
                if weekday_int in (5, 6):
                    moove_users_lst.append(user_name)
                else:
                    users_lst.append(user_name)
        
        if weekday_int == 0:
            users_lst.extend(moove_users_lst)
        
        if len(users_lst):
            weekday_str = weekday_datetime.strftime("%A")
            users_str = ", ".join(users_lst)
            print(f"{weekday_str}: {users_str}")

users = [
    {"name": "Bill", "birthday": datetime(1997, 7, 30)}, # Переноситься на понеділок
    {"name": "Jill", "birthday": datetime(1997, 7, 31)}, # Понеділок
    {"name": "Kim", "birthday": datetime(1997, 8, 1)}, # Вівторок
    {"name": "Alina", "birthday": datetime(1997, 8, 2)}, # Середа
    {"name": "Jan", "birthday": datetime(1997, 8, 2)}, # Середа
    {"name": "Mykola", "birthday": datetime(1997, 8, 1)}, # Вівторок
    {"name": "Ivan", "birthday": datetime(1997, 8, 3)}, # Четвер
    {"name": "Oles", "birthday": datetime(1997, 8, 3)}, # Четвер
    {"name": "Nick", "birthday": datetime(1997, 8, 4)}, # П'ятниця
    {"name": "Artem", "birthday": datetime(1997, 8, 4)}, # П'ятниця
]
     
get_birthdays_per_week(users)
