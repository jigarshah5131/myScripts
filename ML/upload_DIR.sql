set serveroutput on
DECLARE
  CURSOR c_upload
  IS
select
        distinct regexp_substr(regexp_replace(filename,'.+.FDEMAF.D',''),'[0-9]{4}') DIR
        --regexp_replace(filename,'FDEMAF.D','') filename
--      ,filename
    from
        table(rdsadmin.rds_file_util.listdir('RARSS_BLOB_DUMP'))
    where regexp_substr(regexp_replace(filename,'.+.FDEMAF.D',''),'[0-9]{4}') like '2019'
   ;
 --   and filename like '%FDEMAF%D%';
  bn varchar2(40) := 'fcs-ml-shared-pr0-dz-emr-fm-raw';
  task_id varchar2(40) ;
  kn varchar2(40) := 'FDEMAF';
  DPR varchar2(40) := 'RARSS_BLOB_DUMP';
  exec_text varchar2(4000);
BEGIN
--  bn := 'fcs-ml-shared-dv0-dz-emr-fm-raw';
  FOR r_upload IN c_upload
  LOOP
--    SELECT rdsadmin.rdsadmin_s3_tasks.upload_to_s3(p_bucket_name=> '''||bn||''',p_prefix => '''||r_upload.filename||''',p_s3_prefix => '''||kn||'/'||r_upload.DIR||'/'||''', p_directory_name => '''||DPR||''') AS TASK_ID FROM DUAL;
    exec_text := 'SELECT rdsadmin.rdsadmin_s3_tasks.upload_to_s3(p_bucket_name=> '''||bn||''',p_prefix => ''B2XML'',p_s3_prefix => '''||kn||'/'||r_upload.DIR||'/'||''', p_directory_name => '''||DPR||''') AS TASK_ID FROM DUAL';
--    exec_text := 'SELECT rdsadmin.rdsadmin_s3_tasks.upload_to_s3(p_bucket_name=> '''||bn||''',p_prefix => ''D'||r_upload.DIR||''',p_s3_prefix => '''||kn||'/'||r_upload.DIR||'/'||''', p_directory_name => '''||DPR||''') AS TASK_ID FROM DUAL';
    DBMS_OUTPUT.PUT_LINE(exec_text);
    execute immediate exec_text into task_id;
    DBMS_OUTPUT.PUT_LINE('Task_id for '||r_upload.DIR|| ' is '||task_id||'.');
  END LOOP;
END;
/


--select regexp_substr(regexp_replace(filename,'FDEMAF.D',''),'[0-9]{4}') DIR ,regexp_replace(filename,'FDEMAF.D','') filename from table(rdsadmin.rds_file_util.listdir('RACSS_BLOB_DUMP')) where filename like 'FDEMAF%' order by mtime

    --exec_text :='alter table eps_owner.policypaymenttrans split partition  hiosdefault values ('''||c1rec.issid||''') into ( partition HIOS'||C1REC.issid||',partition hiosdefault) UPDATE GLOBAL INDEXES';
--    DBMS_STATS.GATHER_TABLE_STATS('EPS_OWNER', 'POLICYPAYMENTTRANS', PARTNAME=>PART_TEXT, estimate_percent => dbms_stats.auto_sample_size,method_opt => 'for all columns size skewonly', degree => 4,cascade => true);
--    DBMS_OUTPUT.PUT_LINE('Stats gathered for ' || part_text);
