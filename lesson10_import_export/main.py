from config import STUDENT_LANGUAGE, STUDENT_NAME

from lesson8_function.main4 import make_circle


def print_student_info():
    print(f"Студент {STUDENT_NAME} учит {STUDENT_LANGUAGE}")


make_circle(y=5, x=5, radius=5, line_width=6, fill=False)
