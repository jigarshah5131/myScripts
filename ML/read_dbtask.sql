--set feed off long 500000 echo off pages 0 head off set lines 500 wrap off trimspool on
SET NEWPAGE 0
SET SPACE 0
SET LINESIZE 5000
SET PAGESIZE 0
SET ECHO OFF
SET FEEDBACK OFF
SET VERIFY OFF
SET HEADING OFF
SET MARKUP HTML OFF SPOOL OFF
col text format a2000
spool /tmp/rl.lst
SELECT text FROM table(rdsadmin.rds_file_util.read_text_file('BDUMP','&1'));
--exit
