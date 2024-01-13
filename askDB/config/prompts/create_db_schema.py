from typing import Dict

from common.constants import DB_PLACEHOLDER

example_format = f"""
- **Table Name**: Employees
  - **Description**: This table stores employee details.
  - **Columns**:
    - `EmployeeID` (Integer, *Primary Key*): Unique identifier for each employee.
    - `Name` (Varchar): The name of the employee.
    - `Position` (Varchar): The employee's job title.
    - `HireDate` (Date): The date the employee was hired.
    - `DepartmentID` (*Foreign Key*): The foreign key to table *Departments*.
- **Table Name**: Departments
  - **Description**: Contains department details.
  - **Columns**:
    - `DepartmentID` (Integer, *Primary Key*): Unique identifier for each department.
    - `DepartmentName` (Varchar): Name of the department.

- **Version**: PostgreSQL 12.4
- **Additional Context**: This schema is part of a human resources management system.
"""

sql_prompt_system = "You are a skilled SQL analyst. Focus on generating precise SQL statements for database analysis. Avoid providing explanations unless explicitly requested."

sql_prompt = f"""
Generate SQL statements to extract the following Information of a PostgreSQL database:
1. all table names
2. all column names
3. all column types, e.g. VARCHAR, Primary Key, Foreign Key

Use '{DB_PLACEHOLDER}' as the database name. The output should be in the following JSON format:
{{
  "queries": ["sql_1", "sql_2", ..., "sql_n"]
}}
Do not include explanatory texts, just the SQL queries.
"""

create_db_schema_system = "You are a skilled data engineer. Focus on describing databases using markdown. Avoid providing explanations unless explicitly requested."


def create_db_schema_prompt(db_information: Dict[str, str]):
    return f"""
Provided the following information of a database gained from the corresponding queries:
{'\n\n'.join([f'query_{i}: {k}\nresponse_{i}: {v}''' for i, (k, v) in enumerate(db_information.items())])}
Generate a decription of the tables in the database exactly in the following example markdown format:
{example_format}

Provide the database description like the given markdown example in the following JSON format:
{{
  "db_description": 'description_of_the_database'
}}
Do not include explanatory texts, just the db_description. Try to infer the description and the column information from the column names. There must be all tables and columns, do not leave any table or column out.
"""
