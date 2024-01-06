example_format = f"""
- **Table Name**: Employees
  - **Description**: This table stores employee details.
  - **Columns**:
    - `EmployeeID` (Integer, Primary Key): Unique identifier for each employee.
    - `Name` (Varchar): The name of the employee.
    - `Position` (Varchar): The employee's job title.
    - `HireDate` (Date): The date the employee was hired.
- **Table Name**: Departments
  - **Description**: Contains department details.
  - **Columns**:
    - `DepartmentID` (Integer, Primary Key): Unique identifier for each department.
    - `DepartmentName` (Varchar): Name of the department.

- **Relationships**:
  - `Employees` is linked to `Departments` through the `DepartmentID` (Foreign Key in `Employees` table).

- **Version**: PostgreSQL 12.4
- **Additional Context**: This schema is part of a human resources management system.
"""


prompt = f"""
I possess a PostgreSQL database and am seeking to create an exceptionally detailed description of this database.
This comprehensive description is vital to facilitate the effective utilization of a Language Learning Model (LLM)
when interacting with and performing tasks related to the database. 
My goal is to ensure that the LLM can understand and work with the database as efficiently as possible.
In the following I provide an example format, which is completly unrelated to the actual data. 
It starts with START, followed by the format example and ends with END:
START
{example_format}
END

Can you provide SQL statements to fetch the necessary information
from the database with the following output format:
'query 1': 'first query here',
'query 2': 'second query here',
...
"""
