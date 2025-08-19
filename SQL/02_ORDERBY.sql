# ORDER BY
use menudb;

-- 오른차순 정렬 (ASC를 명시하지 않아도 기본 정렬 방식)
SELECT menu_code, menu_name, menu_price
	FROM tbl_menu
		ORDER BY menu_name ASC;
        
-- 내림차순 정렬 (DESC를 명시적으로 작성해야 내림차순 정렬)
SELECT menu_code, menu_name, menu_price
	FROM tbl_menu
		ORDER BY menu_name DESC;
     
-- 다중 조건 정렬
SELECT menu_code, menu_name, menu_price
	FROM tbl_menu
		ORDER BY menu_price DESC, menu_name ASC;
        
-- 별칭을 사용한 정렬
SELECT menu_code, menu_name, menu_price, menu_code*menu_price as '연산결과'
	FROM tbl_menu
		ORDER BY '연산결과';
        
-- 오름차순 정렬 시 기본적으로 (default) NULL이 맨처음
-- IS NULL을 붙이면 NULL을 맨끝으로 보냄 (IS NULL ASC)
SELECT category_code, category_name, ref_category_code
	FROM tbl_category
    ORDER BY ref_category_code IS NULL;
    
-- 내림차순 정렬 시 기본적으로 (default) NULL이 맨끝
-- IS NULL을 붙이면 NULL을 맨처음으로 보냄 (IS NULL DESC) : DESC 생략 불가
SELECT category_code, category_name, ref_category_code
	FROM tbl_category
    ORDER BY ref_category_code IS NULL DESC, ref_category_code DESC;