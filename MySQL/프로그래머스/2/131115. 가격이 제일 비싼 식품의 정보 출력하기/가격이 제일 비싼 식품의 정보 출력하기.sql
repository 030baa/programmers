-- 가격이 제일 비싼 식품 정보 출력하기 
-- 1) 서브쿼리 활용하기
SELECT *
FROM FOOD_PRODUCT
WHERE  PRICE = (SELECT MAX(PRICE)
                    FROM FOOD_PRODUCT);

/*
-- 2) 정렬 및 LIMIT 활용하기
SELECT *
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
LIMIT 1;
*/
                    
                    