import read
import numpy as np
import pandas as pd

if __name__ == "__main__":
    df = read.load_data()
    headline = df['headline'].values.tolist()
    headline = [str(i) for i in headline]
    long_string = " ".join(headline)
    #print(long_string)
    words = long_string.split()
    words=[x.lower() for x in words]
    word_count={}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    inverse = [(value, key) for key, value in word_count.items()]
    print (max(inverse))      
    #print(word_count)