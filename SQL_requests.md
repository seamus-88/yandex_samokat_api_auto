# 1 задание. Cписок логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 
```
SELECT
    "Couriers"."login",
COUNT(*)
FROM
    "Orders"
LEFT JOIN "Couriers" ON "Orders"."courierId" = "Couriers"."id"
WHERE
    "Orders"."inDelivery" = True
GROUP BY "Couriers"."login";
```
# 2 задание: трекеры заказов и их статусы
```
SELECT
    "Orders"."track",
CASE
    WHEN "Orders"."finished" = True THEN 2
    WHEN "Orders"."cancelled" = True THEN -1
    WHEN "Orders"."inDelivery" = True THEN 1
    ELSE 0
END as expectedStatus
FROM
    "Orders";
```
