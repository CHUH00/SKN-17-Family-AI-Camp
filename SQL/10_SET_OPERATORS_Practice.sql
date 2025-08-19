use employeedb;
select * from DEPARTMENT;
# [2-3] Q1.
SELECT d.dept_title, e.dept_code, MAX(e.salary)
  FROM employee e
  JOIN department d
 WHERE e.dept_code = d.dept_id
 GROUP BY e.dept_code;

# [2-3] Q2.
SELECT emp_no, emp_name, dept_code, salary
  FROM employee
 WHERE dept_code IN (SELECT dept_id
					   FROM department
					  WHERE dept_title LIKE '%영업%');

# [2-3] Q3.
SELECT e.emp_no, e.emp_name, d.dept_title, e.salary
  FROM employee e
  JOIN department d
 WHERE (SELECT dept_id
		  FROM department
		 WHERE dept_title LIKE '%영업%') d ON e.dept_code = d.dept_id;

# [2-3] Q4.


# [2-3] Q5.

