DROP TABLE IF EXISTS member_info CASCADE;
DROP TABLE IF EXISTS team_info CASCADE;

CREATE TABLE IF NOT EXISTS member_info (
	member_code INT NOT NULL AUTO_INCREMENT COMMENT '회원코드',
    member_name VARCHAR(70) NOT NULL COMMENT '회원이름',
    birth_day DATE NULL COMMENT '생년월일',
    division_code CHAR(2) NULL COMMENT '구분코드',
    detail_info VARCHAR(500) NULL COMMENT '상세정보',
    contact VARCHAR(50) NOT NULL COMMENT '연락처',
    team_code INT NOT NULL COMMENT '소속코드',
    active_status CHAR(2) COMMENT '활동상태' default 'Y',
    CHECK(active_status IN ('Y', 'N', 'H')),
    CONSTRAINT pk_member_code PRIMARY KEY (member_code)
) ENGINE = INNODB COMMENT '회원정보';

CREATE TABLE IF NOT EXISTS team_info (
	team_code INT NOT NULL AUTO_INCREMENT COMMENT '소속코드',
    team_name VARCHAR(100) NOT NULL COMMENT '소속명',
    team_detail VARCHAR(500) NULL COMMENT '소속상세정보',
    use_yn CHAR(2) NULL COMMENT '사용여부',
    CONSTRAINT pk_team_code PRIMARY KEY (team_code)
);


use menudb;


-- [2-1] Q1.
SELECT category_code, category_name
	FROM tbl_category
		WHERE ref_category_code IS NOT NULL
			ORDER BY category_name DESC;

-- [2-2] Q2.
SELECT menu_name, menu_price
	FROM tbl_menu
		WHERE menu_price BETWEEN 20000 AND 30000;
        
-- [2-3] Q3.
SELECT *
	FROM tbl_menu
		WHERE menu_price < 10000 OR menu_name LIKE '%김치%'
			ORDER BY menu_price ASC, menu_name DESC;
            
-- [2-4] Q4.
SELECT *
	FROM tbl_menu
		WHERE tbl_menu.category_code NOT IN (SELECT category_code
					FROM tbl_category
						WHERE category_name LIKE '%기타%'
							OR category_name LIKE '%쥬스%'
							OR category_name LIKE '%커피%')
			AND menu_price = 13000;
