from src.pre_built.sorting import sort_by
import pytest
import datetime


@pytest.fixture
def data():
    return [
        {
            "min_salary": 2000,
            "max_salary": 5000,
            "date_posted": datetime.date(2023, 3, 2),
        },
        {
            "min_salary": 8000,
            "max_salary": 15000,
            "date_posted": datetime.date(2023, 5, 2),
        },
        {
            "min_salary": 20000,
            "max_salary": 45000,
            "date_posted": datetime.date(2023, 9, 2),
        }
    ]


def test_sort_by_criteria(data):
    sort_by(data, "max_salary")
    assert data[0]['max_salary'] == 45000

    sort_by(data, "min_salary")
    assert data[0]['min_salary'] == 2000
    
    sort_by(data, "date_posted")
    assert data[0]['date_posted'] == datetime.date(2023, 3, 2)
