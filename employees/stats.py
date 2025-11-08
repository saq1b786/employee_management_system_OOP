from .data_handler import load_data

def get_total_employees(data = None):
  if data is None:
    data = load_data()
  return len(data)


def get_average_age(data = None):
  if data is None:
    data = load_data()
  
  all_ages = []
  
  for employee in data:
    age = employee['age']
    all_ages.append(age)

  total_age = sum(all_ages) / len(data)
  
  return total_age


def get_oldest_employee(data = None):
  if data is None:
    data = load_data()

  current_oldest = data[0]

  for employee in data:
    if employee['age'] > current_oldest['age']:
      current_oldest = employee

  return current_oldest
  

def get_youngest_employee(data = None):
  if data is None:
    data = load_data()

  current_youngest = data[0]

  for employee in data:
    if employee['age'] < current_youngest['age']:
      current_youngest = employee

  return current_youngest
  

def get_titles_count(data = None):
  if data is None:
    data = load_data()
  
  titles = {}

  for employee in data:
    if employee['title'] in titles:
      titles[employee['title']] += 1
    else:
      titles[employee['title']] = 1
  
  return titles