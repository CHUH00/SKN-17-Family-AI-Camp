# SET OPERATORS

# UNION (합집합)
SELECT menu_code, menu_name, menu_price, category_code
  FROM tbl_menu
 WHERE category_code = 10
UNION
 SELECT menu_code, menu_name, menu_price, category_code
  FROM tbl_menu
 WHERE menu_price < 9000;

# UNION ALL (합집합 + 교집합)
SELECT menu_code, menu_name, menu_price, category_code
  FROM tbl_menu
 WHERE category_code = 10
UNION ALL
 SELECT menu_code, menu_name, menu_price, category_code
  FROM tbl_menu
 WHERE menu_price < 9000;

# INTERSECT (교집합)
-- MySQL은 INTERSECT를 제공하지 않음
-- 단, INNER JOIN 또는 IN을 활용한 구현 가능

-- 1) INNER JOIN
SELECT a.menu_code, a.menu_name, a.menu_price, a.category_code
  FROM tbl_menu a
  JOIN ( 
		SELECT menu_code, menu_name, menu_price, category_code
		  FROM tbl_menu
		 WHERE menu_price < 9000
	   ) b ON a.menu_code = b.menu_code
 WHERE a.category_code = 10;

-- 2) IN
SELECT menu_code, menu_name, menu_price, category_code
  FROM tbl_menu
 WHERE category_code = 10
   AND menu_code IN (SELECT menu_code
					   FROM tbl_menu
					  WHERE menu_price < 9000);

# MINUS (차집합)
-- MySQL은 MINUS를 제공하지 않음
-- 단, LEFT JOIN을 활용한 구현 가능
SELECT a.menu_code, a.menu_name, a.menu_price, a.category_code
  FROM tbl_menu a
LEFT JOIN ( 
			SELECT menu_code, menu_name, menu_price, category_code
			  FROM tbl_menu
			 WHERE menu_price < 9000
		   ) b ON a.menu_code = b.menu_code
 WHERE a.category_code = 10
   AND b.menu_code IS NULL;
