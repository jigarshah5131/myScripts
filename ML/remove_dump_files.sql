set serveroutput on  echo on feed on
spool /tmp/remove_expdump_files.lst
begin
 for i in (select filename from (select * from table(RDSADMIN.RDS_FILE_UTIL.LISTDIR('RARSS_BLOB_DUMP')) order by mtime) where filename like '&1%')
 loop
  utl_file.fremove('RARSS_BLOB_DUMP',i.filename);
 end loop;
end;
/
spool off
exit
