#/bin/sh

# Backup example db
mysqldump -v -uroot -p example > /tmp/dump.sql

# Restore sample
mysql -uroot -p sample < /tmp/dump.sql

# Dump help_keyword limit 100 rows
mysqldump -uroot -p --where="true limit 100" mysql help_keyword > /tmp/help_keyword.sql
