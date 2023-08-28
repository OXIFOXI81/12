from PIL import Image
from datetime import datetime

from application.db.people import get_employees
from application.salary import calculate_salary


def date_now():
    dt_now = datetime.now()
    print(dt_now)
def View_pick(name):

    im = Image.open(f"{name}.jpg")
    im.show()

if __name__ == '__main__':
    # 2 задание
    calculate_salary()
    get_employees()
    # 3 задание
    date_now()
    # 4 задание
    View_pick("HPE")


