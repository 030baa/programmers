-- 2022년 5월 1일을 기준으로 출고여부를 분류하는 SQL문(출고완료/출고대기/출고미정)
SELECT ORDER_ID, PRODUCT_ID, OUT_DATE,
    CASE WHEN OUT_DATE IS NULL THEN "출고미정"
         WHEN OUT_DATE > DATE("2022-05-01") THEN "출고대기"
         ELSE "출고완료" END AS "출고여부"
FROM FOOD_ORDER
ORDER BY ORDER_ID;
