set serveroutput on
DECLARE
  CURSOR c_upload
  IS
    select
        regexp_substr(regexp_replace(filename,'D',''),'[0-9]{4}') DIR
        --regexp_replace(filename,'RARSS.D','') filename
        ,filename
    from
        table(rdsadmin.rds_file_util.listdir('DATA_PUMP_DIR'))
    where filename like 'D%' order by mtime;
  bn varchar2(40) := 'fcs-ml-shared-pr0-dz-emr-fm-raw';
  task_id varchar2(40) ;
  kn varchar2(40) := 'RARSS';
  DPR varchar2(40) := 'DATA_PUMP_DIR';
  exec_text varchar2(4000);
BEGIN
--  bn := 'fcs-ml-shared-dv0-dz-emr-fm-raw';
  FOR r_upload IN c_upload
  LOOP
--    SELECT rdsadmin.rdsadmin_s3_tasks.upload_to_s3(p_bucket_name=> '''||bn||''',p_prefix => '''||r_upload.filename||''',p_s3_prefix => '''||kn||'/'||r_upload.DIR||'/'||''', p_directory_name => '''||DPR||''') AS TASK_ID FROM DUAL;
    exec_text := 'SELECT rdsadmin.rdsadmin_s3_tasks.upload_to_s3(p_bucket_name=> '''||bn||''',p_prefix => '''||r_upload.filename||''',p_s3_prefix => '''||kn||'/'||r_upload.DIR||'/'||''', p_directory_name => '''||DPR||''') AS TASK_ID FROM DUAL';
    DBMS_OUTPUT.PUT_LINE(exec_text);
    DBMS_OUTPUT.NEW_LINE;
    execute immediate exec_text into task_id;
    DBMS_OUTPUT.PUT_LINE('Task_id for '||r_upload.filename|| ' is '||task_id||'.');
    DBMS_OUTPUT.NEW_LINE;
  END LOOP;
END;
/
