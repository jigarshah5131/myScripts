set serveroutput on
begin
for c in (SELECT pdf.PHYSICAL_DOCUMENT_FILE_ID,regexp_replace(pdf.PHYSICAL_DOCUMENT_FILE_NAME,'^[0-9]+.[A-Za-z]+.','') fname ,pdf.PHYSICAL_DOCUMENT_BINARY_OBJEC from edge_owner.physical_document_file pdf where pdf.EDGE_JOB_FILE_TYPE_CD='RARSS' and pdf.physical_document_file_name like '%D2015%' and rownum <10) loop
SP_BLOB2FILE(c.PHYSICAL_DOCUMENT_FILE_ID,c.fname,c.PHYSICAL_DOCUMENT_BINARY_OBJEC);
end loop;
end;
/
