import pandas as pd



def is_k_anonymous(data, k, quid, sensitive):
    """Determine if a table is k-anonymous for given k and quasi-identifier.
       If one record in the table has some value for qid, at least k − 1 other
       records also have the value qid.
    """
    grouped = data.groupby(quid)
    for name, group in grouped:
        # A series (or dataframe) of frequencies of the non-quid columns per group:
        s = group.count()
        if isinstance(s, pd.Series):
            s = pd.DataFrame(s)
        if s.ix[:,0].min()<k:  # Get the first column countings.
            return False
    return True
