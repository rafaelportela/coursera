select docid, sum(term_similarity) from (
  select A.docid, B.term, sum(A.count * B.count) as term_similarity
    from Frequency A, Frequency B
    where A.term = B.term and A.docid < B.docid
      and A.docid = '10080_txt_crude' and B.docid = '17035_txt_earn'
    group by A.docid, B.term
) group by docid;
