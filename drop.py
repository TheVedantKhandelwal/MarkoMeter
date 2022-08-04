import pandas as pd
import numpy as np
def drop():#Dropping rows from CSV
    
    data = pd.read_csv('YOUR PATH HERE')
    data.drop(data.filter(regex="Unnamed:"),axis=1, inplace=True)
    print(data)
    
    inp = int(input('Enter row number to be cleared'))
    data = data.drop([inp])
    print(data)
    
    data.to_csv("C:/Users/khand/Documents/1234.csv")
drop()
import main