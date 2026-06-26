-- 음식종류별로 즐겨찾기수가 가장 많은 식당의 음식 종류, ID, 식당 이름, 즐겨찾기수를 조회
  -- 다중행 다중컬럼 서브쿼리
/*SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM  REST_INFO
WHERE (FOOD_TYPE, FAVORITES) IN (SELECT FOOD_TYPE, MAX(FAVORITES)
                     FROM REST_INFO
                     GROUP BY FOOD_TYPE) 
ORDER BY 1 DESC; */

-- 여러 조건으로 조인하기 : 음식종류별 최대 즐겨찾기 수 테이블과 원테이블을 조인하기
SELECT A.FOOD_TYPE, A.REST_ID, A.REST_NAME, A.FAVORITES
FROM  REST_INFO A
INNER JOIN (SELECT FOOD_TYPE, MAX(FAVORITES) AS FAVORITES
                     FROM REST_INFO
                     GROUP BY FOOD_TYPE) B
ON A.FOOD_TYPE=B.FOOD_TYPE AND A.FAVORITES=B.FAVORITES
ORDER BY 1 DESC;
                     