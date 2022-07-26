import sqlite3


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(f'{db_name}.db')
        self.cursor = self.conn.cursor()

    def save(self, sql_script):
        self.execute_sql(sql_script)
        self.conn.commit()

    def get(self, sql_script):
        result = self.execute_sql(sql_script).fetchall()
        self.conn.commit()
        return result

    def execute_sql(self, sql_script):
        return self.cursor.execute(f'''{sql_script}''')


class Department:
    def __init__(self, id, name, abbreviation, max_amount, database):
        self.id = id
        self.name = name
        self.abbreviation = abbreviation
        self.max_amount = max_amount
        self.database = database
        self.sql_script = ''

    def save(self):
        self.sql_script = f'''INSERT INTO DEPARTMENT (ID, name, abbreviation, max_amount) 
            VALUES ('{self.id}', '{self.name}', '{self.abbreviation}', '{self.max_amount}')'''
        return self.database.save(self.sql_script)

    def get(self, *args, **kwargs):
        self.sql_script = f'''SELECT {args} FROM department'''
        return self.database.get(self.sql_script)


class Person:
    def __init__(self, id_person, first_name, second_name, middle_name, passport, birthday, place_birthday,
                 address, database):
        self.id = id_person
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
            VALUES ('{self.id}', '{self.first_name}', '{self.second_name}', '{self.middle_name}', '{self.passport}', 
            '{self.birthday}', '{self.place_birthday}', '{self.address}')'''
        return self.database.save(self.sql_script)

    def get(self, *args, **kwargs):
        self.sql_script = f'''SELECT {args} FROM person'''
        return self.database.get(self.sql_script)


class Position:
    def __init__(self, id, position, rate, vacation_days, database):
        self.id = id
        self.position = position
        self.rate = rate
        self.vacation_days = vacation_days
        self.database = database
        self.sql_script = ''

    def save(self):
        self.sql_script = f'''INSERT INTO DEPARTMENT (ID, position, rate, vacation_days) 
            VALUES ('{self.id}', '{self.position}', '{self.rate}', '{self.vacation_days}')'''
        return self.database.save(self.sql_script)

    def get(self, *args, **kwargs):
        self.sql_script = f'''SELECT {args} FROM position'''
        return self.database.get(self.sql_script)


class Employee(Person):
    def __init__(self, id, employment_date, fired_date, head_officer, person_id, position_id, id_person, first_name,
                 second_name, middle_name, passport, birthday, place_birthday, address, database, position):
        super().__init__(id_person, first_name, second_name, middle_name, passport, birthday, place_birthday,
                         address, database)
        self.id = id
        self.employment_date = employment_date
        self.fired_date = fired_date
        self.head_officer = head_officer
        self.person_id = person_id
        self.position_id = position_id
        self.database = database
        self.sql_script = ''
        self.position = position

    def save(self):
        self.sql_script = f'''INSERT INTO DEPARTMENT (ID, employment_date, fired_date, head_officer, 
            person_id, person_id) 
            VALUES ('{self.id}', '{self.employment_date}', '{self.fired_date}', '{self.head_officer}', 
            '{self.person_id}', '{self.position_id}')'''
        return self.database.save(self.sql_script), super().save()

    def get_employee_list(self):
        self.sql_script = f'''SELECT * FROM employee'''
        return self.database.get(self.sql_script)

    def get_employee(self, employee_id):
        self.sql_script = f'''SELECT * FROM employee WHERE employee.ID={employee_id}'''
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
            raise QuantityLimit('In this department cannot work more then 20 workers!')
        return self.database.save(self.sql_script)

    def get(self, *args, **kwargs):
        self.sql_script = f'''SELECT {args} FROM DEPARTMENT_EMPLOYEE'''
        return self.database.get(self.sql_script)


class HistoryVacation:
    def __init__(self, id, start_date, finish_date, employee_id, department_id, database):
        self.id = id
        self.start_date = start_date
        self.finish_date = finish_date
        self.employee_id = employee_id
        self.database = database
        self.department_id = department_id
        self.sql_script = ''

    def save(self):
        self.sql_script = f'''INSERT INTO DEPARTMENT (ID, start_date, finish_date, employee_id) 
            VALUES ('{self.id}', '{self.start_date}', '{self.finish_date}', '{self.employee_id}')'''
        employees_on_vacation = f'''SELECT count(HISTORY_VACATION.employee_id) FROM HISTORY_VACATION
                                    JOIN EMPLOYEE ON HISTORY_VACATION.employee_id=EMPLOYEE.ID
                                    JOIN DEPARTMENT_EMPLOYEE ON EMPLOYEE.ID=DEPARTMENT_EMPLOYEE.employee_id
                                    WHERE DEPARTMENT_EMPLOYEE.department_id = {self.department_id}
                                    AND HISTORY_VACATION.finish_date > DATE('now')'''
        if self.database.execute_sql(employees_on_vacation).fetchone()[0] > 5:
            raise QuantityLimit('Currently on vacation are 5 employees')
        return self.database.save(self.sql_script)

    def get(self, *args, **kwargs):
        self.sql_script = f'''SELECT {args} FROM HistoryVacation'''
        return self.database.get(self.sql_script)


class Company:
    def __init__(self):
        self.list_departments = []
        self.list_employees = []
        self.department_employee = {}
        self.employees_vacation = []

    def add_department(self, id, name, abbreviation, max_amount, database):
        department = Department(id, name, abbreviation, max_amount, database)
        department.save()
        self.list_departments.append(department)

    def add_employee(self, id, employment_date, fired_date, head_officer, person_id, position_id, id_person, first_name,
                     second_name, middle_name, passport, birthday, place_birthday, address, database, position):
        employee = Employee(id, employment_date, fired_date, head_officer, person_id, position_id, id_person, first_name,
                            second_name, middle_name, passport, birthday, place_birthday, address, database, position)
        employee.save()
        self.list_employees.append(employee)

    def get_salary(self, employee):
        for emp in self.list_employees:
            if emp == employee:
                experience = employee.employment_date - employee.fired_date
                if experience >= 1:
                    return employee.position.rate*experience*1.012
                return employee.position.rate

    def allocation_employee_department(self, employee_id, department_id, database):
        emp_to_dep = DepartmentEmployee(employee_id, department_id, database)
        try:
            emp_to_dep.save()
        except QuantityLimit as q:
            print(q)
        else:
            self.department_employee[department_id] = employee_id

    def take_vacation(self, id, start_date, finish_date, employee_id, department_id, database):
        vacation = HistoryVacation(id, start_date, finish_date, employee_id, department_id, database)
        try:
            vacation.save()
        except QuantityLimit as q:
            print(q)
        else:
            self.employees_vacation.append(employee_id)


class QuantityLimit(Exception):
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return f'ERROR: {self.arg}'
