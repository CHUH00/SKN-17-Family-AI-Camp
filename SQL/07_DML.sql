# DML

use menudb;

SELECT menu_code,
	   menu_name,
       menu_price,
       category_code,
       orderable_status
FROM tbl_menu;



# INSERT
-- INSERT INTO 테이블명 VALUES (컬럼순으로, 들어갈, 데이터, 나열, ...);
INSERT INTO tbl_menu 
	 VALUES (null, '회냉면', 12000, 4, 'Y');

INSERT INTO tbl_menu(menu_code, menu_name, menu_price, orderable_status, category_code)
	 VALUES (null, '직화불고기', 17000, 'Y', 4);

INSERT INTO tbl_menu(menu_name, menu_price, orderable_status, category_code)
	 VALUES ('카페라떼', 4500, 'Y', 7);

-- 여러 줄 INSERT하는 방법
INSERT INTO tbl_menu
	 VALUES (null, '화이트머쉬룸버거', 12000, 12, 'Y'), 
	   (null, '프렌치프라이', 2500, 12, 'Y'), 
       (null, '코울슬로', 1200, 12, 'Y');
       
INSERT INTO tbl_menu
	 VAlUES (100, '한방능이100숙', 1000000, 4, 'Y');


# UPDATE
-- UPDATE 테이블명
-- SET 컬럼명1 = 수정할 데이터,
-- 	컬럼명2 = 수정할 데이터2,
--     ...
-- [WHERE 수정 대상 데이터의 조건];

UPDATE tbl_menu
   SET menu_name = '100번이었던 음식',
	   menu_price = 19000
 WHERE menu_code = 100;


# DELETE
-- DELETE FROM 테이블명 [ WHERE 삭제 조건 ]; 

DELETE FROM tbl_menu
	  WHERE menu_code = 101;
      
DELETE FROM tbl_menu
   ORDER BY menu_code DESC
   LIMIT 6;
   
-- REPLACE
-- 중복값에 대해서는 데이터를 덮어 쓰고, 중복값이 없다면 INSERT
-- INTO 키워드는 생략 가능
INSERT INTO tbl_menu
	 VAlUES (100, '한방능이100숙', 1000000, 4, 'Y');

REPLACE INTO tbl_menu
	  VAlUES (100, '한방능이100숙', 10000, 4, 'Y');

REPLACE tbl_menu
 VAlUES (100, '한방능이100숙', 1000000, 4, 'Y');