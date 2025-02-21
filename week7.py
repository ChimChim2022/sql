# -*- coding: utf-8 -*-
import pymysql
import pandas as pd

#the database name is ORG

#IMPORTANT: type your student password below
connection = pymysql.connect(host='127.0.0.1', user='root', password='1*2*Pkpk', database='org', port=3306)


# IMPORTANT: the table name is CASE SENSITIVE
# When you write the query, make sure to have the correct case of table name
# Also, make sure your dataframe column names are exactly same as the column names in expected output.
# (e.g. Salary is different from SALARY)


# Problem 1: Write an SQL query to fetch “LAST_NAME” from Worker table
# expected output(should be a dataframe):

# '''
#    LAST_NAME
# 0        Doe
# 1      Smith
# 2        Lee
# 3    Johnson
# 4     Watson
# 5        Kim
# 6       Chen
# 7      White
# 8      Brown
# 9    Johnson
# 10    Nguyen
# 11    Harris
# 12      Tran
# 13     Lopez
# 14  Gonzalez
# 15     Perez
# 16  Madercod
# 17      Wong
# '''

def question1():
	# write your query below
	query = "Select LAST_NAME from org.worker"
	df = pd.read_sql(query, connection)

	return df

print(question1())


# Problem 2: Write an SQL query to fetch unique values of DEPARTMENT from Worker table.
# with ascending Department name order
# expected output(should be a dataframe):

# '''
#          DEPARTMENT
# 0  Customer Service
# 1       Engineering
# 2         Executive
# 3           Finance
# 4   Human Resources
# 5                IT
# 6         Marketing
# 7        Operations
# 8             Sales
# 9      Supply Chain
# '''

def question2():
    # write your query below
	query = "SELECT DISTINCT DEPARTMENT FROM org.worker ORDER BY DEPARTMENT ASC"
	df = pd.read_sql(query, connection)

	return df

print(question2())


# # Problem 3: Write an SQL query to print only the FIRST_NAME, SALARY details from the Worker table with ascending FIRST_NAME order and descending SALARY order.
# #expected output(should be a dataframe):

# '''
#    FIRST_NAME  SALARY
# 0     Charles   72000
# 1       David  950000
# 2        Emma   68000
# 3       Frank   33000
# 4        Ivan   80000
# 5       James   85000
# 6        Jane   75000
# 7     Jessica   60000
# 8        John   80000
# 9        John   80000
# 10      Kevin   80000
# 11       Lily   70000
# 12       Lisa   75000
# 13    Melissa   65000
# 14    Michael   90000
# 15   Samantha   68000
# 16        Tom   90000
# 17    Zachary   72000
# '''

def question3():
    # write your query below
	query = "Select FIRST_NAME, SALARY from org.worker Order by FIRST_NAME asc, SALARY desc"
	df = pd.read_sql(query, connection)

	return df

print(question3())


# # Problem 4:  Write an SQL query to fetch no. of workers for each department
# # in the ascending order of number of worker.
# # make sure to name the correct column stated in expected output
# # expected output(should be a dataframe):

# '''
# 0      Supply Chain           1
# 1                IT           1
# 2         Marketing           1
# 3   Human Resources           1
# 4  Customer Service           1
# 5           Finance           2
# 6        Operations           2
# 7       Engineering           2
# 8         Executive           3
# 9             Sales           4
# '''

def question4():
    # write your query below
	query = "Select DEPARTMENT, Count(*) as WORKER_NUM from org.worker Group by DEPARTMENT Order by WORKER_NUM asc"
	df = pd.read_sql(query, connection)
	
	return df

print(question4())

# # Problem 5: Write an SQL query to fetch the WORKER_TITLE, FIRST_NAME, SALARY
# # with descending SALARY and ascending FIRST NAME as second sorting order
# # HINT: look at the schema diagram given in the README
# #expected output(should be a dataframe):

# '''
#                        WORKER_TITLE FIRST_NAME  SALARY
# 0                        Accountant      David  950000
# 1                 Assistant Manager    Michael   90000
# 2                     Sales Manager        Tom   90000
# 3              Supply Chain Manager      James   85000
# 4                Operations Manager       Ivan   80000
# 5                     Lead Engineer       John   80000
# 6                   Senior Engineer       John   80000
# 7                       Salesperson      Kevin   80000
# 8                           Manager       Jane   75000
# 9                 Financial Analyst       Lisa   75000
# 10               Software Developer    Charles   72000
# 11              Marketing Associate    Zachary   72000
# 12            Operations Supervisor       Lily   70000
# 13             Marketing Specialist       Emma   68000
# 14                    Sales Manager   Samantha   68000
# 15  Customer Service Representative    Melissa   65000
# 16                              CEO    Jessica   60000
# 17                      Salesperson      Frank   33000
# '''

def question5():
    # write your query below
	query = "SELECT org.title.WORKER_TITLE, org.worker.FIRST_NAME, org.worker.SALARY FROM org.worker LEFT JOIN org.title ON org.title.WORKER_REF_ID = org.worker.WORKER_ID ORDER BY org.worker.SALARY DESC, org.worker.FIRST_NAME ASC;"
	df = pd.read_sql(query, connection)

	return df

print(question5())


# # Problem 6: Write an SQL query to fetch the list of employees with the same salary with descending SALARY and ascending FIRST NAME as second sorting order
# #NOTE: WORKER_TITLE is the first column in the dataframe
# #expected output(should be a dataframe):

# '''
#             WORKER_TITLE FIRST_NAME  SALARY
# 0      Assistant Manager    Michael   90000
# 1          Sales Manager        Tom   90000
# 2     Operations Manager       Ivan   80000
# 3          Lead Engineer       John   80000
# 4        Senior Engineer       John   80000
# 5            Salesperson      Kevin   80000
# 6                Manager       Jane   75000
# 7      Financial Analyst       Lisa   75000
# 8     Software Developer    Charles   72000
# 9    Marketing Associate    Zachary   72000
# 10  Marketing Specialist       Emma   68000
# 11         Sales Manager   Samantha   68000
# '''

def question6():
    # write your query below
	query = "SELECT org.title.WORKER_TITLE, FIRST_NAME, SALARY FROM org.worker JOIN org.title ON org.title.WORKER_REF_ID = org.worker.WORKER_ID WHERE SALARY IN (SELECT SALARY FROM org.worker GROUP BY SALARY HAVING COUNT(*) > 1) ORDER BY SALARY DESC, FIRST_NAME ASC;"
	df = pd.read_sql(query, connection)

	return df

print(question6())


# # Problem 7: Write an SQL query to fetch the departments that have exactly 4 people in it.
# # make sure to name the correct column stated in expected output
# #expected output(should be a dataframe):

# '''
#   DEPARTMENT  No_Of_Workers
# 0      Sales              4
# '''

def question7():
    # write your query below
	query = "SELECT DEPARTMENT, COUNT(*) AS No_Of_Workers FROM org.worker GROUP BY DEPARTMENT HAVING COUNT(*) = 4;"
	df = pd.read_sql(query, connection)

	return df

print(question7())
