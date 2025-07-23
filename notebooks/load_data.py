import pandas as pd

def load_data(path="../data/ecommerce_data.csv"):
    df = pd.read_csv(path,index_col=0)
    return df

