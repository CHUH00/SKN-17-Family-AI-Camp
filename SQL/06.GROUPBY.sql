# GROUP BY

SELECT category_code, COUNT(*)
	FROM tbl_menu
		GROUP BY category_code;

SELECT category_code, SUM(menu_price)
	FROM tbl_menu
		GROUP BY category_code;
        
SELECT category_code, AVG(menu_price)
	FROM tbl_menu
		GROUP BY category_code;
        
SELECT category_code, menu_price, COUNT(*)
	FROM tbl_menu
		GROUP BY category_code, menu_price;
  
  
# HAVING

SELECT category_code, COUNT(*)
	FROM tbl_menu
		GROUP BY category_code
			HAVING category_code BETWEEN 5 AND 8;


# ROLLUP

-- 컬럼 한 개를 활용해 GROUP BY 후 ROLLUP -> 총계(합계) 
SELECT category_code, SUM(menu_price)
	FROM tbl_menu
		GROUP BY category_code
			WITH ROLLUP;
            
-- 컬럼 두 개를 활용해 GROUP BY 후 ROLLUP -> 중계 + 총계
-- 먼저 나온 컬럼의 총합을 구하고, 이후에 나오는 컬럼의 총합까지 구하는 방법
SELECT category_code, menu_price, COUNT(*)
	FROM tbl_menu
		GROUP BY category_code, menu_price
			WITH ROLLUP;