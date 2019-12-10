set serveroutput on
begin
for c in (SELECT pdf.PHYSICAL_DOCUMENT_FILE_ID,'B2XML.'||pdf.PHYSICAL_DOCUMENT_FILE_NAME fname ,pdf.PHYSICAL_DOCUMENT_BINARY_OBJEC from edge_owner.physical_document_file pdf where pdf.EDGE_JOB_FILE_TYPE_CD='FDEEAF' and pdf.physical_document_file_name like '%D2019%' ) loop
SP_BLOB2FILE(c.PHYSICAL_DOCUMENT_FILE_ID,c.fname,c.PHYSICAL_DOCUMENT_BINARY_OBJEC);
end loop;
end;
/
