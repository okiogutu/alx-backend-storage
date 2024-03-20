-- Lists bands with glam rock as their main
SELECT band_name, (IF NULL(split, '2020') -formed) AS lifespan
	FROM metal_bands
	WHERE FIND_IN_SET('Glam rock', IFNULL(style, ""))
	ORDER BY lifespan DESC;

