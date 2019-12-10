select filename from table(rdsadmin.rds_file_util.listdir('RARSS_BLOB_DUMP')) where filename like 'B2XML%' order by mtime ;
