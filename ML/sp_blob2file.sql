
CREATE or REPLACE procedure SP_BLOB2FILE (pId integer,pFilename varchar2, pBlob blob) is
        v_file_w        UTL_FILE.FILE_TYPE;
        v_buffer        raw(32767);
        v_amount        binary_integer :=32767;
        v_pos           INTEGER :=1;
--        v_blob                BLOB;
        v_blob_len      INTEGER;
BEGIN

        v_blob_len      := dbms_lob.getlength(pBlob);
        v_file_w        := UTL_FILE.fopen('RARSS_BLOB_DUMP',pFilename,'wb',32767);

        WHILE v_pos <= v_blob_len LOOP
                DBMS_LOB.read(pBlob,v_amount,v_pos,v_buffer);
                UTL_FILE.put_raw(v_file_w,v_buffer,TRUE);
                v_pos := v_pos + v_amount;
        END LOOP;

        UTL_FILE.fclose(v_file_w);

EXCEPTION
        WHEN OTHERS THEN
                IF UTL_FILE.is_open(v_file_w) THEN
                        UTL_FILE.fclose(v_file_w);
                END IF;
                RAISE;
END;
/
--      SELECT physical_document_binary_objec
--      INTO p_blob
--      FROM EDGE_OWNER.PHYSICAL_DOCUMENT_FILE
--      WHERE PHYSICAL_DOCUMENT_FILE_ID=824561;
