# WHERE

-- 1) 비교 연산자
-- 같음 : =
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
		WHERE orderable_status = 'Y';

-- 같지 않음 : !=, <>
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
		WHERE orderable_status <> 'Y';
        
-- 대소 비교 : <, >, <=, >=
-- 아래와 같은 비교는 오류는 발생하지 않으나 정상 결과를 현출하지 않음
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
		WHERE 10000 < menu_price <= 20000;
        
-- 2) AND
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
		WHERE menu_price > 10000 AND menu_price <= 20000;

-- 3) OR
-- 메뉴 가격이 30,000원 초과이거나 메뉴 이름이 '열무김치라떼'인 메뉴
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
		WHERE menu_price > 30000 OR menu_name = '열무김치라떼';
    
-- 4) BETWEEN
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
		WHERE menu_price BETWEEN 10000 AND 20000;
        
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
		WHERE menu_price NOT BETWEEN 10000 AND 20000;

-- 5) LIKE
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
		WHERE menu_name LIKE '%김치%';
        
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
		WHERE menu_name NOT LIKE '%김%치%';
        
-- 6) IN
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
		WHERE category_code = 4 OR category_code = 5 OR category_code = 6;
        
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
		WHERE category_code IN (4, 5, 6);
        
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
		WHERE category_code NOT IN (4, 5, 6);

-- 7) IS NULL
SELECT category_code, category_name, ref_category_code
	FROM tbl_category
		WHERE ref_category_code IS NULL;
        
SELECT category_code, category_name, ref_category_code
	FROM tbl_category
		WHERE ref_category_code IS NOT NULL;