# DISTINCT

SELECT category_code
	FROM tbl_menu
		ORDER BY category_code;
        
SELECT DISTINCT ref_category_code
	FROM tbl_category;
    
SELECT DISTINCT category_code, orderable_status
	FROM tbl_menu
		ORDER BY category_code, orderable_status;