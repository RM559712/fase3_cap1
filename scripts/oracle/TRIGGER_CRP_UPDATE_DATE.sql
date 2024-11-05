--------------------------------------------------------
--  Arquivo criado - sexta-feira-outubro-11-2024   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Trigger TRIGGER_CRP_UPDATE_DATE
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "RM559712"."TRIGGER_CRP_UPDATE_DATE" 
BEFORE UPDATE ON "CROP"
FOR EACH ROW
BEGIN
    :NEW.CRP_UPDATE_DATE := CURRENT_TIMESTAMP;  -- Atualiza a coluna com a data/hora atual
END;
/
ALTER TRIGGER "RM559712"."TRIGGER_CRP_UPDATE_DATE" ENABLE;
