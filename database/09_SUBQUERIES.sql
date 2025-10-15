# 서브쿼리

use menudb;

-- 서브쿼리1
SELECT category_code
  FROM tbl_menu
 WHERE menu_name = '열무김치라떼';
 
-- 메인쿼리1
SELECT menu_code, menu_name, menu_price, category_code, orderable_status
  FROM tbl_menu;

-- (WHERE절에 서브쿼리 사용)
-- 메뉴명이 열무김치라떼인 메뉴의 카테고리와 동일한 카테고리의 메뉴 정보 조회
SELECT menu_code, menu_name, menu_price, category_code, orderable_status
  FROM tbl_menu
 WHERE category_code = (SELECT category_code
						  FROM tbl_menu
						 WHERE menu_name = '열무김치라떼');

SELECT menu_code, menu_name, menu_price, category_code, orderable_status
  FROM tbl_menu
 WHERE category_code IN (SELECT category_code
						  FROM tbl_menu
						 WHERE menu_name LIKE '%김치%');



-- 서브쿼리2
SELECT COUNT(*) AS 'count'
  FROM tbl_menu
GROUP BY category_code;

-- 메인쿼리2
-- SELECT MAX(컬럼명)
--   FROM ();

-- (FROM 절에 서브쿼리 사용) / JOIN절에도 서브쿼리 사용 가능
-- 가장 많은 메뉴가 포함된 카테고리의 메뉴 개수 조회 
SELECT MAX(count)
  FROM (SELECT COUNT(*) AS 'count'
		  FROM tbl_menu
		GROUP BY category_code) as countmenu;



# 상관 서브쿼리
-- 메인쿼리가 서브쿼리의 결과에 영향을 주는 경우
SELECT menu_code, menu_name, menu_price, category_code, orderable_status
  FROM tbl_menu a
 WHERE menu_price > (SELECT AVG(menu_price)
					   FROM tbl_menu
					  WHERE category_code = a.category_code
					 GROUP BY category_code);
                     
SELECT AVG(menu_price)
  FROM tbl_menu
 WHERE category_code = a.category_code
GROUP BY category_code;



# EXISTS
-- 조회 결과가 존재하면 TRUE, 존재하지 않으면 FALSE
SELECT category_code, category_name
  FROM tbl_category a
 WHERE EXISTS(
				SELECT 1
                  FROM tbl_menu b
				 WHERE b.category_code = a.category_code
			 );
