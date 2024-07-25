from datetime import date
from time import sleep

import tqdm

from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    print('\033[31mThe current date -', date.today().strftime('%d.%m.%Y'))
    for func in (pbar := tqdm.tqdm((calculate_salary, get_employees))):
        pbar.set_description(f'\033[31m{func()}')
        sleep(1)
