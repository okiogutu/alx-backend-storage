-- Creates index idx_name on the first letter of name and on the table names
CREATE INDEX idx_name_first ON names(name(1))

