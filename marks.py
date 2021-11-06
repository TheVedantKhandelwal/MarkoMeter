#Importing Libraries
import pandas as pd
import numpy as np
#Taking input for marks
inp = int(input('How many entries do you want to take?:'))
x = 0
while x <inp:
    p = input('How Much did you get in Physics? : \n')
    c = input('How much did you get in chemistry? : \n')
    m = input('How much did you get in Maths? : \n')
    p = int(p)
    c = int(c)
    m = int(m)
    data = pd.read_csv('C:/Users/khand/Documents/1234.csv')
    data = data.append({'Physics':p,'Chemistry':c,'Maths':m},ignore_index=True)
    data.drop(data.filter(regex="Unnamed:"),axis=1, inplace=True)
    data.to_csv("C:/Users/khand/Documents/1234.csv")
    x = x+1
import main
    
