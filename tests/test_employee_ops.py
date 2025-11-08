import pytest
import json
from employees import data_handler
from employees.employee_ops import EmployeeOps

# -------------------------
# Fixtures
# -------------------------
@pytest.fixture
def temp_data_file(tmp_path, monkeypatch):
    # Create a temp JSON file inside pytest’s temp directory
    temp_file = tmp_path / "employee_data.json"
    temp_file.write_text("[]")  # start with empty list

    # Monkeypatch the DATA_FILE in data_handler.py
    monkeypatch.setattr(data_handler, "DATA_FILE", temp_file)

    return temp_file

@pytest.fixture
def employee_ops(temp_data_file):
    return EmployeeOps()

# -------------------------
# Tests
# -------------------------

def test_add_employee(employee_ops, temp_data_file):
    employee_ops.add_employee("Alice", 25, "Engineer", "E001")

    with open(temp_data_file) as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]["name"] == "Alice"
    assert data[0]["employee_id"] == "E001"

def test_view_employees(employee_ops, capsys):
    # Add an employee first
    employee_ops.add_employee("Bob", 30, "Manager", "E002")

    employee_ops.view_employees()
    captured = capsys.readouterr()

    assert "Bob" in captured.out
    assert "30" in captured.out
    assert "Manager" in captured.out
    assert "E002" in captured.out

def test_update_employee(employee_ops, temp_data_file):
    employee_ops.add_employee("Charlie", 28, "Developer", "E003")

    # Update name and age
    result = employee_ops.update_employees("E003", name="Charles", age=29)
    assert result == "Update successful!"

    # Verify in-memory
    emp = employee_ops.employees[0]
    assert emp.get_name == "Charles"
    assert emp.get_age == 29

    # Verify saved in JSON
    with open(temp_data_file) as f:
        data = json.load(f)
    assert data[0]["name"] == "Charles"
    assert data[0]["age"] == 29

def test_delete_employee(employee_ops, temp_data_file):
    employee_ops.add_employee("Diana", 35, "Analyst", "E004")

    # Delete employee
    result = employee_ops.delete_employee("E004")
    assert "successfully deleted" in result

    # Ensure list is empty in-memory
    assert len(employee_ops.employees) == 0

    # Ensure JSON file is empty
    with open(temp_data_file) as f:
        data = json.load(f)
    assert data == []

def test_delete_nonexistent_employee(employee_ops):
    # Attempt to delete an employee that doesn't exist
    result = employee_ops.delete_employee("NON_EXISTENT")
    assert "not found" in result

def test_update_nonexistent_employee(employee_ops):
    # Attempt to update an employee that doesn't exist
    result = employee_ops.update_employees("NON_EXISTENT", name="Nobody")
    assert "failed" in result
