CREATE VIEW minprice AS
SELECT author_name
    , SUM(amount) AS qty
	    FROM
		    author a INNER JOIN book b
		    ON a.author_id = b.author_id
	    GROUP BY author_name
		HAVING SUM(amount) = (
						SELECT MIN(sum_amount) AS min_amount
						FROM(
							SELECT author_id, SUM(amount) AS sum_amount
								FROM book
								GROUP BY author_id
							) ms
			                    );

--SELECT author_name, qty
--	FROM public.minprice;