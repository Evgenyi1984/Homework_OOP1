class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lect_grade(self, lect, course, grade):
        if isinstance(lect, Lecturer):
            if course in lect.courses_attached:
                lect.st_grades[course] += [grade]
            else:
                return f'Лектор {lect} не преподаёт курс {course}'
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values())
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}\n")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\n" f"Фамилия: {self.surname}\n"


class Lecturer(Mentor):
    def __init__(self, name, surname, course):
        super().__init__(name, surname)
        self.course_taught = course
        self.st_grades = {}

    def __str__(self):
        avg_grade = sum(sum(grades) for grades in self.st_grades.values()) / sum(len(grades) for grades in self.st_grades.values())
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade}\n")


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
        return f"Имя: {self.name}\n" f"Фамилия: {self.surname}\n"


# Создание экземпляров классов
student1 = Student('Evgenii', 'Kostylev', 'male')
student1.finished_courses = ['Введение в программирование']
student1.courses_in_progress = ['Python', 'GIT']
student1.grades = {'Python': [8, 9, 7], 'GIT': [10, 9, 8]}

student2 = Student('Irina', 'Ivanova', 'female')
student2.finished_courses = ['Введение в программирование']
student2.courses_in_progress = ['Python', 'OOP']
student2.grades = {'Python': [7, 8, 9], 'OOP': [9, 8, 10]}

lecturer1 = Lecturer('Sergei', 'Petrov', 'Python')
lecturer1.st_grades = {'Python': [9, 9, 10]}

lecturer2 = Lecturer('Anna', 'Evtushenko', 'GIT')
lecturer2.st_grades = {'GIT': [8, 9, 10]}

reviewer1 = Reviewer('Petr', 'Ilovaev')
reviewer2 = Reviewer('Adelaida', 'Petrova')

# Вызов методов для созданных экземпляров классов
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)



# здесь создал функцию для подсчета средней оценки за 
# домашние задания по всем студентам
def avg_hw_grade(students, course):
    total_grade = 0
    count = 0
    for student in students:
        if course in student.grades:
            total_grade += sum(student.grades[course])
            count += len(student.grades[course])
    if count != 0:
        return total_grade / count
    else:
        return 0

# это функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def avg_lecture_grade(lecturers, course):
    total_grade = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.st_grades:
            total_grade += sum(lecturer.st_grades[course])
            count += len(lecturer.st_grades[course])
    if count != 0:
        return total_grade / count
    else:
        return 0

# Проверка функций
print("Средняя оценка за домашние задания по курсу Python:", avg_hw_grade([student1, student2], 'Python'))
print("Средняя оценка за лекции по курсу GIT:", avg_lecture_grade([lecturer1, lecturer2], 'GIT'))