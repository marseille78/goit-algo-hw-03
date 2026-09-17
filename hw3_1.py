from datetime import datetime

def get_days_from_today(date):
    try:
        user_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Будь ласка, введіть дату в форматі YYYY-MM-DD")
        return
    else:
        current_date = datetime.today()
        delta_date = current_date - user_date
        return delta_date.days

print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2026-09-20"))
print(get_days_from_today("2021.10.09"))