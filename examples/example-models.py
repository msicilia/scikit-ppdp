
from skppdp import anatomize, is_k_anonymous
import pandas as pd
import os
import sys


def main():
    os.chdir(sys.path[0]) # Ensure we are in the same dir as data.
    data = pd.read_csv("datasample_02.csv")
    print(data)
    quid = ["job", "sex", "age"] # Quasi-identifier columns.
    sensitive = ["name"] # sensitive columns.
    for i in range(1,6):
        print(str(i)+"-anonymous:", is_k_anonymous(data, i, quid, sensitive))


if __name__ == "__main__":
    main()
