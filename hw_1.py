# Home work #1

class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        marital_status = "женат/замужем" if self.is_married else "холост/незамужем"
        print(f"Меня зовут {self.fullname}, мне {self.age} лет, я {marital_status}.")


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average_marks(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)


class Teacher(Person):
    base_salary = 50000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        if self.experience > 3:
            bonus = (self.experience - 3) * 0.05 * Teacher.base_salary
        else:
            bonus = 0
        return Teacher.base_salary + bonus


def create_students():
    student1 = Student("Уланов Назар", 16, False, {"математика": 5, "русский язык": 4})
    student2 = Student("Мукашев Максат", 17, False, {"математика": 3, "русский язык": 5})
    student3 = Student("Садырова Мария", 16, False, {"математика": 4, "русский язык": 4, "физика": 5})

    return [student1, student2, student3]


teacher = Teacher("Любовь Михайловна", 55, True, 25)
teacher.introduce_myself()
print(f"Зарплата: {teacher.calculate_salary()}")

students = create_students()
for student in students:
    student.introduce_myself()
    print(f"Оценки: {student.marks}")
    print(f"Средняя оценка: {student.average_marks():.2f}")
