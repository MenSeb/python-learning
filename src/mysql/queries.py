"""Modules to handle MySQL queries."""

EMPLOYE_TABLE = "Employe"
EMPLOYE_QUERY = """(
  id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(48) NOT NULL,
  last_name VARCHAR(48) NOT NULL,
  email VARCHAR(319) NOT NULL,
  phone VARCHAR(20) NOT NULL
)"""

TASK_TABLE = "Task"
TASK_QUERY = f"""(
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(50) NOT NULL,
  description TEXT NOT NULL,
  date_from DATE NOT NULL,
  date_to DATE NOT NULL,
  FOREIGN KEY(id) REFERENCES {EMPLOYE_TABLE}(id)
)"""
