from student import Student
from course_group import CourseGroup

student = Student("Татьяна", "Абрамова", 30, "Инженер по тестированию")
classmate1 = Student("Маргарита", "Ростова", 58, "Инженер по тестированию")
classmate2 = Student("Денис", "Рыбкин", 23, "Инженер по тестированию")
classmate3 = Student("Дмитрий", "Кузнецов", 40, "Инженер по тестированию")

course_group = CourseGroup(student, [classmate1, classmate2, classmate3])

print(course_group)
