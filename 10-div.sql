-- Creates function SafeDiv that divides 
DELIMITER $$ ;
CREATE FUNCTION SafeDiv(
	a INT,
	b INT
)
RETURS FLOAT
DETERMINISTIC
BEGIN
	DECLARE result FLOAT;
	IF b = 0 THEN
		RETURN 0
	END IF;
	SET rESULT = (a	* 1.0) / b;
	RETURN result;
END;$$
DELIMITER ;

