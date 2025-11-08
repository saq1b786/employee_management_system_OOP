from .data_handler import load_data, save_data
class Employee:
  def __init__(self, name, age, title, employee_id):
    self._name = name 
    self.__age = age
    self._title = title
    self.__employee_id = employee_id

  def __str__(self):
    return f"Employee: {self._name} | Age: {self.__age} | Title: {self._title} | ID: {self.__employee_id}"


  @property
  def get_age(self):
    return self.__age
  
  @property
  def get_employee_id(self):
    return self.__employee_id
  
  @property
  def get_name(self):
    return self._name
  
  @property
  def get_title(self):
    return self._title
  
  @get_age.setter
  def update_age(self, new_age):
    self.__age = new_age

  @get_name.setter
  def update_name(self, new_name):
    self._name = new_name

  @get_title.setter
  def update_title(self, new_title):
    self._title = new_title
  
  def to_dict(self):
    employee = {
      'name': self._name, 
      'age': self.__age, 
      'title': self._title, 
      'employee_id': self.__employee_id
    }
    return employee
  

class EmployeeOps:
  def __init__(self):
    self.employees = []
    self.load_employees()

  def load_employees(self):
    employee_data = load_data()

    for emp in employee_data:
      new_emp = (Employee(emp['name'], emp['age'], emp['title'], emp['employee_id']))
      self.employees.append(new_emp)

  def add_employee(self, name, age, title, employee_id):
    added_emp = Employee(name, age, title, employee_id)
    self.employees.append(added_emp)
    all_employees_dict = [emp.to_dict() for emp in self.employees]
    save_data(all_employees_dict)

  def view_employees(self):
    if not self.employees:
      return 'No employees found'
    else:
      for employee in self.employees:
        print(f'{employee.get_name} | {employee.get_age} | {employee.get_title} | {employee.get_employee_id}' ) 


  def update_employees(self, employee_id, **kwargs):
      found = False  # track if an employee was updated

      for employee in self.employees:
          if employee.get_employee_id == employee_id:
              found = True

              if 'name' in kwargs:
                  employee.update_name(kwargs['name'])
                  print(f"Name updated to {employee.get_name}")

              if 'age' in kwargs:
                  employee.update_age(kwargs['age'])
                  print(f"Age updated to {employee.get_age}")

              if 'title' in kwargs:
                  employee.update_title(kwargs['title'])
                  print(f"Title updated to {employee.get_title}")

              break  # stop searching once we found the right employee

      if not found:
          print("The employee ID was not found. Please try again.")
          return "Update failed: employee not found."

      updated_list = [emp.to_dict() for emp in self.employees]
      save_data(updated_list)
      return "Update successful!"


  def delete_employee(self, employee_id):
     found = False
     for employee in self.employees:
        if employee.get_employee_id == employee_id:
           found = True 
           self.employees.remove(employee)
           updated_list = [empl.to_dict() for empl in self.employees]
           save_data(updated_list)
           return f'{employee_id} has been successfully deleted!'
           

     if not found:
        return f'{employee_id} was not found.'
     



    

