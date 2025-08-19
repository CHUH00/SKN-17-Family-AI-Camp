use employeedb;

select * from employee;

# [2-2] Q1.
SELECT emp_id, emp_name, phone, hire_date, ent_yn
  FROM employee
 WHERE ent_yn = 'N' and phone LIKE '%2'
 ORDER BY hire_date
 LIMIT 3;
 
 # [2-2] Q2.
 SELECT e.emp_name, j.job_name, e.salary, e.dept_code, e.email, e.phone, e.hire_date
   FROM employee e
   JOIN JOB j
  WHERE ent_yn = 'N' and j.job_name = '대리'
  ORDER BY e.salary DESC;

# [2-2] Q3.
SELECT d.dept_title as '부서명', COUNT(*) as '인원', SUM(e.salary) as '급여합계', AVG(e.salary) as '급여평균'
FROM employee e
JOIN department d ON e.dept_code = d.dept_id
GROUP BY e.dept_code;

# [2-2] Q4.
SELECT e.emp_name, e.emp_no, e.phone, d.dept_title, j.job_name
FROM employee e
JOIN department d on e.dept_code = d.dept_id
JOIN job j USING (job_code)
ORDER BY e.hire_date ASC;

# [2-2] Q5.
-- 1단계
SELECT *
FROM employee
WHERE manager_id IS NOT NULL;

-- 2단계
SELECT COUNT(*)
  FROM employee
 WHERE emp_id IN (
       SELECT manager_id
         FROM employee
        WHERE manager_id IS NOT NULL
     );