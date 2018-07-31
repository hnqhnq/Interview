#9.对记录进行去重
#默认筛选出序号小的重复项
SELECT * FROM mygame GROUP BY game HAVING COUNT(game)>1;
#自定义筛出序号大的重复项
SELECT * FROM mygame WHERE id IN 
(SELECT MAX(id) FROM mygame GROUP BY game HAVING COUNT(game)>1)

#删除重复项
DELETE FROM mygame WHERE id IN
(SELECT id FROM (SELECT * FROM mygame GROUP BY game HAVING COUNT(game)>1)AS d )


#完美的去重留一
DELETE mygame FROM mygame,
(SELECT MIN(id)id,game,userid FROM mygame GROUP BY game HAVING COUNT(game)>1)AS d
WHERE mygame.game=d.game AND mygame.userid=d.userid AND mygame.id>d.id;