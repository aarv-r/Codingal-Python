import random
from datetime import datetime, timedelta
def get_random_date(start_date, end_date):
    start=datetime.strptime(start_date, "%m/%d/%Y")
    end=datetime.strptime(end_date, "%m/%d/%Y")
    days=(end-start).days
    random_days=random.randint(0, days)
    return (start + timedelta(days=random_days)).strftime("%m/%d/%Y")
print(get_random_date("01/01/2026", "12/31/2026"))