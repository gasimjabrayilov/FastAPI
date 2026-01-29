import pytest

def test_equal_or_not_equal():
    assert 1 == 1
    assert 3 != 1

def test_is_instance():
    assert isinstance(1, int)
    assert  isinstance("Hello", str)

def test_boolean():
    validated = True
    assert validated is True
    assert ('hello' == 'world') is False


def test_type():
    assert type('Hello' is str)
    assert type("World" is not int)

def test_greater_than():
    assert 1 > 0
    assert 4 < 10

def test_list():
    num_list = [1,2,3]
    any_list = [False, True]

    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)
    assert any(any_list)


class Student:
    def __init__(self, first_name: str, last_name: str, major: str, years: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years


# def test_person_initialization():
#     student = Student("Kasim", "Mahmud", "Computer Science", 3)
#     assert student.first_name == "Kasim"
#     assert student.last_name == "Mahmud"
#     assert student.major == "Computer Science"
#     assert student.years == 3

@pytest.fixture
def default_employee():
    return Student("Kasim", "Mahmud", "Computer Science", 3)

def test_person_initialization(default_employee):
    assert default_employee.first_name == "Kasim"
    assert default_employee.last_name == "Mahmud"
    assert default_employee.major == "Computer Science"
    assert default_employee.years == 3

















