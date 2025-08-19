# SELECT ~ FROM ~

use menudb;

-- 단일 컬럼 조회
SELECT menu_name
	FROM tbl_menu;
    
-- 다중 컬럼 조회
SELECT menu_code, menu_name, category_code, orderable_status
	FROM tbl_menu;

-- 전체 컬럼 조회
SELECT *
	FROM tbl_menu;
    
-- 연산자 사용
SELECT 7 + 4 FROM DUAL;
SELECT 7 - 4;
SELECT 7 * 4;
SELECT 7 / 4;
SELECT 7 % 4
