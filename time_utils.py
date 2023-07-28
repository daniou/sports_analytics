import random
from datetime import datetime, timedelta


def random_datetime():
    # Define el rango de tiempo que desees
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31, 23, 59, 59)

    time_delta = end_date - start_date
    random_seconds = random.randint(0, time_delta.total_seconds())
    random_time = start_date + timedelta(seconds=random_seconds)
    return random_time
