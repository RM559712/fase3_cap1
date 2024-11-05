--------------------------------------------------------
--  Arquivo criado - sexta-feira-outubro-11-2024   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Trigger TRIGGER_CRP_ID
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "RM559712"."TRIGGER_CRP_ID" 
BEFORE INSERT ON CROP 
FOR EACH ROW 
BEGIN
  <<COLUMN_SEQUENCES>>
  BEGIN
    IF INSERTING AND :NEW.CRP_ID IS NULL THEN
      SELECT CROP_SEQ.NEXTVAL INTO :NEW.CRP_ID FROM SYS.DUAL;
    END IF;
  END COLUMN_SEQUENCES;
END;
/
ALTER TRIGGER "RM559712"."TRIGGER_CRP_ID" ENABLE;
