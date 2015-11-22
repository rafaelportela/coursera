create view keywords as
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;

 select docid, sum(term_similarity) as doc_similarity from (
  select A.docid, B.term, sum(A.count * B.count) as term_similarity
    from keywords A, keywords B
    where A.term = B.term and A.docid < B.docid
      and B.docid = 'q'
    group by A.docid, B.term
) group by docid order by doc_similarity;
