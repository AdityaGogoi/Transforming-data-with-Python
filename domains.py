import read
import numpy as np
import pandas as pd

if __name__ == "__main__":
    df = read.load_data()
    domains = df['url'].values.tolist()
    domains = [str(i) for i in domains]
    domains = list(filter(lambda x: x!= 'nan', domains))
    #print(domains)
    domain_count={}
    for domain in domains:
        if domain in domain_count:
            domain_count[domain] += 1
        else:
            domain_count[domain] = 1
    inverse = [(value, key) for key, value in domain_count.items()]
    print (max(inverse))