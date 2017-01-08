import pandas as pd
import sys


def load_data():
    dataframe={}
    dataframe=pd.read_csv("hn_stories.csv")
    dataframe.columns=['submission_time','upvotes','url','headline']
    return dataframe

if __name__ == "__main__":
    data=load_data()
    print(data.head(2))
    