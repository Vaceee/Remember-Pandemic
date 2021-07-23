USE bbsdb;



SELECT pst.id, usr.usr_name, pst.post_title, pst.post_content,
		pst.post_time, pst.post_repCnt, pst.post_clickCnt, pst.post_lastRepTime
FROM posts AS pst
LEFT JOIN users AS usr
ON usr.id = pst.usr_id
WHERE pst.post_deleted = 'N'
ORDER BY (0.7 * pst.post_clickCnt + 0.3 * pst.post_repCnt) / ((pst.post_lastRepTime - pst.post_time) / 1000) DESC
LIMIT 3 OFFSET 0;

SELECT pst.id, usr.usr_name, pst.post_title, pst.post_content,
		pst.post_time, pst.post_repCnt, pst.post_clickCnt, pst.post_lastRepTime
FROM posts AS pst
LEFT JOIN users AS usr
LEFT JOIN post_tag AS ptg
LEFT JOIN tags AS tg
ON usr.id = pst.usr_id AND pst.id = ptg.post_id AND ptg.tag_id = tg.id
WHERE pst.post_deleted = 'N'
ORDER BY (0.7 * pst.post_clickCnt + 0.3 * pst.post_repCnt) / ((pst.post_lastRepTime - pst.post_time) / 1000) DESC
LIMIT 3 OFFSET 0;