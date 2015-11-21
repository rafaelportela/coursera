select count(*) from (
  select f.docid, count(f.count) as total_terms
  from Frequency f
  group by f.docid
  having total_terms > 300
) x;
