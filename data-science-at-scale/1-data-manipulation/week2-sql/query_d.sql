select count(*) from (select distinct docid from Frequency where term = "law" or term = "legal");
