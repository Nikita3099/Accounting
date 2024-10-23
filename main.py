from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


def main():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Запуск программы 'Бухгалтерия' - {current_date}")

    get_employees()
    calculate_salary()


if __name__ == '__main__':
    main()
