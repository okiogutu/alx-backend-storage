-- Creates a list of need_meeting that has a score under 80
CREATE VIEW need_meeting AS SELECT name from students
AND (last_meeting IS NULL OR last_meeting < DATE(CURDATE() - INTERVAL 1 MONTH));
