from dataclasses import dataclass
import datetime


@dataclass
class Department:
    ID: int
    name: str
    abbreviation: str
    max_amount: int

    def check_max_amount(self):
        if self.max_amount > 20:
            return 'In this department cannot work more then 20 workers!'


@dataclass
class Person:
    ID: int
    first_name: str
    second_name: str
    middle_name: str
    passport: str
    birthday: datetime.date
    place_birthday: str
    address: str


@dataclass
class Position:
    ID: int
    position: str
    rate: int
    vacation_days: int


@dataclass
class Employee(Person, Position):
    ID: int
    employment_date: datetime.date
    fired_date: datetime.date
    head_officer: bool
    person_id: int
    position_id: int

    def get_salary(self):
        experience = int(self.fired_date.strftime('%Y')) - int(self.employment_date.strftime('%Y'))
        return self.rate*experience*1.012


@dataclass
class DepartmentEmployee(Department, Employee):
    department_id: int
    employee_id: int


@dataclass
class HistoryVacation(Employee):
    ID: int
    employee_id: int
    start_date: datetime.date
    finish_date: datetime.date

    def get_number_employees_vacation(self):
        pass
