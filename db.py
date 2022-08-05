import sqlite3


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(f'{db_name}.db')
        self.c = self.conn.cursor()

    def __format_string(self, **kwargs):
        string = ''
        for item in kwargs:
            string += f'{item} {kwargs[item]}, '
        return string[0: -2]

    def __format_insert(self, **kwargs):
        string = ''
        string1 = ''
        for item in kwargs:
            string += f'{item}, '
            string1 += f"'{kwargs[item]}', "
        return string[0: -2], string1[0:-2]

    def create_table(self, table_name, **col_name_types):
        try:
            col_type = self.__format_string(**col_name_types)
            self.c.execute(f'''CREATE TABLE {table_name}(ID INTEGER PRIMARY KEY, {col_type})''')
            self.conn.commit()
            print(f'Table {table_name} was created')
        except sqlite3.OperationalError:
            print(f'Table {table_name} already exist')

    def insert_into_table(self, table_name, **col_val):
        c_v = self.__format_insert(**col_val)
        self.c.execute(f'INSERT INTO {table_name} ({c_v[0]}) VALUES ({c_v[1]})')
        self.conn.commit()

    def execute_sql(self, sql_script):
        return self.c.execute(f'''{sql_script}''')


list_employee_department = '''
SELECT PERSON.first_name, PERSON.second_name, DEPARTMENT.abbreviation 
FROM PERSON 
JOIN EMPLOYEE ON PERSON.ID = person_id 
JOIN DEPARTMENT_EMPLOYEE ON employee.ID = DEPARTMENT_EMPLOYEE.employee_id 
JOIN DEPARTMENT ON department_id = DEPARTMENT.ID 
ORDER BY abbreviation
'''

list_vacations = '''
SELECT PERSON.first_name, PERSON.second_name, HISTORY_VACATION.start_date, HISTORY_VACATION.finish_date, abs(strftime('%d-%m-%Y', finish_date)-strftime('%d-%m-%Y', start_date)) AS `sum of days spent on vacation` 
FROM PERSON 
JOIN EMPLOYEE ON PERSON.ID = person_id 
JOIN HISTORY_VACATION ON EMPLOYEE.ID = HISTORY_VACATION.employee_id 
ORDER BY PERSON.ID
'''

employee_position_rate = '''
SELECT PERSON.first_name, PERSON.second_name, POSITION.position, POSITION.rate 
FROM PERSON 
JOIN EMPLOYEE ON PERSON.ID = person_id 
JOIN POSITION ON employee.position_id = POSITION.ID 
ORDER BY position
'''

list_department_head_amount = '''
SELECT t1.name, t1.emp_count, t2.first_name, t2.second_name FROM (SELECT DEPARTMENT.id, DEPARTMENT.name, count(DEPARTMENT_EMPLOYEE.employee_id) AS emp_count FROM DEPARTMENT
JOIN DEPARTMENT_EMPLOYEE ON DEPARTMENT.ID = DEPARTMENT_EMPLOYEE.department_id
GROUP BY DEPARTMENT.ID) AS t1
JOIN (SELECT DEPARTMENT.id, PERSON.first_name, PERSON.second_name FROM DEPARTMENT
JOIN DEPARTMENT_EMPLOYEE ON DEPARTMENT.ID = DEPARTMENT_EMPLOYEE.department_id
JOIN EMPLOYEE ON EMPLOYEE.ID = DEPARTMENT_EMPLOYEE.employee_id
JOIN PERSON ON EMPLOYEE.person_id = PERSON.ID
WHERE EMPLOYEE.head_officer = 1) AS t2 ON t1.id = t2.id
'''

reports = {
    'list_employee_department': list_employee_department,
    'list_vacations': list_vacations,
    'employee_position_rate': employee_position_rate,
    'list_department_head_amount': list_department_head_amount
}


def get_report(report):
    reports_result = []
    d = Database('factory')
    result = d.execute_sql(reports[report])
    for i in result.fetchall():
        reports_result.append(i)
    return reports_result


if __name__ == '__main__':
    '''
    Pass the name of report as an argument
    Example: 
    python db.py <one of the report below>
    
    1. list_employee_department
    2. list_vacations
    3. employee_position_rate
    4. list_department_head_amount
    '''
    import sys
    report = sys.argv[1]
    print(get_report(report=report))
