
from skppdp import anatomize, is_k_anonymous
import pandas as pd
import numpy as np
import os
import sys


def main():
    os.chdir(sys.path[0]) # Ensure we are in the same dir as data.
    data = pd.read_csv("datasample_01.csv")

    quid = ["age", "sex"] # Quasi-identifier columns.
    sensitive = ["disease"] # sensitive columns.
    for i in range(1,4):
        print(str(i)+"-anonymous:", is_k_anonymous(data, i, quid, sensitive))

    qit, st, max_prob = anatomize(data, quid, sensitive)
    print(qit)
    print(st)
    print(max_prob)


if __name__ == "__main__":
    main()
