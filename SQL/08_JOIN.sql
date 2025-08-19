# JOIN

# ALIAS (별칭)
SELECT menu_code as 'code',
	   menu_name as name,
       menu_price as '메뉴의 가격'
  FROM tbl_menu;
  
SELECT m.menu_code,
	   m.menu_name,
       m.menu_price
  FROM tbl_menu as m;    -- as 생략 가능
  
# INNER JOIN
-- INNER 생략가능, 기본 JOIN은 INNER JOIN이다.
-- 둘 다 존재하는 컬럼만 가지고 JOIN을 함.
SELECT m.menu_code,
	   m.menu_name,
       c.category_name
  FROM tbl_menu m
  JOIN tbl_category c ON m.category_code = c.category_code;
  -- INNER JOIN tbl_category c ON m.category_code = c.category_code;

-- USING 사용 방법
SELECT m.menu_code,
	   m.menu_name,
       c.category_name
  FROM tbl_menu m
  JOIN tbl_category c USING (category_code);
  
  
# OUTER JOIN
-- LEFT JOIN
SELECT m.menu_code,
	   m.menu_name,
       c.category_name
  FROM tbl_category c
  LEFT JOIN tbl_menu m ON m.category_code = c.category_code;
  
-- RIGHT JOIN
SELECT m.menu_code,
	   m.menu_name,
       c.category_name
  FROM tbl_menu m
  RIGHT JOIN tbl_category c ON m.category_code = c.category_code;

# CROSS JOIN
SELECT a.menu_name, b.category_name
  FROM tbl_menu a
  CROSS JOIN tbl_category b;

# SELF JOIN
SELECT a.category_name, b.category_name as '상위 카테고리명'
  FROM tbl_category a 
  JOIN tbl_category b ON a.ref_category_code = b.category_code;