"""
De-associates the relationship between the quasi-identifier and
the sensitive attributes.
"""

import pandas as pd
import numpy as np

def anatomize(data, quid, sensitive, group_column = "_group_id"):
    """Breaks the data into a table with the quasi-identifier attributes (quid)
       and another with the sensitive attributes. Both are related via a
       group_id attribute.

        Parameters
        ==========
        data : DataFrame object
              The data table.
        quid : seq
              The list of columns in data that are a quasi-identifier.
              These columns need to be discretized.
        sensitive: seq
              The list of columns in data that contain sensitive information.
        Returns
        =======
        qit : DataFrame object
              The quasi-identifier table.
        st : DataFrame object
              The sensitive data table.
        max_prob : real
              The maximum probability of inference of the sensitive info to
              a record if we know the group the individual is. 
    """
    # Create the group id for the different combinations.
    data_with_groupids = data.set_index(quid)
    # TODO: Replace hash with cryptographic, collision-resistant hash?
    data_with_groupids[group_column] = data_with_groupids.index.map(lambda k : hash(k))
    data_with_groupids = data_with_groupids.reset_index()

    # Group to produce the st table.
    grouped = data_with_groupids.groupby([group_column] + sensitive)

    # Compute the max prob
    max_prob = 0
    aux = data_with_groupids.groupby([group_column])
    for name, group in aux:
        # A series of frequencies of the sensitive columns per group:
        s = group.groupby(sensitive)[group_column].count()
        mp = s.max()/s.sum() # The max prob. for the group.
        if mp > max_prob:
            max_prob = mp

    # Include the new column in the lists of columns:
    quid.append(group_column)
    sensitive.append(group_column)

    # Note it may be more than one sensitive column.
    return data_with_groupids[quid], \
           grouped[sensitive[0]].agg(['count']).reset_index(), \
           max_prob
