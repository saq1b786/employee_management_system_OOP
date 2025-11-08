import pytest
from employees import stats
from employees.data_handler import load_data

@pytest.fixture
def sample_data():
    return [
        {"name": "Alice", "age": 25, "title": "Engineer"},
        {"name": "Bob", "age": 40, "title": "Manager"},
        {"name": "Charlie", "age": 30, "title": "Engineer"}
    ]


#TESTS

def test_get_total_employees(sample_data):
    total_employees = stats.get_total_employees(sample_data)
    assert total_employees == 3 


def test_get_average_age(sample_data):
    average_age = stats.get_average_age(sample_data)
    result = (25+40+30)/ 3

    assert average_age == result

def test_get_oldest_employee(sample_data):
    oldest = stats.get_oldest_employee(sample_data)
    age = oldest['age']
    oldest_age = 40

    assert age == oldest_age

def test_get_youngest_employee(sample_data):
    youngest = stats.get_youngest_employee(sample_data)
    age = youngest['age']
    youngest_age = 25

    assert age == youngest_age

def test_get_titles_count(sample_data):
    titles = stats.get_titles_count(sample_data)
    title_engineers = titles['Engineer']
    engineer = 2

    assert title_engineers == engineer