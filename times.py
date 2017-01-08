import read
import numpy as np
import pandas as pd
from dateutil.parser import parse
    
def convert(string):
    datetime = parse(string, fuzzy=True)
    return(datetime.hour)

if __name__ == "__main__":
    df = read.load_data()
    sub_hour = df.apply(lambda row: convert(row['submission_time']), axis=1)
    #print(sub_hour)
    hour_count={}
    for hour in sub_hour:
        if hour in hour_count:
            hour_count[hour] += 1
        else:
            hour_count[hour] = 1
    
    inverse = [(value, key) for key, value in hour_count.items()]
    print (max(inverse))