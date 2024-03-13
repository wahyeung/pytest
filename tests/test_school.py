import pytest
from source.school import Classroom, Student, Teacher, TooManyStudents 

@pytest.fixture
def setup_classroom():
    # Creating a Hogwarts classroom setup
    teachers = [Teacher("Professor McGonagall")]
    students = [Student("Harry"), Student("Hermione"), Student("Ron")]
    course_title = "Transfiguration"
    classroom = Classroom(teachers, students, course_title)
    return classroom

def test_add_student(setup_classroom):
    classroom = setup_classroom
    new_student = Student("Luna")
    classroom.add_student(new_student)
    assert new_student in classroom.students

def test_remove_student(setup_classroom):
    classroom = setup_classroom
    classroom.remove_student("Ron")
    assert all(student.name != "Ron" for student in classroom.students)

def test_change_teacher(setup_classroom):
    classroom = setup_classroom
    new_teacher = Teacher("Professor Snape")
    classroom.change_teacher(new_teacher)
    assert classroom.teacher == new_teacher

def test_too_many_students(setup_classroom):
    classroom = setup_classroom
    for i in range(8):  # Already have 3 students, adding 8 more to exceed the limit
        classroom.add_student(Student(f"Student {i}"))
    with pytest.raises(TooManyStudents):
        classroom.add_student(Student("One too many"))

@pytest.mark.parametrize("student_name", ["Harry", "Hermione", "Nonexistent Student"])
def test_find_student(setup_classroom, student_name):
    classroom = setup_classroom
    found = any(student.name == student_name for student in classroom.students)
    expected = student_name in ["Harry", "Hermione"]  # "Nonexistent Student" should not be found
    assert found is expected
