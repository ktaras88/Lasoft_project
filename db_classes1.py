import sqlite3
import datetime


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(f'{db_name}.db')
        self.c = self.conn.cursor()

    def save(self, sql_script):
        self.execute_sql(sql_script)
        self.conn.commit()

    def get(self, sql_script):
        result = self.execute_sql(sql_script).fetchall()
        self.conn.commit()
        return result

    def execute_sql(self, sql_script):
        return self.c.execute(f'''{sql_script}''')


class Department:
    def __init__(self, ID, name, abbreviation, max_amount, database):
        self.ID = ID
        self.name = name
        self.abbreviation = abbreviation
        self.max_amount = max_amount
        self.database = database
        self.sql_script = ''

    def save(self):
        self.sql_script = f'''INSERT INTO DEPARTMENT (ID, name, abbreviation, max_amount) 
            VALUES ('{self.ID}', '{self.name}', '{self.abbreviation}', '{self.max_amount}')'''
        return self.database.save(self.sql_script)

    def get(self, *args, **kwargs):
        self.sql_script = f'''SELECT {args} FROM department'''
        return self.database.get(self.sql_script)

    # def check_amount_employee_department(self, department_id):
    #     pass

    def get_salary(self, employee_id):
        experience = self.employment_date - self.fired_date
        if experience > 0:
            return self.rate*experience*1.012
        return self.rate


class Person:
    def __init__(self, ID, first_name, second_name, middle_name, passport, birthday, place_birthday, address, database):
        self.ID = ID
        self.first_name = first_name
        self.second_name = second_name
        self.middle_name = middle_name
        self.passport = passport
        self.birthday = birthday
        self.place_birthday = place_birthday
        self.address = address
        self.database = database
        self.sql_script = ''

    def save(self):
        self.sql_script = f'''INSERT INTO DEPARTMENT (ID, first_name, second_name, middle_name, passport, birthday, 
            place_birthday, address) 
            VALUES ('{self.ID}', '{self.first_name}', '{self.second_name}', '{self.middle_name}', '{self.passport}', 
            '{self.birthday}', '{self.place_birthday}', '{self.address}')'''
        return self.database.save(self.sql_script)

    def get(self, *args, **kwargs):
        self.sql_script = f'''SELECT {args} FROM department'''
        return self.database.get(self.sql_script)


class Position:
    def __init__(self, ID, position, rate, vacation_days, database):
        self.ID = ID
        self.position = position
        self.rate = rate
        self.vacation_days = vacation_days
        self.database = database
        self.sql_script = ''

    def save(self):
        self.sql_script = f'''INSERT INTO DEPARTMENT (ID, position, rate, vacation_days) 
            VALUES ('{self.ID}', '{self.position}', '{self.rate}', '{self.vacation_days}')'''
        return self.database.save(self.sql_script)

    def get(self, *args, **kwargs):
        self.sql_script = f'''SELECT {args} FROM department'''
        return self.database.get(self.sql_script)


class Employee:
    def __init__(self, ID, employment_date, fired_date, head_officer, person_id, position_id, database):
        self.ID = ID
        self.employment_date = employment_date
        self.fired_date = fired_date
        self.head_officer = head_officer
        self.person_id = person_id
        self.position_id = position_id
        self.database = database
        self.sql_script = ''

    def save(self):
        self.sql_script = f'''INSERT INTO DEPARTMENT (ID, employment_date, fired_date, head_officer, 
            person_id, person_id) 
            VALUES ('{self.ID}', '{self.employment_date}', '{self.fired_date}', '{self.head_officer}', 
            '{self.person_id}', '{self.position_id}')'''
        return self.database.save(self.sql_script)

    def get(self, *args, **kwargs):
        self.sql_script = f'''SELECT {args} FROM department'''
        return self.database.get(self.sql_script)


class DepartmentEmployee:
    def __init__(self, department_id, employee_id, database):
        self.department_id = department_id
        self.employee_id = employee_id
        self.database = database
        self.sql_script = ''

    def save(self):
        self.sql_script = f'''INSERT INTO DEPARTMENT (department_id, employee_id) 
            VALUES ('{self.department_id}', '{self.employee_id}')'''
        amount_emp_dep = f'''SELECT count(employee_id) FROM department_employee WHERE department_id={self.department_id}'''
        if self.database.execute_sql(amount_emp_dep).fetchone()[0] > 20:
            return print('In this department cannot work more then 20 workers!')
        return self.database.save(self.sql_script)

    def get(self, *args, **kwargs):
        self.sql_script = f'''SELECT {args} FROM department'''
        return self.database.get(self.sql_script)


class HistoryVacation:
    def __init__(self, ID, start_date, finish_date, employee_id, database):
        self.ID = ID
        self.start_date = start_date
        self.finish_date = finish_date
        self.employee_id = employee_id
        self.database = database
        self.sql_script = ''

    def save(self):
        self.sql_script = f'''INSERT INTO DEPARTMENT (ID, start_date, finish_date, employee_id) 
            VALUES ('{self.ID}', '{self.start_date}', '{self.finish_date}', '{self.employee_id}')'''
        return self.database.save(self.sql_script)

    def get(self, *args, **kwargs):
        self.sql_script = f'''SELECT {args} FROM department'''
        return self.database.get(self.sql_script)

    def check_number_employees_vacation(self, department_id):
        pass


db = Database('factory')
