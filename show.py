import pandas as pd
import numpy as np
def show():#To display CSV as a dataframe
    data = pd.read_csv('YOUR PATH HERE')
    data.drop(data.filter(regex="Unnamed:"),axis=1, inplace=True)
    print(data)

show()
import main
