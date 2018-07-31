#对通关总数超过3关的用户进行通关排名，并根据奖品表显示对应的奖品
#说明：通关书目越多排名越在片面，如果通关数目相同，那么早通关的排在前面

SELECT * FROM (SELECT *,COUNT(userid)AS totnum 
FROM gamegate GROUP BY userid HAVING COUNT(totnum))AS ONE 
JOIN arangeaward WHERE totnum>3
;


SELECT *,COUNT(userid)AS totnum 
FROM gamegate GROUP BY userid HAVING COUNT(totnum)

