# 서브쿼리

use menudb;

-- 서브쿼리 1
SELECT category_code
FROM tbl_menu
WHERE menu_name = '열무김치라떼';

-- 메인쿼리 1
SELECT menu_code, menu_name, menu_price, category_code, orderable_status
FROM tbl_menu;

-- 메뉴명이 열무김치라떼인 메뉴의 카테고리와 동일한 카테괴의 메뉴 정보 조회
SELECT menu_code, menu_name, menu_price, category_code, orderable_status
FROM tbl_menu
WHERE category_code = (select category_code
						 FROM tbl_menu
						WHERE menu_name = '열무김치라떼');
                        
SELECT menu_code, menu_name, menu_price, category_code, orderable_status
FROM tbl_menu
WHERE category_code IN (select category_code
						 FROM tbl_menu
						WHERE menu_name LIKE '%김치%');
                        
                        
                        
-- 서브쿼리 2
SELECT COUNT(*) as 'count'
FROM tbl_menu
GROUP BY category_code;

-- 메인쿼리 2
SELECT MAX(count)
  FROM (SELECT COUNT(*) AS 'count'
		  FROM tbl_menu
          GROUP BY category_code) as countmenu;
          
-- 가장 많은 메뉴가 포함된 카테고리의 메뉴 개수 조회


# 상관 서브쿼리
-- 메인쿼리가 서브쿼리의 결과에 영향을 주는 경우
SELECT menu_code, menu_name, menu_price, category_code, orderable_status
  FROM tbl_menu a
 WHERE menu_price > (SELECT AVG(menu_price)
					   FROM tbl_menu
					  WHERE category_code = a.category_code
					 GROUP BY categpry_code);
                     
                     
# EXISTS
SELECT category_code, category_name
  FROM tbl_category a
 WHERE EXISTS (
				SELECT 1
                  FROM tbl_menu b
				 WHERE b.category_code = a.category_code
 );
 
 
 
 