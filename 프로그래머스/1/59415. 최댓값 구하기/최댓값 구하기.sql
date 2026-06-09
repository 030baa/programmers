-- 가장 최근 데이터 뽑기 방법 1 : 정렬과 상위행 이용하기
/*SELECT DATETIME
FROM ANIMAL_INS 
ORDER BY DATETIME DESC
LIMIT 1;*/

-- 가장 최근 데이터 뽑기 방법 2 : 집계함수 활용하기
SELECT MAX(DATETIME)
FROM ANIMAL_INS;