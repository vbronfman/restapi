import pytest
import requests
def test_get_all_employees():
    res = requests.get("http://localhost:5000/employees")
    assert res.status_code == 200

def test_get_employee():
    res = requests.get("http://localhost:5000/employees/1")
    assert res.status_code == 200

def test_get_non_existing_employee():
    res = requests.get("http://localhost:5000/employees/666")
    assert res.status_code == 200








