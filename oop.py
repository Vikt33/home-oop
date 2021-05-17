class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def average_grade_homework(self):
        for course, grades in self.grades.items():
            return sum(grades) / len(grades)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {(Student.average_grade_homework(self))} \n Курсы в процессе изучения: {self.courses_in_progress}\n Завершенные курсы: {self.finished_courses}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Это не студент")
            return
        return Student.average_grade_homework(self) < other.average_grade_homework()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturer = {}

    def average_grade_lectures(self):
        for course, grades_lecturer in self.grades_lecturer.items():
            return sum(grades_lecturer) / len(grades_lecturer)

    def average_grade_course(self, course):
        if course in self.courses_attached:
            for grades_lecturer in self.grades_lecturer.values():
                return sum(grades_lecturer) / len(grades_lecturer)
        else:
            return "Ошибочный курс"

    def __str__(self):
        return f"Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {round(Lecturer.average_grade_lectures(self))}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Это не лектор")
            return
        return Lecturer.average_grade_lectures(self) < other.average_grade_lectures()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\n Фамилия: {self.surname}"


def average_grade_all_lecturers(course, *args):
    grades_all_lecturer = []
    for lecturer in args:
        if course in lecturer.courses_attached:
            grades_all_lecturer.append(round((lecturer.average_grade_lectures(course)), 1))
            average_grade = sum(grades_all_lecturer) / len(grades_all_lecturer)
    return f'Средняя оценка за лекции всех лекторов "{course}" : {round(average_grade, 1)}'


student_1 = Student("Иван", "Иванович", "мужской")
student_1.finished_courses += ['Java']
student_1.courses_in_progress += ['Python', 'GIT']

student_2 = Student("Иван", "Иванович", "мужской")
student_2.finished_courses += ['Java']
student_2.courses_in_progress += ['Python', 'GIT']

lecturer_1 = Lecturer("Сергей", "Петрович")
lecturer_1.courses_attached += ['Python', 'GIT']

lecturer_2 = Lecturer("Сергей", "Петрович")
lecturer_2.courses_attached += ['Python', 'GIT']

student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_2.rate_lecturer(lecturer_2, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'GIT', 7)
student_2.rate_lecturer(lecturer_2, 'GIT', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_2.rate_lecturer(lecturer_2, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'GIT', 10)
student_2.rate_lecturer(lecturer_2, 'GIT', 7)

print(student_1)
print(lecturer_1)
print(lecturer_1.grades_lecturer)
print()
print(lecturer_2)
print(lecturer_2.grades_lecturer)
print()
print(lecturer_1 < lecturer_2)
print(average_grade_all_lecturers('Python', lecturer_1, lecturer_2))
print(average_grade_all_lecturers('GIT', lecturer_1, lecturer_2))