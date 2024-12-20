import pytest
import pandas as pd
from week7 import *

def test_1():
	d = {'LAST_NAME': ['Doe', 'Smith', 'Lee', 'Johnson', 'Watson', 'Kim', 'Chen', 'White', 'Brown', 'Johnson', 'Nguyen', 'Harris', 'Tran', 'LOpez', 'Gonzalez', 'Perez', 'Madercod', 'Wong']}
	ans = pd.DataFrame(data=d)
	ans = ans[['LAST_NAME']]
	print(question1())
	assert all(question1() == ans)
 
def test_2():
	d = {'DEPARTMENT':['Customer Service','Engineering', 'Executive', 'Finance', 'Human Resources', 'IT', 'Marketing', 'Operations', 'Sales', 'Supply Chain']}
	ans = pd.DataFrame(data=d)
	ans = ans[['DEPARTMENT']]
	print(ans)
	assert all(question2() == ans)

def test_3():
	d = {'FIRST_NAME':['Charles', 'David', 'Emma', 'Frank', 'Ivan', 'James', 'Jane', 'Jessica', 'John', 'John', 'Kevin', 'Lily', 'Lisa', 'Melissa', 'Michael', 'Samantha', 'Tom', 'Zachary'], 'SALARY':[72000, 950000, 68000, 33000, 80000, 85000, 75000, 60000, 80000, 80000, 80000, 70000, 75000, 65000, 90000, 68000, 90000, 72000]}
	ans = pd.DataFrame(data=d)
	ans = ans[['FIRST_NAME','SALARY']]
	assert all(question3() == ans)

def test_4():
	d = {'DEPARTMENT': ['Supply Chain', 'IT', 'Marketing', 'Human Resources', 'Customer Service', 'Finance', 'Operations', 'Engineering', 'Executive', 'Sales'], 'WORKER_NUM': [1, 1, 1, 1, 1, 2, 2, 2, 3, 4]}
	ans = pd.DataFrame(data=d)
	ans = ans[['DEPARTMENT','WORKER_NUM']]
	assert all(question4() == ans)
