from datetime import datetime

class Person:
    def __init__(self, name, surname, date_of_birth):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        # Парсим строку даты рождения в объект datetime
        birth_date = datetime.strptime(self.date_of_birth, "%d.%m.%Y")
        # Получаем текущую дату
        today = datetime.now()
        # Вычисляем разницу между сегодняшней датой и датой рождения
        age = today.year - birth_date.year
        # Если день/месяц рождения еще не наступили в этом году, уменьшаем возраст на 1
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age


class Student(Person):
    def __init__(self, name, surname, date_of_birth, group):
        super().__init__(name, surname, date_of_birth)
        self.group = group

    def print_student_info(self):
        print(f"{self.name} {selfsS.surname}, возраст: {self.calculate_age()}, группа: {self.group}")


# Создаем экземпляр класса Person
person = Person("Марсель", "Цинцирук", "27.04.2010")
print(person.name, person.surname, person.calculate_age())

# Создаем экземпляр класса Student
student = Student("Иван", "Иванов", "01.09.2000", "ИТ-101")
student2  = Student(person, "ИТ-101")
student.print_student_info()
student2.print_student_info()
